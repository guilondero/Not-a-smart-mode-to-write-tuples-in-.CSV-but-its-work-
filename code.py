import csv
import os
from os.path import exists 




def convertTupleToString(tuple):
    tuple = list(tuple)  #the tuple need to be a list
    stringTotal = ''  #string to recive all datas 

    for i in tuple: 
        string = str(i) #making the data a string 
        stringTotal = stringTotal + ',' + string #concated the string in the stringTotal

    if stringTotal[0] == ',': #remove the first ',' 
        stringTotal = stringTotal[1:] 

    return stringTotal]
    

def CSVfile(data):
    fileExiste = exists("/home/user/yourpath/CSVFILE.csv") #verify if the file exist, return a bolean 
    
    dataString = convertTupleToString(data) #transform the tuple in a string with the ','
    
    header = "id,time,value,otherValue,someValue"  #header for the  csv 

    if fileExiste == False: #if the file dont existe, need create and write the HEADER 
        f = open("/home/user/yourpath/CSVFILE.csv", "w")   #path where the file is gonna be save 
        f.write(header)    
        f.write('\n')
        f.write(dataString)
        f.write('\n')
        f.close()
    else: #if the file existe, just need to write the dataString
        f = open("/home/user/yourpath/CSVFILE.csv", "a")
        f.write(dataString)
        f.write('\n')
        f.close()

