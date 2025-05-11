#!/bin/python3

import urllib.request
from json import loads
import argparse


URL="https://raw.githubusercontent.com/Madhava-mng/my-cyber-diary/refs/heads/master/docs/cheetsheet/"

def find(vuln="xss", type_="obj"):

    try:
        response = urllib.request.urlopen(URL+vuln+".json")
        data = response.read().decode("utf-8")
    except:
        print("unable to get data for:", vuln)
        return

    if data.startswith("{"):

        d = loads(data)
        for k in d.keys():
            if type_ != "list":
                print("\033[1m"+k, ":\033[0m\033[32m")
                num = 1
            if type(d[k]) == list:
                for v in d[k]:
                    if v.rfind("\n") != -1:
                        v = v.encode()
                    if type_ != "list":
                        print((f"{num}.  " + v + " "))
                        num += 1
                    else:
                        print(v)
            else:
                print(d[k])
            if type_ != "list":
                print("\033[0m\033[2m-\033[0m"*20)



parser = argparse.ArgumentParser(description="payload search")

parser.add_argument("search", help="Search: eg: xss")
parser.add_argument("-l", "--list",action="store_true" ,help="Shown in list format")

args = parser.parse_args()



#print(args)
if args.list:
    type_="list"
else:
    type_="obj"
find(args.search, type_)
