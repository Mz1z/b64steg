# b64steg

base64 Steganography, support by python3.

支持python3的base64隐写库。

author: Mz1

email: mzi_mzi@163.com



## Installment

```bash
pip install b64steg
```



## Usage

```python
import b64steg

s = '''5rGJ55qH6YeN6Imy5oCd5YC+5Zu9LOW+oeWuh+WkmuW5tOaxguS4jeW+l+OAgk==
5p2o5a625pyJ5aWz5Yid6ZW/5oiQLOWFu+WcqOa3semXuuS6uuacquivhuOAgt==
5aSp55Sf5Li96LSo6Zq+6Ieq5byDLOS4gOacnemAieWcqOWQm+eOi+S+p+OAgn==
5Zue55y45LiA56yR55m+5aqa55SfLOWFreWuq+eyiem7m+aXoOminOiJsuOAgq==
5pil5a+S6LWQ5rW05Y2O5riF5rGgLOa4qeazieawtOa7kea0l+WHneiEguOAgj==
5L6N5YS/5om26LW35aiH5peg5YqbLOWni+aYr+aWsOaJv+aBqeazveaXtuOAgh==
'''

# decrypt example
# base64 strings split by '\n'
print(b64steg.decry(s))


# encrypt example
# type of argv is bytes
print(b64steg.encry('whoami'.encode()))


# you can also use your text to take place of 《长恨歌》
# or use other base64 table.

```

