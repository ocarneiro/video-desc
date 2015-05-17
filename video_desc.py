import os, subprocess

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0].decode('UTF-8')
  for resultline in result.rsplit(sep="\n"):  #quebra o resultado em linhas
        if 'Duration' in resultline:
            print (resultline)

print ("Lendo diretório: ", os.getcwd())
for filename in os.listdir():
    print (" -- Lendo arquivo: ", filename)
    ext = filename[-3:] #extensão do arquivo
    if ext == 'MOV' or ext == 'MP4': #se for um vídeo...
        getLength(filename)



