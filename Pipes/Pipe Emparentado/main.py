from multiprocessing import Process, Pipe



def process1(pipe):
    print("Process 1: ")
    print("Send Process 1......")
    pipe.send([10.5, False, "string Python"])
    print("End Process 1")


def process2(pipe):
    print("Process 2: ")
    print("Receiver Process 2......")
    print("package : ", pipe.recv())
    print("End Process 2")


def main():
    server_pipe, client_pipe = Pipe()
    p1 = Process(target=process1, args=(client_pipe,))
    p2 = Process(target=process2, args=(server_pipe,))

    p2.start()
    p1.start()


if __name__ == "__main__":
    main()

# Out[]:

# Process 2: 
# Receiver Process 2......
# Process 1: 
# Send Process 1......
# End Process 1
# package :  [10.5, False, 'string Python']
# End Process 2
