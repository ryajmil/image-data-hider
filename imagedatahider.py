import sys
from PIL import Image
from shutil import copyfile

class ImageDataHider():

    def __init__(self):
        self.keyFName = ""
        self.keyOutFName = ""
        self.dataFName = ""
        self.cipherFName = ""
        self.cipherOutFName = ""
    
    def extract(self): 
        try:
                keyImg = Image.open(self.keyFName)
                dataImg = Image.open(self.cipherFName)
        except:
                print("Error: One of these files do not exist")
                return

        outputFile = open(self.cipherOutFName,"a+")

        height,width = keyImg.size
        
        for x in range(height):
                for y in range(width):
                        keyR,keyG,keyB,keyO = keyImg.getpixel((x,y))
                        dataR,dataG,dataB,dataO = dataImg.getpixel((x,y))
                        
                        if dataO != keyO:
                                return
                        val = abs(dataR - keyR) + abs(dataG - keyG) + abs(dataB - keyB)
                        outputFile.write(chr(val))

    def hide(self):
            
        try:
                dataFile = open(self.dataFName)
        except:
                print("Error: Data file does not exist!")
                sys.exit()
        #copy the image so that we have the alter key picture ouput
        keyOutput = self.cipherOutFName
        #keyOutput = input('Enter a name for the output file: ')
        copyfile(self.keyFName,keyOutput)
        
        
        keyImg = Image.open(keyOutput)
        height,width = keyImg.size

        # get the data into a integer array
        dataString = dataFile.read()
        dataIntArray = []
        for x in range(len(dataString)):
                dataIntArray.append(ord(dataString[x]))

        dataIdx = 0
        heightIdx = 0
        widthIdx = 0
        
        while dataIdx < len(dataIntArray):
                r,g,b,o = keyImg.getpixel((heightIdx,widthIdx))
                val = dataIntArray[dataIdx] / 3

                #print("Before:\nr = {0}\tg = {1}\tb = {2}\tval={3}".format(r,g,b,val))

                if r + val <= 255:
                        r += val
                else:
                        r -= val

                if g + val <= 255:
                        g += val
                else:
                        g -= val
                
                if dataIntArray[dataIdx] % 3 != 0:
                        val += dataIntArray[dataIdx]%3

                if b + val <= 255:
                        b += val
                else:
                        b -= val
                #print("After:\nr = {0}\tg = {1}\tb = {2}\tval={3}\n\n".format(r,g,b,val))
                if dataIdx+1 == len(dataIntArray):
                        if o == 255:
                                o =- 1
                        else:
                                o += 1
                
                keyImg.putpixel((heightIdx,widthIdx),(int(r),int(g),int(b),int(o)))


                dataIdx += 1
                #print("dataIdx = {0} datalen = {1}".format(dataIdx,len(dataIntArray))
                if widthIdx+1 < width:
                        widthIdx += 1
                else:
                        widthIdx = 0
                        if heightIdx+1 < height:
                                heightIdx += 1

        keyImg.save(keyOutput)
