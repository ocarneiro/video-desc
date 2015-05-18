#! /usr/bin/env python3
import os, subprocess

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0].decode('UTF-8')
  for resultline in result.rsplit(sep="\n"):  #quebra o resultado em linhas
        if 'Duration' in resultline:
            #print (resultline) # Duration: 00:01:26.89, start: 0.000000, bitrate: 11975 kb/s
            words = resultline.split(sep=" ")
            duration = words[3]
            #print ("Duração: ", duration[:-1])
            time = duration[:-1].split(sep=':')
            #print(time)
            #print ("Duração: ", time[0], "h", time[1], 'm', time[2], 's')
            print ("%s - %sh%sm%ss" % (filename, time[0], time[1], time[2]))
            #wcount = 0
            #for word in words:
            #    print (wcount, " = ", word)
            #    wcount += 1

print ("Lendo diretório: ", os.getcwd())
for filename in os.listdir():
    #print (" -- Lendo arquivo: ", filename)
    ext = filename[-3:] #extensão do arquivo
    if ext == 'MOV' or ext == 'MP4': #se for um vídeo...
        getLength(filename)



