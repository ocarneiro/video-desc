#! /usr/bin/env python3
import os, subprocess
import sys
import magic

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

def getFileInfo(filename):
    type_media, ext = getFileType(filename)
    if type_media == "video": #se for um vídeo...
        getLength(filename)
    else:
        print("Arquivo: " + filename + " não é um vídeo.")

def getFileType(filename):
    f = magic.Magic(mime=True)
    ftype = str(f.from_file(filename), 'UTF-8')
    print(ftype)
    return ftype.split("/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print ("Lendo arquivo: ", filename)
        getFileInfo(filename)
    else:
        print ("Lendo diretório: ", os.getcwd())
        for filename in os.listdir():
            if os.path.isfile(filename):
                getFileInfo(filename)

