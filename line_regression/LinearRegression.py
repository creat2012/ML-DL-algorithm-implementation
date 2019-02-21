import torch
import torch.nn as nn

class LinearRegression(nn.Module):
	"""docstring for LinearRegression"""
	def __init__(self, input_size, output_size):
		super(LinearRegression, self).__init__()
		self.linear = nn.Linear(input_size, output_size)

	def forward(self, x):
		out = self.linear(x)
		return out
		