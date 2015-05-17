import os, subprocess

def getLength(filename):
  #result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()[0].decode('UTF-8')
  result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT).communicate()
  if result[0]:
      print('----------- ZERO -------------')
      print (result[0].decode('UTF-8'))
  if result[1]:
      print('-----------  UM  -------------')
      print (result[1].decode('UTF-8'))
  #print(type(result))
  #print(type(result.stdout.readlines()))
  #for resultline in result.stdout.readlines():
    #  if 'Duration' in resultline:
    #      print (resultline)
  #return [x for x in result.stdout.readlines() if "Duration" in x]

print (os.getcwd())
for filename in os.listdir():
    print (filename)
    ext = filename[-3:]
    if ext == 'MOV' or ext == 'MP4':
        print ('vídeo!')
        getLength(filename)



