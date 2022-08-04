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
    fileExiste = exists("/home/user/yourpath") #verifica se o arquivo existe
    
    dataString = convertTupleToString(data) #transform the tuple in a string with the ','

    if fileExiste == False: #se o arquivo nao existe é necessario criar o cabeçalho e inserir os dados
        f = open("/home/user/yourpath", "w")
        f.write("id,data,datasys,longitude,latitude,odometro,velocidade,ignicao,rpm,transparent_data,ibutton,dir,in1,out1,out2,gps,gprs,horimetro,voltagem,temperatura,contador,motivo,pacote")
        f.write('\n')
        f.write(dataString)
        f.write('\n')
        f.close()
    else: #se o arquivo existe é necessario inserir os dados
        f = open("/home/londero/gateway/python/GV53MG/csvTrack.csv", "a")
        f.write(dataString)
        f.write('\n')
        f.close()

