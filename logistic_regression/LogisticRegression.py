import torch
import torch.nn as nn


class LogisticRegression(nn.Module):
	"""docstring for LogisticRegression"""
	def __init__(self, input_size, output_size):
		super(LogisticRegression, self).__init__()
		self.linear = nn.Linear(input_size, output_size)
		
	def forward(self, x):
		out = self.linear(x)
		return out