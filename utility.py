import numpy as np
import math
import matplotlib.pyplot as plt


#function to get average value of the matrix
def matrixAverage(M, order):
    M = np.array(M)
    rval = 0
    for r in range(0, len(M)):
        for c in range(0, len(M[0])):
            rval += M[r, c]
    rval = rval / (order ** 2)
    rval = math.ceil(rval)
    return rval

#function to get index of max arg in a 2d python list
def maxIndex(lst2d):
    maxima = 0
    rparam = []
    for i in lst2d:
        if maxima < i[2]:
            maxima = i[2]
            rparam = i
        else:
            pass
    return rparam


#function to compress the image by averaging
def compressor(ImgMatrix, Order):
    ImgMatrix = np.array(ImgMatrix)
    Rows = len(ImgMatrix)
    Columns = len(ImgMatrix[0])
    StartRow, StartCol = 0, 0
    m = math.floor(Rows / Order)
    n = math.floor(Columns / Order)
    CompressedImg = np.empty((m, n))
    for i in range(0, m):
        StartCol = 0
        for j in range(0, n):
            M = ImgMatrix[StartRow: StartRow + Order, StartCol: StartCol + Order]
            compressedVal = matrixAverage(M, Order)
            CompressedImg[i, j] = int(compressedVal)
            StartCol += Order
        StartRow = StartRow + Order
        CompressedImg = CompressedImg.astype(np.uint8)
    return CompressedImg

#function to compress the image without averaging (faster than compressor)
def lessFrame(imgMatrix, skipVAl):
    imgMatrix = np.array(imgMatrix)
    rows = len(imgMatrix)
    columns = len(imgMatrix[0])
    m = math.floor(rows / skipVAl)
    n = math.floor(columns / skipVAl)
    startRow, startCol = 0, 0
    outputImg = np.empty((m, n))
    for i in range(0, m):
        startCol = 0
        for j in range(0, n):
            val = imgMatrix[startRow, startCol]
            outputImg[i, j] = val
            startCol += skipVAl
        startRow += skipVAl

    return outputImg.astype(np.uint8)

#to get the co-ordinates of brightest sub matrix inside image matrix
def brightestSubsetMatrix(img_matrix, order):
    rows = len(img_matrix)
    columns = len(img_matrix[0])
    m = math.floor(rows/order)
    n = math.floor(columns/order)
    startRow, startCol = 0, 0
    holdLst = []
    for i in range(0, m):
        startCol = 0
        for j in range(0, n):
            M = img_matrix[startRow: startRow + order, startCol: startCol + order]
            averageVal = matrixAverage(M, order)
            tempLst = [startRow, startCol, averageVal]
            holdLst.append(tempLst)
            startCol += order
        startRow = startRow + order

    return maxIndex(holdLst)

#plot class
class Plot:
    def __init__(self, res):
        self.xData = []
        self.yData = []
        self.xLim = res*1.77777
        self.yLim = -res
        self.fig, self.axes = plt.subplots()
        self.line, = self.axes.plot(self.xData, self.yData)
        self.axes.set_xlim(0, self.xLim)
        self.axes.set_ylim(self.yLim, 20)
        plt.show(block=False)


    def rt_plot(self, x, y):
        self.xData.append(x)
        self.yData.append(y)
        if len(self.xData) > 200:
            self.xData = self.xData[len(self.xData) - 200: len(self.xData)]
            self.yData = self.yData[len(self.yData) - 200: len(self.yData)]
        self.line.set_xdata(self.xData)
        self.line.set_ydata(self.yData)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.01)

    def close(self):
        plt.close(self.fig)

    






