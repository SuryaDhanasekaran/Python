Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #COMPOSITION
>>> x = math.sin(degrees / 360.0 * 2 * math.pi)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x = math.sin(degrees / 360.0 * 2 * math.pi)
NameError: name 'math' is not defined
>>> import math
>>> x = math.sin(degrees / 360.0 * 2 math.pi)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> # left side of the assignment has to be variable name.Any other expressions on the left side is a syntax error
>>> minutes = hours  * 60
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    minutes = hours  * 60
NameError: name 'hours' is not defined
>>> hours= 10
>>> hours *  60 = minutes
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> #SYNTAX ERROR CANT ASSIGN TO OPERATOR
