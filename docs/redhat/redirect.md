# redirection

```ruby
[attacker]
 |
 |
<8080>
 |
 |
[redirector]
 |
 |
<80>
 |
 |
[victom]
```

**WARNING: Make sure your FW is configured perfectly. when you are using publically. and https too.**

## socat

**tcp-ipv4:**

```ruby
$ socat tcp4-listen:80 tcp:example.com:8080
```

**tcp-multi-con-once:**

```ruby
$ socat tcp4-listen:80,fork tcp:example.com:8080
```

**tcp-multi-con:**

```ruby
$ socat tcp4-listen:80,reuseaddr,fork tcp:example.com:8080
```

---

**tcp-ipv6:**

```ruby
$ socat tcp6-listen:80 tcp:example.com:8080
```

**tcp-multi-con-once:**

```ruby
$ socat tcp6-listen:80,fork tcp:example.com:8080
```

**tcp-multi-con:**

```ruby
$ socat tcp6-listen:80,reuseaddr,fork tcp:example.com:8080
```

---

**udp-ipv4:**

```ruby
$ socat udp4-listen:80 udp:example.com:8080
```

**udp-multi-con-once:**

```ruby
$ socat udp4-listen:80,fork udp:example.com:8080
```

**udp-multi-con:**

```ruby
$ socat udp4-listen:80,reuseaddr,fork udp:example.com:8080
```

---

**udp-ipv6:**

```ruby
$ socat udp6-listen:80 udp:example.com:8080
```

**udp-multi-con-once:**

```ruby
$ socat udp6-listen:80,fork udp:example.com:8080
```

**udp-multi-con:**

```ruby
$ socat udp6-listen:80,reuseaddr,fork udp:example.com:8080
```

---

## ruby

to be continue...
