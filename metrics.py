''' Author: Yashwanth Remidi
	Email: yashwanthremidi@gmail.com

	Functional units for metrics, encoders and decoders used in machine learning algorithms.
	Note: Please also check essentials.py for libraries
'''


from essentials import *


def IoU():
	'''
	Description: IoU of single image predicted(P) and Ground Truth(G) = (P ∩ G)/ (P ∪ G)
	 at thresholds range(0.5, 0.95, 0.05) => [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]

	IoU = intersected pixels / union pixels 

	Note: Intersected pixels will be lesser than or equal to the ground truth and Union pixels will be greater than equal to ground truth

	precision at threshold (t) = TP / TP + FP + FN

	TP: hit with prediction and ground truth
	FP: prediction didn't hit
	FN: ground truth was not hit 

	Note: FP and FN are both same. so the formula = TP/(TP + ~TP)

	precision of image = 1/n_tresh * ∑ precision t

	IoU metric = mean(precision of images)
	'''

	pass


def rle_encode(img):
    '''
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated '''

    pixels = img.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)


def rle_decode(mask_rle, shape):
    '''
    mask_rle: run-length as string formated (start length)
    shape: (height,width) of array to return 
    Returns numpy array, 1 - mask, 0 - background '''

    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape)


