import os

f = open("Github_Repos","r")
line = f.readline()

while line:
    if line == 'END OF INPUT':
        break
    data = line.strip().split(' ')
    os.mkdir(data[0])
    os.chdir(data[0])
    url = "git clone " + data[1] + " . >> ../clone_log.txt 2>&1"
    os.system(url)
    os.chdir('..')
    line = f.readline()
f.close()