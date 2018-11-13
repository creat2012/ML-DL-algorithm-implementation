from kmeans import *

if __name__ == '__main__':
	data = generator_points(100)
	for point in data:
		print("(%d, %d)" % (point[0], point[1]))

	km = Kmeans(data, 3)
	km.kmeans()
