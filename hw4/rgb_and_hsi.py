#encoding utf-8
import cv2
import numpy as np 
import math

def rgb2hsi(img):
	m,n = img.shape[:2]
	img_hsi = np.zeros((m,n,3),np.float)
	b = np.zeros((m,n),np.float)
	g = np.zeros((m,n),np.float)
	r = np.zeros((m,n),np.float)
	b[:,:] = img[:,:,0]
	g[:,:] = img[:,:,1]
	r[:,:] = img[:,:,2]
	img_hsi[:,:,2] = (b + g + r)/3
	for i in range(m):
		for j in range(n):
			if img[i,j,0] == img[i,j,1] == img[i,j,2]:
				img_hsi[i,j,0] = 0
				img_hsi[i,j,1] = 0
			else:
				img_hsi[i,j,1] = 1 - 3.0*min(b[i,j],g[i,j],r[i,j])/((b[i,j]+g[i,j]+r[i,j]))
				numerator = 0.5*(2.0*r[i,j]-b[i,j]-g[i,j])
				temp1 = (r[i,j]-g[i,j])**2
				temp2 = (r[i,j]-b[i,j])*(g[i,j]-b[i,j])
				denominator = float(np.power(temp1+temp2, 0.5))
				theta = np.arccos(float(numerator)/float(denominator))*180.0/np.pi
				if b[i,j] > g[i,j]:
					img_hsi[i,j,0] = 360 - theta
				else:
					img_hsi[i,j,0] = theta
	return img_hsi
def hsi2rgb(img_hsi):
	m,n = img_hsi.shape[:2]
	img = np.zeros((m,n,3),np.float)
	temp1 = img_hsi[:,:,2]*(1 - img_hsi[:,:,1])
	temp_h = (img_hsi[:,:,0] - (img_hsi[:,:,0]//120)*120)*np.pi/180.0
	temp2 = (img_hsi[:,:,1]*np.cos(temp_h)/np.cos(np.pi/3 - temp_h) + 1)*img_hsi[:,:,2]
	temp3 = 3.0 * img_hsi[:,:,2] - (temp1 + temp2)
	for i in range(m):
		for j in range(n):
			if 0 <= img_hsi[i,j,0] < 120:
				img[i,j,0] = temp1[i,j]
				img[i,j,1] = temp3[i,j]
				img[i,j,2] = temp2[i,j]
			elif 120 <= img_hsi[i,j,0] < 240:
				img[i,j,0] = temp3[i,j]
				img[i,j,1] = temp2[i,j]
				img[i,j,2] = temp1[i,j]
			elif 240 <= img_hsi[i,j,0] < 360:
				img[i,j,0] = temp2[i,j]
				img[i,j,1] = temp1[i,j]
				img[i,j,2] = temp3[i,j]
	return img
if __name__ == '__main__':
	img = cv2.imread('00.png')
	img_hsi = rgb2hsi(img)
	'''
	cv2.imwrite('hehehe_i.png', img_hsi[:,:,2])
	
	cv2.imwrite('hehehe_s.png', img_hsi[:,:,1]*255)
	cv2.imwrite('hehehe_h.png', img_hsi[:,:,0]*255/360.0)
	'''
	img1 = hsi2rgb(img_hsi)
	cv2.imwrite('rgb2hsi2rgb_00.png', img1)
	'''
	img_hsi[:,:,1] = img_hsi[:,:,1]*255
	img_hsi[:,:,0] = img_hsi[:,:,0]*255/360.0
	cv2.imwrite('hsi.png',img_hsi)
	'''
