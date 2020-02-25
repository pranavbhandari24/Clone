import os


# Open the text file with the Github Repos
f = open("Github_Repos","r")
line = f.readline()
# Recording the start time in the log file
os.system("echo -n Start Time : >> clone_log.txt; date +\"%T\" >> clone_log.txt")

# Loop to read the file line by line
while line:
    if line == 'END OF INPUT':
        break
    data = line.strip().split(' ')
    os.mkdir(data[0])
    # Forking a child process to clone the Repo
    pid = os.fork()
    if pid == 0:
        # Child Process
        os.chdir(data[0])
        url = "git clone " + data[1] + " . >> ../clone_log.txt 2>&1"
        os.system(url)
        os._exit(os.EX_OK)
        
    # Parent Process
    line = f.readline()
f.close()

# An infinite loop to wait for child processes till there are none left
while True:
    try:
        os.wait()
    except:
        break

# Recording the end time in the log file
os.system("echo -n End Time : >> clone_log.txt; date +\"%T\" >> clone_log.txt")