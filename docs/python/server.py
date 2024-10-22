import socket
from sys import exc_info
from random import randint

blacklist:list = []
ip_info:dict = {}
UNBLOCK_PIN_PATH = "recovery.txt"
files_and_maps:dict = {
        "*":"index.html",
        "index.html": "index.html"
        }
IGNORE = [
        "favicon.ico"
        ]
REC_PIN = 0
DEFAULT_TEMPLAE = {
        "addr": "",
        "connection_count": 1,
        "non_suspicious_count": 3,
        "recovery_attumpt": 0
        }
HEADER = b'''
HTTP/1.1 200 OK
Content-Type: text/html

'''
HEADER_REC = f'''
HTTP/1.1 200 OK
Content-Type: text/html

Good to go :)<br>
your are unblocked.
<a href="/{files_and_maps["*"]}">Default page</a>


'''.encode()
HEADER_FAILED = b'''
HTTP/1.1 400 Bad Request
Content-Type: text/html

You are blocked ! 
Have a good day :)


'''
HEADER_REDIRECT = f"""
HTTP/1.1 303 Moved Permanently
perf: 7402827104
location: /{files_and_maps["*"]}

""".encode()

def gen_rec():
    global REC_PIN
    REC_PIN = randint(10000, 99999)
    f = open(UNBLOCK_PIN_PATH, 'w')
    f.write(f"{REC_PIN}")
    f.close()
    print(f"[INFO] Current recovery code is {REC_PIN}\n[INFO] Recovery code is also available in '{UNBLOCK_PIN_PATH}' file.")


def main(port = 4444, host = '0.0.0.0'):
    gen_rec()
    s = socket.socket()
    s.bind((host, port))
    s.listen()
    print(f"[INFO] Server listerning on {host}:{port}")
    while(True):
        try:
            file_maped = files_and_maps["*"]
            con, addr = s.accept()
            data = con.recv(1024*10)
            path = data.split(b" ")[1][1:].decode()
            #print(path,data)
            if( path in IGNORE):
                con.close()
                continue
            if(path.isdigit() and addr[0] in ip_info.keys()):
                if(ip_info[addr[0]]['non_suspicious_count'] <= 0 and ip_info[addr[0]]['recovery_attumpt'] <= 3):
                    if(path == str(REC_PIN)):
                        ip_info[addr[0]]['non_suspicious_count'] = 3
                        ip_info[addr[0]]['recovery_attumpt'] = 0
                        con.send(HEADER_REC)
                        con.close()
                        print(f"[RECV] Ip recovered with code '{REC_PIN}'",ip_info[addr[0]])
                        gen_rec()
                        continue
                    else:
                        ip_info[addr[0]]['recovery_attumpt'] += 1

            if(path):
                #print(f"[CONN] {addr}, {REC_PIN}")
                if(addr[0] not in ip_info.keys()):
                    ip_info[addr[0]] = DEFAULT_TEMPLAE
                    ip_info[addr[0]]['addr'] = addr[0]
                ip_info[addr[0]]["connection_count"] += 1
                print(f"[INFO] /{path} Connection from",ip_info[addr[0]])
                if(path not in files_and_maps.keys()):
                    ip_info[addr[0]]['non_suspicious_count'] -= 1
                    print(f"[WARN] /{path} Trying access",ip_info[addr[0]])
                    if(ip_info[addr[0]]['non_suspicious_count'] == -1):
                        print(f"[WARN] {addr[0]} is consider as suspect.")
                    con.send(HEADER_REDIRECT)
                    con.close()
                    continue
                if(ip_info[addr[0]]['non_suspicious_count'] < 0):
                    con.send(HEADER_FAILED)
                    con.close()
                    continue

                file_reg = open(files_and_maps[file_maped], 'rb')
                con.send(HEADER + file_reg.read())
                file_reg.close()
                con.close()
        except KeyboardInterrupt:
           print("[INTERRUPT]", exc_info())
           break
        except:
           print("[ERROR]", exc_info())

main()






