import shutil
import os

class invert:
  def __init__(self, file):
    
    self.file = file
    
  def invertFile(self):  
    try:
      os.remove("work/"+self.file)    
      
    except FileNotFoundError:
      pass
    
    fileCopy = open("work/"+self.file, "x")

    shutil.copyfile("input/"+self.file, "work/"+self.file)
    
    arr = bytearray()
    with open("work/"+self.file, "rb") as f:
        for b in f:
            arr += bytearray(b)
        for i in range(len(arr)):
            arr[i] = ~arr[i] + 256
  
    with open("work/"+self.file, "wb") as f:
        f.write(arr)

    fileCopy.close()

    
  def finish(self):

    try:
      os.remove("output/"+self.file)
      
    except FileNotFoundError: 
      pass
    
    newFile = open("output/"+self.file, "x")

    shutil.copyfile("work/"+self.file, "output/"+self.file)
    
    arr = bytearray()
    with open("output/"+self.file, "rb") as f:
        for b in f:
            arr += bytearray(b)
        for i in range(len(arr)):
            arr[i] = ~arr[i] + 256
  
    with open("output/"+self.file, "wb") as f:
        f.write(arr)

    newFile.close()
    