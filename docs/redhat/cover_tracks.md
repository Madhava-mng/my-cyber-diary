# covering tracks

Covering tracks is most import for redhat.


**overwrite files:**
```bash
cat /dev/null > /var/log/auth.log
cat /dev/null > ~/.bash_history

# If It was used by you
cat /dev/null > ~/.python_history
cat /dev/null > ~/.sqlite_history
cat /dev/null > ~/.irb_history
```

---

**clearing history:**

```bash
history -c
```

---

**changing variables:**

```bash
export HISTFILESIZE=0
export HISTSIZE=0
```
---

**Unset the historyfile variable:**

```bash
unset HISTFILE
```
---

**permenently clear .bash_history file:**

```bash
ln -sf /dev/null ~/.bash_history
```
---

**kill the current session:**

```bash
kill -9 $$
```
---



Thanks!
