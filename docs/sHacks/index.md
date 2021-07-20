# sHacks shell hacks

# sh

```bash
$ cat > plain.txt
It is the plain text
^D
$ base64 plain.txt
$ cat plain.txt | base64
$ echo It is the plain text | base64
```

```bash
$ echo "{\"key\":\"secret\"}"
$ echo `cat|base64`
{"key":"secret"}
^D
$ 
```

```bash
$ ls -l -A
$ {ls,-l,-A}
```
```bash
$ ls *.txt
$ ls *.{txt,php}
$ rm *.{txt,js}
```

```bash
$ alias update_pkgm="sudo apt updata;sudo apt upgrade"
```

```bash
$ > new.txt
written
^D
$ >> new.txt
another line
^D
$ cat new.txt
written
another line
$
```

```bash
$ cat >> ~/.bashrc
gclone(){
	git clone https://github.com/Myname/$1
	cd $1
	git status
}
^D
$ source ~/bashrc
$ gclone myrepo
```

```bash
$ export var="hello"
$ echo "${var:1:2}"
el
$ echo "${var:2:3}"
llo
```

```bash
$ export var="hello"
$ echo "${#var}"
4
```

```bash
$ git commit -m "Initial commit"
$ git commit -m Initial\ commit
```

```bash
$ echo '
multi
line
echo
'
```

# loops
```bash
$ for i in `seq 1 10`;do echo $i;done
$ for i in {1..10};do echo $i;done
$ for ((i = 0;i < 10; i++));do echo $i;done
$ for i in $(cat test.txt);do echo $i|base64;done
```

```bash
$ cat > forloop.sh
for i in `ls`
do
	echo "`pwd`/$i"
done
^D
$ sh forloop.sh
$ cat forloop.sh | sh
```

```bash
$ cat | sh
for ((i=0; i<10 ;i++))
do
	echo $i
done
```

```bash
$ while read -r i;do
	echo $i
done < test.txt
```

```bash
$ cat > io.py
#!/bin/python
from sys import stdin,stdout
stdout.write(stdin.read())
^D
$ chmod -x io.py
$ ./io.py | base64
hello World
^D
```


# simple servers

```ruby
$ python -m http.server
$ python -m http.server 8080
```
```ruby
$ python2 -m  SimpleHTTPServer
$ python2 -m  SimpleHTTPServer 1245
```

```ruby
$ ruby -run -e httpd
$ ruby -run -e httpd . -p 4444
```

```ruby
$ php -S 0.0.0.0:8080
```

# comparition

```bash
[[ -z STRING ]]
[[ -n STRING ]]
[[ STRING == STRING ]]
[[ STRING != STRING ]]
[[ NUM -eq NUM ]]
[[ NUM -ne NUM ]]
[[ NUM -lt NUM ]]
[[ NUM -le NUM ]]
[[ NUM -gt NUM ]]
[[ NUM -ge NUM ]]
[[ STRING =~ STRING ]]

(( NUM < NUM ))

[[ ! EXPR ]]
[[ X && Y ]]
[[ X || Y ]]

[[ -e FILE ]]  
[[ -r FILE ]]  
[[ -h FILE ]]  
[[ -d FILE ]]  
[[ -w FILE ]]  
[[ -s FILE ]]
[[ -f FILE ]]  
[[ -x FILE ]]  
[[ FILE1 -nt FILE2 ]]
[[ FILE1 -ot FILE2 ]]
[[ FILE1 -ef FILE2 ]]
```
