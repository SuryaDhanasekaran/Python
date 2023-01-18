Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+1
2
print("Hello World")
Hello World
40 + 2
42
43 - 1
42
6 * 7
42
84/2
42.0
6**2 + 6
42
6^2
4
type(2)
<class 'int'>
type(42.0)
<class 'float'>
type('Hello,World!')
<class 'str'>
type('2)
     
SyntaxError: unterminated string literal (detected at line 1)
type('2')
     
<class 'str'>
type('42.0')
     
<class 'str'>
1,000,000
     
(1, 0, 0)
print('Hello world
      
SyntaxError: unterminated string literal (detected at line 1)
print('hello world')
...       
hello world
>>> print 'hello world'
...       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(hello world)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('hello world)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> -2+4
...       
2
>>> print(+2)
...       
2
>>> +2
...       
2
>>> 2++2
...       
4
>>> 2+++2
...       
4
>>> 02+04
...       
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 2 4
...       
SyntaxError: invalid syntax
>>> 42*60+42
...       
2562
>>> 10/1.61
...       
6.211180124223602
>>> 6.21/2562
...       
0.002423887587822014
