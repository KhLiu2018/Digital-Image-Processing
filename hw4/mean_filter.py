#encoding:utf-8
import cv2
import numpy as np
import itertools # 用于将二维数组变成一维
from operator import mul #用于连乘
from functools import reduce

def various_filter(img, filter_size, choose):
	m, n = img.shape[:2]
	img_1 = padding_zero(img, filter_size)
	m_1, n_1 = img_1.shape[:2]
	img_2 = np.zeros((m_1-filter_size+1, n_1-filter_size+1))
	for i in range(img_2.shape[0]):
		for j in range(img_2.shape[1]):
			temp = img_1[i:i+filter_size,j:j+filter_size]
			if choose == 'ha':
				img_2[i,j] = harmonic_mean(temp, filter_size)
			elif choose == 'con':
				img_2[i,j] = contraharmonic_mean(temp, filter_size)
			elif choose == 'ari':
				filters = np.ones((filter_size,filter_size))
				filters *= float(1)/float(filter_size*filter_size)
				img_2[i,j] = matrix_filter(temp, filters)
			elif choose == 'med':
				img_2[i,j] = median_filter(temp, filter_size)
			elif choose == 'min':
				img_2[i,j] = min_filter(temp, filter_size)
			elif choose == 'geo':
				img_2[i,j] = geometric_mean(temp, filter_size)
	return img_2[filter_size-1:filter_size+m-1,filter_size-1:filter_size+n-1]
def padding_zero(img, filter_size):
	m,n = img.shape[:2]
	img_1 = np.zeros((m+2*filter_size-2,n+2*filter_size-2))
	img_1[filter_size-1:filter_size+m-1,filter_size-1:filter_size+n-1] = img
	return img_1
def matrix_filter(matrixs, filters):
    filter_size = len(filters)
    result = matrixs * filters
    ans = sum(sum(result))
    return ans
def median_filter(matrixs, filter_size):
	matrixs_1 = list(itertools.chain.from_iterable(matrixs))
	sorted_matrix = sorted(matrixs_1)
	return sorted_matrix[filter_size*filter_size//2]
def min_filter(matrixs, filter_size):
	matrixs_1 = list(itertools.chain.from_iterable(matrixs))
	sorted_matrix = sorted(matrixs_1)
	return sorted_matrix[0]
def geometric_mean(matrixs, filter_size):
	for i in range(matrixs.shape[0]):
		for j in range(matrixs.shape[1]):
			if matrixs[i,j] == 0:
				matrixs[i,j] = 1
	matrixs_1 = list(itertools.chain.from_iterable(matrixs))
	return reduce(mul, np.power(matrixs_1, 1.0/float(filter_size**2)))
def harmonic_mean(matrixs, filter_size):
	ans = 0
	for i in range(filter_size):
		for j in range(filter_size):
			if matrixs[i,j] == 0:
				return 0
			else:
				ans = ans + float(1)/float(matrixs[i,j])
	return float(np.power(filter_size, 2))/float(ans)
def contraharmonic_mean(matrixs, filter_size):
	q = -1.5
	ans_num = sum(sum(np.power(matrixs, q+1)))
	ans_den = sum(sum(np.power(matrixs, q)))
	if ans_den == 0:
		return 0
	return ans_num/ans_den
if __name__ == '__main__':
	img = cv2.imread('task_2.png', 0)
	'''
	cv2.imwrite('3x3hm.png', various_filter(img, 3, 'ha'))
	cv2.imwrite('9x9hm.png', various_filter(img, 9, 'ha'))
	cv2.imwrite('3x3hmcontra.png', various_filter(img, 3, 'con'))
	cv2.imwrite('9x9hmcontra.png', various_filter(img, 9, 'con'))
	'''
	#cv2.imwrite('3x3ari.png', various_filter(img, 3, 'ari'))
	#cv2.imwrite('3x3med.png', various_filter(img, 3, 'med'))
	cv2.imwrite('3x3geo.png', various_filter(img, 3, 'geo'))
