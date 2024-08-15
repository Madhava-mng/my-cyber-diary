#!/bin/python3

from socket import socket
from re import findall

class Listerner:

    def __init__(self):
        self.host="localhost"
        self.port=8000
        self.size=1024
        self.maxAccept=50
        self.ignore = ['favicon.ico']
        self.con_count = 0
        self.accepted_count = 0
        self.accepted_file = "accepted.txt"
        self.ignored_file = "ignored.txt"
        self.mode = "a"

    def start(self):
        listerner = socket()
        listerner.bind((self.host, self.port, ))
        self.accepted_file = open(self.accepted_file, self.mode)
        self.ignored_file = open(self.ignored_file, self.mode)
        while(self.maxAccept):
            try:
                listerner.listen(1);
                con,addr = listerner.accept()
                try:
                    self.con_count = self.con_count + 1
                    data = findall(r"GET /(.*?) HTTP", con.recv(self.size).split(b"\n")[0].decode())[0]

                    if(data):
                        if (data not in self.ignore):
                            self.accepted_file.write(data + "\n")
                            self.accepted_count = self.accepted_count + 1
                            print(data, "[ TotalConnection:",self.con_count, "AcceptedConnection:", self.accepted_count , "]")
                        else:
                            self.ignored_file.write(data + "\n")
                        con.send(b"{\"Added\":\""+data.encode()+b"\"}\n\n\n")
                    else:
                        con.close()
                finally:
                    con.close()
                    if (data not in self.ignore):
                        self.maxAccept = self.maxAccept - 1
            except KeyboardInterrupt:
                print("[!] Interrupt")
                self.accepted_file.close()
                self.ignored_file.close()
                return


lnr = Listerner()
lnr.maxAccept = 10
lnr.start()
