import torch
import torch.nn as nn



class LogisticRegression(nn.Module):
	"""docstring for LogisticRegression"""
	def __init__(self, input_size, output_size):
		super(LogisticRegression, self).__init__()
		self.norm = nn.BatchNorm1d(input_size)
		self.fc1 = nn.Linear(input_size, output_size)
		
		
	def forward(self, x):
		out = self.norm(x)
		out = self.fc1(out)
		return torch.sigmoid(out)