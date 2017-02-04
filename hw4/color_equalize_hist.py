#encoding: utf-8
import cv2
import numpy as np
import equalize_hist as hist
import rgb_and_hsi

def separate_channel(img):
	m, n = img.shape[:2]
	b = np.zeros((m,n), np.float)
	g = np.zeros((m,n), np.float)
	r = np.zeros((m,n), np.float)
	b[:,:] = img[:,:,0]
	g[:,:] = img[:,:,1]
	r[:,:] = img[:,:,2]
	'''
	或者用opencv的函数：
	b = cv2.split(img)[0]
	'''
	return b, g, r
if __name__ == '__main__':
	img = cv2.imread('test.png',3)
	m, n = img.shape[:2]
	#cv2.imwrite('task_2_test.png', hist.equalize_hist(img))
	#cv2.imwrite('task_2_test.png', hist.calcAndDrawHist(img))
	channels = separate_channel(img)
	b, g, r = channels[:3]
	b_h = hist.getHist(b)
	r_h = hist.getHist(r)
	g_h = hist.getHist(g)
	'''
	#第一小问：三个通道分别做均衡化，再合并
	b_eq = hist.equalize_hist(b,b_h)
	g_eq = hist.equalize_hist(g,g_h)
	r_eq = hist.equalize_hist(r,r_h)
	img_new = np.dstack([b_eq,g_eq,r_eq])
	cv2.imwrite('75_new.png', img_new)
    '''

	#第二小问：取三个通道的直方图的平均数进行均衡化：
	average = (b_h+r_h+g_h)/3.0
	b_eq_2 = hist.equalize_hist(b,average)
	g_eq_2 = hist.equalize_hist(g,average)
	r_eq_2 = hist.equalize_hist(r,average)
	img_aver_eq = np.dstack([b_eq_2,g_eq_2,r_eq_2])
	cv2.imwrite('75_rgb_aver_eq.png', img_aver_eq)

	'''
	#第三小问：先转到hsi,i分量做均衡化再转回rgb
	img_hsi = rgb_and_hsi.rgb2hsi(img)
	channels_hsi = separate_channel(img_hsi)
	h,s,i = channels_hsi[:3]
	i_h = hist.getHist(i)
	i_eq = hist.equalize_hist(i,i_h)
	hsi_new = np.dstack([h, s, i_eq])
	rgb_new = rgb_and_hsi.hsi2rgb(hsi_new)
	cv2.imwrite('test_hsi_eq.png', rgb_new)
    '''
	'''
	img_new = np.zeros((m,n,3),np.float)

	img_new[:,:,0] = b[:,:]
	img_new[:,:,1] = g[:,:]
	img_new[:,:,2] = r[:,:]'''
