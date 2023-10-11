Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #functions
>>> #FUNCTION CALLS
>>> TYPE(42)'
SyntaxError: unterminated string literal (detected at line 1)
>>> TYPE(42)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    TYPE(42)
NameError: name 'TYPE' is not defined
>>> type(42)
<class 'int'>
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> float('32')
32.0
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> import math
>>> +
SyntaxError: invalid syntax
>>> #module object - math
>>> math
<module 'math' (built-in)>
