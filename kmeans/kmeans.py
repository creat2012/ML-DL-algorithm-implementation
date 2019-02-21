from random import *
import matplotlib.pyplot as plt
def generator_points(num, x_rand = 100, y_rand = 100):
	""" generate num  points """
	data = []
	for i in range(num):
		data.append((randint(0, x_rand) , randint(0, y_rand)))
	return data

class Kmeans(object):
	def __init__(self, data, k):
		self.data = data
		self.k = k
		self.cluster = []
		for i in range(self.k):
			self.cluster.append([])
		self.center = []
		self.error = 0
	
	def init_center(self):
		""" choose k samples that in data init as the center"""
		if self.k > len(self.data):
			print("the length of data is smaller than k")
		else:
			for i in range(self.k):
				self.center.append(self.data[i])
		for center in self.center:
			print("(%f, %f)"%(center[0], center[1]))

	def compute_dis(self, x, y):
		return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])

	def print_center(self):
		print("the num of center:", self.k)
		for point in self.center:
			print("(%f, %f)" % (point[0], point[1]))

	def print_cluster(self):
		print("the cluster is", self.k)
		for cluster in self.cluster:
			for point in cluster:
				print("(%d, %d)", point[0], point[1])
	def plot(self):
		print("in plot")
		plt.figure()
		for point in self.data:
			plt.plot(point[0], point[1], 'ro')
		for center in self.center:
			plt.plot(center[0], center[1], 'bo')
		plt.show()
		print("end plot")
	def plot2(self):
		color_shape = ['ro', 'go', 'yx']
		plt.figure()
		cnt = 0
		for cluster in self.cluster:
			for point in cluster:
				plt.plot(point[0], point[1], color_shape[cnt])
			cnt += 1
		for center in self.center:
			plt.plot(center[0], center[1], 'bo')
		plt.show()
		print("end plot")

	def compute_error(self):
		for i in range(self.k):
			for point in self.cluster[i]:
				self.error += self.compute_dis(self.center[i], point)
		print("error : ", self.error)

	def kmeans(self):
		self.init_center()
		center_change = True
		self.plot()
		while center_change:
			center_change = False
			temp_cluster = []
			for i in range(self.k):
				temp_cluster.append([])
			self.print_center()
			for sample in self.data:
				belong_center = 0
				min_dis = self.compute_dis(sample, self.center[0])
				for i in range(len(self.center)):
					dist = self.compute_dis(sample, self.center[i]) 
					if dist < min_dis:
						min_dis = dist
						belong_center = i
				if sample not in self.cluster[belong_center]:
					center_change = True
				print("(%d, %d) belong %d" % (sample[0], sample[1], belong_center))
				# this sample is belong the belong_center
				temp_cluster[belong_center].append(sample)
			# the center is not changed
			if center_change == False:
				break
			# update the cluster
			self.cluster = temp_cluster
			# updata the center
			print("temp cluster ", temp_cluster) 
			for i in range(len(temp_cluster)):
				print(temp_cluster[i])
				sum_x = 0
				sum_y = 0
				for sample in temp_cluster[i]:
					sum_x += sample[0]
					sum_y += sample[1]
				self.center[i] = (sum_x / len(temp_cluster[i]), sum_y / len(temp_cluster[i]))
			self.compute_error()
			self.plot2()
