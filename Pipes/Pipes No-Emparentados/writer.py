import os

path = "/tmp/mkfifo.dat"

os.mkfifo(path)

fifo = open(path, "w")
fifo.write("Message from the sender!\nHello World")

fifo.close()