import socket
import sys
import time
import threading

if __name__ == "__main__":

        #thread = threading.Thread(target=client,args=['127.0.0.1',8888,'wo hoa',])
        #thread.daemon = True
        #thread.start()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 8888))
        while True:
                sock.sendall("ni hao")
                time.sleep(1)

        #while True:
                #time.sleep(1)