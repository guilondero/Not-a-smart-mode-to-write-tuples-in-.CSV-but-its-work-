import csv
import os


def convertTupleToString(tuple):
    tuple = list(tuple)  #the tuple need to be a list
    stringTotal = ''  #string to recive all datas 

    for i in tuple: 
        string = str(i) #making the data a string 
        stringTotal = stringTotal + ',' + string #concated the string in the stringTotal

    if stringTotal[0] == ',': #remove the first ',' 
        stringTotal = stringTotal[1:] 

    return stringTotal
