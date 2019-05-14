
import os

path = "/tmp/mkfifo.dat"

fifo = open(path, "r")

for line in fifo:
    print("Received: ", line)


fifo.close()
os.remove(path)

# Out[]:

# Received:  Message from the sender!
# Received:  Hello World