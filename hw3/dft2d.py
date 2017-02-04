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

def dft2d(image, flags):
	h,w = image.shape[:2]
	image_shift = np.zeros((h,w),np.uint8)
	output = np.zeros((h,w),np.complex)
	for x in range(h):
		for y in range(w):
			image_shift[x,y] = image[x,y]*(-1)**(x+y)
	output = dft_matrix(h,'dft').dot(image_shift).dot(dft_matrix(w,'dft'))
	if flags == 'dft':
		return output
	elif flags == 'idft':
		inverse_output = float(1/(h*w))*dft_matrix(h,'idft').dot(output).dot(dft_matrix(w,'idft'))
		inverse_output_shift = np.zeros((h,w),np.uint8)
		for x in range(h):
			for y in range(w):
				inverse_output_shift[x,y] = inverse_output[x,y].real*(-1)**(x+y)
		return inverse_output_shift

if __name__ == '__main__':
	flag = input("please enter flags such as dft or idft: ")
	img = cv2.imread('75.png',0)
	if flag == 'dft':
		output = dft2d(img, flag)
		cv2.imwrite('test.png',(1+np.log(np.abs(output)))**2)
	elif flag == 'idft':
		output = dft2d(img, 'idft')
		cv2.imwrite('test1.png', output)