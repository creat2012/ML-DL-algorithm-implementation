import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from LinearRegression import LinearRegression

INPUT_SIZE = 1
OUTPUT_SIZE = 1
EPOCHS = 100
DATA_PATH = "./data.txt"

def ReadData(file):
	"""read the txt from file; return the data;"""
	X = []
	Y = []
	with open(file) as f:
		for xy in f.readlines():
			X.append([float(xy.split()[0]),])
			Y.append([float(xy.split()[1]),])
	# print (data)
	return (np.array(X, dtype=np.float32), np.array(Y, dtype=np.float32))


if __name__ == '__main__':
	xy_data = ReadData(DATA_PATH)
	# xy_plo
	plt.figure()
	plt.scatter(xy_data[0], xy_data[1])
	plt.show()

	## line regression mode
	model = LinearRegression(INPUT_SIZE, OUTPUT_SIZE)
	criterion = nn.MSELoss()
	optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)
	
	## train 
	for epoch in range(EPOCHS):
		# epochs = 10 
		inputs = Variable(torch.from_numpy(xy_data[0]))
		targets = Variable(torch.from_numpy(xy_data[1]))
		
		# forwards
		outputs = model(inputs)
		loss = criterion(outputs, targets)

		# backwards
		optimizer.zero_grad()
		loss.backward() # it's not ness
		optimizer.step()

		print("Epoch[%d/10], loss : %.4lf" % (epoch, loss))
	#model.eval()
	predicted = model(Variable(torch.from_numpy(xy_data[0]))).data.numpy()
	plt.plot(xy_data[0], xy_data[1], 'ro')
	plt.plot(xy_data[0], predicted, label='predict')
	plt.legend()
	plt.show()
