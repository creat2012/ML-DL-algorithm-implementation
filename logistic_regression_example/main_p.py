import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.utils.data as Data
from LogisticRegression import LogisticRegression
import csv
import numpy as np
import pandas as pd
INPUT_SIZE = 26
OUTPUT_SIZE = 2

EPOCH = 200

BATCH_SIZE = 1000
BASE_LEARNING = 0.1

data = pd.read_csv("./data/data.csv")
data = data.drop(['id', 'time'], axis = 1)
data = data.values
data_test = data[-400:, :]
np.random.shuffle(data)
data = np.mat(data)
for i in range(np.shape(data)[1]):
	meanval = np.mean(data[np.nonzero(~np.isnan(data[:, i].A))[0], i])
	data[np.nonzero(np.isnan(data[:, i].A))[0], i] = meanval

data = np.array(data)
#print (data)
#np.random.shuffle(data)
#print (data)
#print (data)
#print (len(data))
X = data[:, :-1]
X = X.astype('float32')
x = data[-1, :]
print (x)
#X.dtype = 'float32'
print (len(X))
Y = data[:, -1]
Y = Y.astype('int64')

print (len(Y))
X = torch.from_numpy(X)
Y = torch.from_numpy(Y)

test_X = data_test[:, :-1]
test_Y = data_test[:, -1]
test_X = test_X.astype('float32')
test_Y = test_Y.astype('int64')
print (len(test_Y))
test_X  = torch.from_numpy(test_X )
test_Y = torch.from_numpy(test_Y)
### data set
train_dataset = Data.TensorDataset(X, Y)

### data loader 
train_loader = Data.DataLoader(
    dataset=train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=2
)

foward_net = LogisticRegression(INPUT_SIZE, OUTPUT_SIZE)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(foward_net.parameters(), lr=BASE_LEARNING )



def train(epoch):
	""" train for one epoch"""
	

	for i, (x, y) in enumerate(train_loader):
		#print (i)
		x = Variable(x)
		y = Variable(y)

		optimizer.zero_grad()
		outputs = foward_net(x)    # forward
		loss = criterion(outputs, y) # loss
		#print (labels)
		loss.backward()  # backwards
		optimizer.step() # updata the parameters
	print("loss = %.4lf"%(loss))

def test():
	total = 0
	correct = 0
	x = test_X
	y = test_Y
	outputs = foward_net(x)
	_, predicted = torch.max(outputs.data, 1)
	total += y.size(0)
	correct += (predicted == y).sum()
	

	print("total : %d, correct %d"%(total, correct))
	print("accuary : %.4lf"%( 100. * correct / total))

#train
for epoch in range(EPOCH):
	train(epoch)
test()
