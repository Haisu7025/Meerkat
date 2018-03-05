import torch
import torchvision
from torchvision import utils, datasets
from torch.utils import data
from torch.autograd import Variable
import random
import os
import shutil
import logger
import models

log = logger.init_logger('cross_val')
part = False


def part_data(num=10):
    # organize files in operating system to attain 10-cross
    defaced_num = 0
    legitimate_num = 0
    def_file_list = range(defaced_num)
    leg_file_list = range(legitimate_num)
    random.shuffle(def_file_list)
    random.shuffle(leg_file_list)

    for i in range(10):
        os.mkdir('data/{}'.format(i))
        os.mkdir('data/{}/def'.format(i))
        os.mkdir('data/{}/leg'.format(i))

        for file_index in def_file_list[i * 1000:(i + 1) * 1000]:
            shutil.move('data/def.{}.jpg'.format(file_index),
                        'data/{}/def'.format(i))
        for file_index in leg_file_list[i * 1000:(i + 1) * 1000]:
            shutil.move('data/leg.{}.jpg'.format(file_index),
                        'data/{}/leg'.format(i))


def cross_val(val_index, dataloaders, data_sizes, model, criterion, optimizer):
    stime = time.time()

    # training phase
    running_corrects = 0.0
    for i in range(10):
        if i == val_index:
            continue
        else:
            model.train()
            for batch_x, batch_y in enumerate(dataloaders[i]):
                inputs, labels = batch_y
                if torch.cuda.is_available():
                    inputs = inputs.cuda()
                    labels = labels.cuda()
                inputs, labels = Variable(inputs), Variable(labels)

                optimizer.zero_grad()

                outputs = model(inputs)
                _, preds torch.max(outputs.data, 1)
                loss = criterion(outputs, labels)

                loss.backward()
                optimizer.step()

                running_corrects += torch.sum(preds == labels.data)

            train_acc = running_corrects / dataset_sizes[0]
            log.info('Validation Index [{}].[{}] \t Validation Phase Accuracy: {:.4f}'.format(
                val_index, 10, train_acc))


# prepare datasets
img_folder = 'data/snapshots'
img_datasets = {x: datasets.ImageFolder(
    'data/snapshots/{}'.format(x), None) for x in range(10)}
dataloaders = {x: data.DataLoader(
    img_datasets[x], batch_size=10, shuffle=True, num_workers=2) for x in range(10)}
dataset_sizes = {x: len(img_datasets[x]) for x in range(10)}

# model and training
model = models.SAE()
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 10-cross validation
for val_index in range(10):
    # re-init the network
    model = models.SAE()
    if torch.cuda.is_available():
        model = model.cuda()
    cross_val(val_index, dataloaders, dataset_sizes,
              model, criterion, optimizer)
