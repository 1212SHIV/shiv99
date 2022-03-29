import os
import shutil


#"C:\Users/shiv3/OneDrive/Desktop/python/a""C:\Users/shiv3/OneDrive/Desktop/python/a"
source = input("Enter the source folder:- ")
destination = input("Enter the destination folder:-")

source = source + '/'
destination = destination + '/'

listfiles = os.listdir(source)

for file in listfiles:
    shutil.copy((source+file) , destination)
 