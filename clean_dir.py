import os
import cv2

def clean_dir(dirname):
	os.system("cd  "+dirname);
	filelist=map(lambda x:os.path.join(dirname,x),os.listdir(dirname));
	for f in filelist:
		print f
		if f.lower().endswith("jpg"):
			img=cv2.imread(f)
			if (abs(img.shape[1]-600)<100 and abs(img.shape[0]-400)<100):
				pass
			else:
				os.system("rm "+f)


def main():
	for i in range(24,25):
		clean_dir(str(i))

if __name__ == "__main__":
    main()