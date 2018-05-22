from PIL import Image
import numpy
import matplotlib.pyplot as plt


class ConcScan:

    def imageData(self, imgPath):  # calculate and return light absorbance array for a given image
        img = Image.open(imgPath).convert('LA')  # open image
        pxl = img.load()  # load image
        imgSize = img.size  # get tuple of image size
        # iterate through each pixel in image and store intensity in 'intensityArr'
        intensityArr = []
        for y in range(imgSize[0]):
            for x in range(imgSize[1]):
                intensityArr.append(pxl[x, y])
        # iterate through each pixel value tuple, calculate and store  absorbance in 'pcentArr'
        pcentArr = []
        for val in intensityArr:
            pcentArr.append(2-numpy.log10(100*float(val[0]/255)))
        return pcentArr  # return array

    def conc(self, data):  # calculate and return concentration array for a given absorbance array
        eCof = 15.2  # molar extension coefficient (M^-1*cm^-1)
        len = 1  # path length (cm)
        # iterate through each data value, calculate and store concentration in 'concArr'
        concArr = []
        for val in data:
            c = val/eCof*len  # concentration (M)
            concArr.append(c)
        return concArr  # return array

    def plotData(self, arr1, arr2):  # given two arrays, plot them against each other
        plt.plot(arr1, arr2, 'ro') # plot given arrays
        # define labels
        plt.ylabel('Absorbance')
        plt.xlabel('Concentration (M)')
        plt.show()  # display plot
