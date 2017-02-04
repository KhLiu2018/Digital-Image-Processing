#encoding: utf-8
import cv2
import numpy as np

def dft_matrix(N, flags):
	i,j = np.meshgrid(np.arange(N), np.arange(N))
	if flags == 'dft':
		omega = np.exp(-2j*np.pi/N)
	elif flags == 'idft':
		omega = np.exp(2j*np.pi/N)
	w = np.power(omega, i*j)
	return w

def dft2d_for_matrix(matrixs): #矩阵的傅里叶正变换
	h,w = matrixs.shape[:2]
	matrix_shift = np.zeros((h,w),np.float)
	output = np.zeros((h,w),np.complex)
	for x in range(h):
		for y in range(w):
			matrix_shift[x,y] = matrixs[x,y]*(-1)**(x+y)
	output = dft_matrix(h,'dft').dot(matrix_shift).dot(dft_matrix(w,'dft'))
	return output

def idft2d_for_matrix(matrixs): #矩阵的傅里叶逆变换
	h,w = matrixs.shape[:2]
	inverse_output = float(1/(h*w))*dft_matrix(h,'idft').dot(matrixs).dot(dft_matrix(w,'idft'))
	inverse_output_shift = np.zeros((h,w), np.float)
	for x in range(h):
		for y in range(w):
			inverse_output_shift[x,y] = inverse_output[x,y].real*(-1)**(x+y)
	return inverse_output_shift

def filter2d_freq(img, filters):
	h,w = img.shape[:2]
	n = len(filters)
	img_pad = np.zeros((h*2, w*2), np.float)
	img_pad[:h,:w] = img
	img_dft = dft2d_for_matrix(img_pad)
	filters_pad = np.zeros((h*2, w*2), np.float)
	filters_pad[:n,:n] = filters
	filters_dft = dft2d_for_matrix(filters_pad)
	g_freq = img_dft * filters_dft
	inverse_output_shift = idft2d_for_matrix(g_freq)
	return inverse_output_shift[:h,:w]

if __name__ == '__main__':
	img = cv2.imread('75.png',0)
	filters = np.array([[1,1,1],[1,-8,1],[1,1,1]])
	cv2.imwrite('ftest1.png',filter2d_freq(img, filters))
	filter7mul7 = np.ones((7,7))
	filter7mul7 *= float(1)/float(7*7)
	cv2.imwrite('fftest1.png',filter2d_freq(img, filter7mul7))
	