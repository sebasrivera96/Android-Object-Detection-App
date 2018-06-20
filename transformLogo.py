"""
    Author: Sebastian Rivera Gonzalez
    Date: 19.06.2018
    Artificial Intelligence & Robotics Labs
    
    OBJECTIVE: Grow a dataset of images to create a Deep Learning Model, e.g. 
    a SSD-Mobilenet to recognize the Continental Logo.
"""
#----------------------------------LIBRARIES------------------------------------
import cv2
import os
import numpy as np
#-------------------------------------------------------------------------------

'''
This function rotates the image 'angle' degrees.
INPUT:
    - img loaded with function cv2.imread(FILE_NAME)
    - angle of rotation
    - rows of img
    - cols of img
OUTPUT:
    - dstImg -> Rotated image
'''
def rotateImage(img, angle, rows, cols):
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    dstImg = cv2.warpAffine(img, M, (cols, rows))
    return dstImg

'''
This function creates a modified version of the original image with an 
horizontal and a vertical displacements.
INPUT:
    - x1 is the horizontal displacement
    - x2 is the vertical displacement
    - img is an image or frame loaded with the function cv2.imread(FILE_NAME)
OUTPUT: 
    - dst which is a displaced version of the original image
'''
def translateImage(x1,x2,img):
    rows,cols,_ = img.shape
    M = np.float32([[1,0,x1],[0,1,x2]])
    dst = cv2.warpAffine(img,M,(cols,rows))
    # cv2.imshow("image",dst)
    # cv2.waitKey(0)
    return dst

'''
This function will create the variants of the original logo to increase the 
train and test datasets.
INPUT:
    No input because the function will seach for all the files within the actual
    directory that end with .jpg
OUTPUT: 
    No return value. All the modified images will be stored on `pwd`
'''
def createVariantsOfLogo():
    currentDirectory = "."
    originalImages = []
    for fileName in os.listdir(currentDirectory):
        if fileName.endswith(".jpg"):
            originalImages.append(fileName)
    for fileName in originalImages:
        # Load the image and store number of rows and columns
        img = cv2.imread(fileName)
        rows,cols,_ = img.shape
        # Remove the .jpg to create the new files
        ACT_IMG = fileName[:-4]
        # Transform from BGR to GRAY sclae and save
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(ACT_IMG+'_gray.jpg',gray_img)
        # Transform from BGR to HSV color space and save
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imwrite(ACT_IMG+'_hsv.jpg',hsv_img)
        # Transform from BGR to YUV color space and save
        yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        cv2.imwrite(ACT_IMG+'_yuv.jpg',yuv_img)
        # Blur the image with a 5x5 kernel and save
        blur = cv2.blur(img,(5,5))
        cv2.imwrite(ACT_IMG+'_blur.jpg',blur)
        # Erode the image with a 5x5 kernel and save
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(img,kernel,iterations = 1)
        cv2.imwrite(ACT_IMG+'_erosion.jpg',erosion)
        # Dilate the image with a 5x5 kernel and save
        dilation = cv2.dilate(img,kernel,iterations = 1)
        cv2.imwrite(ACT_IMG+'_dilation.jpg',dilation)
        # Rotate the image 45, 90, 135, 180, 225, 270 and 315 degrees and
        # save each modification
        for angle in range(45,316,45):
            dst = rotateImage(img, angle, rows, cols)
            cv2.imwrite(ACT_IMG + '_' + str(angle) + '.jpg',dst)
        # Displace the original image into 8 different positions
        for hor in range(-75,76,75):
            for ver in range(-75,76,75):
                if hor != 0 or ver != 0:
                    dst = translateImage(hor,ver,img)
                    cv2.imwrite(ACT_IMG + '_trans_' + str(hor) + '_' + str(ver) + '.jpg',dst)
                    
'''
This function will resize all the images on the current direcotry to a size
FINAL_ROWS x FINAL_COLUMNS pixels. All the images will be resized and stored
with the same name on the same directory.
INPUT:
    - FINAL_ROWS with default of 320 px
    - FINAL_COLUMNS with default of 480 px
OUTPUT: 
    - All the images on the current directory wil be resized. No return value.
'''
def resizeImages(FINAL_ROWS=320.0, FINAL_COLUMNS=480.0):
    currentDirectory = "."
    for fname in os.listdir(currentDirectory):
        if fname.endswith(".jpg"):
            img = cv2.imread(fname)
            rows,cols,_ = img.shape
            FX = FINAL_ROWS/float(rows)
            FY = FINAL_COLUMNS/float(cols)
            img = cv2.resize(img, (0,0), fx=FY, fy=FX)
            cv2.imwrite(fname, img)
            # print img.shape

'''
The main function will first resizeImages and then create the variants of the 
images found on the currentDirectory
'''
def main():
    resizeImages()
    createVariantsOfLogo()

if __name__ == '__main__':
    main()
