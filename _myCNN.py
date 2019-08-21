#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 12:36
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : _myCNN.py
# @Software: PyCharm
"""
Description:
"""


import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, utils
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
import random
import matplotlib.pyplot as plt

DICT = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
        17: 'Down', 18: 'Up', 19: 'Ring', 20: 'L', 21: '-'}

CATEGERY = len(DICT.keys())
SEED = 0
SAVE_PATH = './asset/model1.pkl'
torch.manual_seed(SEED)
random.seed(SEED)


class MyDataset(Dataset):
    def __init__(self, path, transform):
        print('INFO: load img from system')
        self.imgs_labels = []
        for root, directory, files in os.walk(path):
            for file in files:
                if file.endswith('.png'):
                    img = Image.open(root + file).convert('L')
                    label = int(file.split('-')[0])
                    # self.imgs_labels.append((img,label))
                    for i in range(-9, 9, 3):
                        self.imgs_labels.append((transform(img.rotate(i)), label))

        random.shuffle(self.imgs_labels)
        print('img number:', len(self.imgs_labels))
        print('img size:', self.imgs_labels[0][0].size())

    def __getitem__(self, index):
        return self.imgs_labels[index][0], self.imgs_labels[index][1]

    def __len__(self):
        return len(self.imgs_labels)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 4, kernel_size=1)
        self.conv2 = nn.Conv2d(4, 8, kernel_size=3)
        self.mp = nn.MaxPool2d((2, 2))
        self.fc1 = nn.Linear(840, 512)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, CATEGERY)

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        x = x.view(in_size, -1)  # flatten the tensor
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = (self.fc3(x))
        return F.log_softmax(x)

    def retrieve_features(self, x):
        feature_map1 = F.relu(self.conv1(x))
        x = self.pool(feature_map1)
        feature_map2 = F.relu(self.conv2(x))
        return feature_map1, feature_map2


# 显示图像
def show_img(test_loader):
    for i, (batch_x, batch_y) in enumerate(test_loader):
        if i < 4:
            print(i, batch_x.size(), batch_y.size())
            show_batch(batch_x)
            plt.axis('off')
            plt.show()


def show_batch(imgs):
    grid = utils.make_grid(imgs)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')


def rightness(predictions, labels):
    pred = torch.max(predictions.data, 1)[1]  #
    rights = pred.eq(labels.data.view_as(pred)).sum()  #
    return rights, len(labels)  #


# 1.准备数据
transforms_list = transforms.Compose([
    transforms.ToTensor()])


def main(batch_size=64, learning_rate=0.003, epoches=15, q_cnn2gui=None):
    dataSet = MyDataset(path='./input/dataSet/', transform=transforms_list)

    indices = range(len(dataSet))
    indices_train = indices[:int(len(dataSet) * 0.7)]
    indices_val = indices[int(len(dataSet) * 0.7) + 1:int(len(dataSet) * 0.85)]
    indices_test = indices[int(len(dataSet) * 0.85) + 1:]

    sampler_train = torch.utils.data.sampler.SubsetRandomSampler(indices_train)
    sampler_val = torch.utils.data.sampler.SubsetRandomSampler(indices_val)
    sampler_test = torch.utils.data.sampler.SubsetRandomSampler(indices_test)
    train_loader = DataLoader(dataset=dataSet,
                              batch_size=batch_size,
                              sampler=sampler_train,
                              shuffle=False)
    validation_loader = DataLoader(dataset=dataSet,
                                   batch_size=batch_size,
                                   sampler=sampler_val)
    test_loader = DataLoader(dataset=dataSet,
                             batch_size=batch_size,
                             sampler=sampler_test)

    # 4.prepare net
    model = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
    optimizer.zero_grad()

    # show img
    # show_img(test_loader)

    # 5.start training
    print('INFO: start training NN')
    record = []
    weights = []
    for epoch in range(epoches):
        train_rights = []
        for batch_idx, (data, target) in enumerate(train_loader):
            model.train()
            output = model(data)
            loss = criterion(output, target)
            optimizer.zero_grad()
            # loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
            right = rightness(output, target)
            train_rights.append(right)

            if batch_idx % 100 == 0:
                model.eval()
                val_rights = []
                for (data_t, target_t) in validation_loader:
                    output = model(data_t)
                    right = rightness(output, target_t)
                    val_rights.append(right)

                train_r = (sum([tup[0] for tup in train_rights]), sum([tup[1] for tup in train_rights]))
                val_r = (sum([tup[0] for tup in val_rights]), sum([tup[1] for tup in val_rights]))
                train_string = 'epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}\ttrain accuracy: {:.2f}%\tval acc: {:.2f}%'.\
                    format(epoch, batch_idx * batch_size, len(train_loader.dataset),
                           100. * batch_idx / len(train_loader), loss.item(),
                           100. * train_r[0] / train_r[1],
                           100. * val_r[0] / val_r[1])
                print(train_string)
                if q_cnn2gui is not None:
                    q_cnn2gui.put({"train_progress": train_string})

                record.append((100 - 100. * train_r[0] / train_r[1], 100 - 100. * val_r[0] / val_r[1]))

                weights.append([model.conv1.weight.data.clone(), model.conv1.bias.data.clone(),
                                model.conv2.weight.data.clone(), model.conv2.bias.data.clone()])
    # #6.plot
    # plt.figure(figsize=(10, 7))
    # plt.plot(record)
    # plt.xlabel('Steps')
    # plt.ylabel('Error rate')
    # plt.show()
    model.eval()
    vals = []
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            val = rightness(output, target)
            vals.append(val)

    rights = (sum([tup[0] for tup in vals]), sum([tup[1] for tup in vals]))
    right_rate = (1.0 * rights[0].numpy() / rights[1])
    print('test accurace:', right_rate)
    # 10.save model
    torch.save(model, SAVE_PATH)


def predict(model, img):
    # model = torch.load('model.pkl')
    img = transforms_list(img).unsqueeze(0)
    with torch.no_grad():
        y_pred = model(img)
        pred = y_pred.data.max(1, keepdim=True)[1]
        find_num = int(pred[0][0].numpy())
        find_num = DICT[find_num]

    return find_num


if __name__ == '__main__':
    main()