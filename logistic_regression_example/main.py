

import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.utils.data as Data
from LogisticRegression import LogisticRegression
import csv
INPUT_SIZE = 784
OUTPUT_SIZE = 10

EPOCH = 10

BATCH_SIZE = 100
BASE_LEARNING = 0.0001

def ReadData(file):
	"""read the txt from file; return the data;"""
	X = []
	Y = []
	with open(data.csv) as f:
		for xy in f.readlines():
			X.append([float(xy.split()[0]),])
			Y.append([float(xy.split()[1]),])
	# print (data)
	return (np.array(X, dtype=np.float32), np.array(Y, dtype=np.float32))

# train_data
train_dataset = dsets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
# test data
test_dataset = dsets.MNIST(root='./data', train=False, transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=False)
## define the model
foward_net = LogisticRegression(INPUT_SIZE, OUTPUT_SIZE)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(foward_net.parameters(), lr=BASE_LEARNING )


def train(epoch):
	""" train for one epoch"""
	for i, (images, labels) in enumerate(train_loader):
		images = Variable(images.view(-1, 28 * 28))
		labels = Variable(labels)

		optimizer.zero_grad()
		outputs = foward_net(images)    # forward
		loss = criterion(outputs, labels) # loss
		print (labels)
		loss.backward()  # backwards
		optimizer.step() # updata the parameters
	print("loss = %.4lf"%(loss))

def test():
	total = 0
	correct = 0
	for images, labels in test_loader:
		images = Variable(images.view(-1, 28 * 28))
		outputs = foward_net(images)
	
		_, predicted = torch.max(outputs.data, 1)
		total += labels.size(0)
		correct += (predicted == labels).sum()
	print("total : %d, correct %d"%(total, correct))
	print("accuary : %.4lf"%( 100. * correct / total))

#train
for epoch in range(EPOCH):
	train(epoch)
test()


