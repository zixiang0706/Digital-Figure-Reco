[TOC]


# Background
add

This project uses`OpenCV`, `Pytorch` and `PyQt5`

# Install

- the develop environment: `Pycharm CE` IDE with `Python 3.6`
- use `pip3` to install related dependence
  `pip3 install -r requirements.txt`


# introduction
it is the v1.0 version, based on `Python 3.6`

## Dependence
all the dependence and its version is 
`pip3 install -r requirements.txt`

## File architecture
- asset: some temp file which is required by the project. DO NOT delete it
- backup: old version of code, no need to care about it
- input: some outsider resource used. E.g. dataset used by training NN 
- output: some raw file generated during running. operate it at will
- UI: auto generated code by IDE, which is used as UI. DO NOT delete it

## Quick start
the entry of this project is the `main.py` under the root of this project
- main  
    - myGUI 
        - myDialog 
        - myQlabel
    - myCamera
        - myPreProcessing
        - myCNN
    - myTCP_Client  

for independent module design, different module communicate each other by single-direction queue
the queue is named by  producer and consumer:

# Structure Introduction

## File architecture

- asset: some temp file which is required by the project. DO NOT delete it
- backup: old version of code, no need to care about it
- input: some outsider resource used. E.g. dataset used by training NN 
- output: some raw file generated during running. operate it at will
- UI: auto generated code by IDE, which is used as UI. DO NOT delete it
 
for independent module design, different module communicate each other by single-direction queue
the queue is named by  producer and consumer:
![queue](/asset/queue.jpg)

## dic
DICT = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
        17: 'Down', 18: 'Up', 19: 'Ring', 20: 'L', 21: '-'}
        
## basic func
1. digital figure reco
2. save image
3. retrain NN

# Roadmap

1. add one more UI which can help user to add customized items to be recognized.
2. update the CNN architecture, use transfer-learning based on `MNIST handwritten digit` will be a cool idea
3. currently architecture of CNN is based on Gray-image clipped by OpenCV, which means that when this clipping-image is wrong or contain other information. then, the CNN will output wrong result. So, use YOLO V3 maybe a good idea to recognize digit.

# Authors

Andew Chu in Schindler Elevator AP CO team.

Mail: `andrew.chu@schindler.com`

# License

This Project is licensed under the terms of the GPL Open Source license and is available for free.

Any conflict to the copyright of others, please contact author of this project to rectify it.

NOTICE: `PyQt5`is in Commercial and GPL license which means it has restriction with commercial-purpose usage. If there is any demand to use this project in commercial affair, you can simple use `Pyside2` to replace `PyQt5`

