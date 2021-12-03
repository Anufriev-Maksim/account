import numpy as np

def masfun(img, y, x):
	if(y >= 0 and x >= 0 and y < img.shape[0] and x < img.shape[1]):
		if img[y,x] == 1:
			return 1
	return 0

def sumi(img, y, x, mix = 1):
	return (
		masfun(img, y-mix, x) + 
		masfun(img, y+mix, x) + 
		masfun(img, y, x-mix) + 
		masfun(img, y, x+mix) +
		masfun(img, y-mix, x-mix) + 
		masfun(img, y+mix, x+mix) + 
		masfun(img, y+mix, x-mix) + 
		masfun(img, y-mix, x+mix)
	)
	
def countElem(img):
	count = [0, 0, 0, 0, 0, 0]

	for y in range(0, img.shape[0], 2):
		for x in range(0,img.shape[1], 2):
			if img[y,x] == 1:
				c = sumi(img, y, x, mix = 2)
				if c == 4:

					if masfun(img, y,x-2) == 0:
						count[1] += 1

					if masfun(img, y-2,x) == 0:
						count[0] += 1

					if masfun(img, y,x+2) == 0:
						count[3] += 1

					if masfun(img, y+2,x) == 0:
						count[2] += 1

				if c == 5:

					if masfun(img, y+2,x) + masfun(img, y-2,x)  == 1:
						count[4] += 1

					if masfun(img, y,x-2) + masfun(img, y,x+2)  == 1:
						count[5] += 1

	ar = np.array([ 
		[1,0,1],
		[1,1,1] 
		])
	ar2 = np.array([ 
		[1,1,1],
		[1,1,1] 
		])

	for i in range(len(count) - 2):
		print(ar)
		print(count[i])
		ar = np.rot90(ar)

	for i in range(4, len(count)):
		print(ar2)
		print(int(count[i]/2))
		ar2 = np.rot90(ar2)




img = np.load("ps.npy").astype("uint")
countElem(img)