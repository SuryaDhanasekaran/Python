Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '2' - 1
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    '2' - 1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 'eggs'/'eggs'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'eggs'/'eggs'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 'third'*'a charm'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    'third'*'a charm'
TypeError: can't multiply sequence by non-int of type 'str'
>>> first = 'throat'
>>> second = 'wabler'
>>> first + second
'throatwabler'
>>> 'Spam'*3
'SpamSpamSpam'
>>> 'Spam'*100
'SpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpamSpam'
>>> n = 42
>>> 42 = n
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 42 == n
True
>>> 33 == n
False
>>> x = y = 1
>>> print(x + y)
2
>>> x + y;
2
