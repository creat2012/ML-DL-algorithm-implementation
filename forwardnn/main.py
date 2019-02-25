import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import torch.utils.data as Data
from ForwardNN import ForwardNN

INPUT_SIZE = 784
HID_SIZE = 500
OUTPUT_SIZE = 10

EPOCH = 5

BATCH_SIZE = 100
BASE_LEARNING = 0.001

# train_data
train_dataset = dsets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
# test data
test_dataset = dsets.MNIST(root='./data', train=False, transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=False)
## define the model
foward_net = ForwardNN(INPUT_SIZE, HID_SIZE, OUTPUT_SIZE)
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


