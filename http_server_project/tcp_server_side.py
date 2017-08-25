import socket
import sys
import SocketServer
import threading
import time

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            cur_thread = threading,current_thread()
            response = "{}: {}".format(cur_thread.name, data)
            print data

class ThreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8888
    server = ThreadedTCPServer((HOST,PORT),ThreadedTCPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    while True:
        time.sleep(1)

    server.shutdown()
    server.server_close()


