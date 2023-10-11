Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#MATH FUNCTIONS'
ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
decibels = 10 * math.log10(ratio)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    decibels = 10 * math.log10(ratio)
NameError: name 'math' is not defined
radians = 0.7
height = math.sin(radians)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    height = math.sin(radians)
NameError: name 'math' is not defined
>>> import math
>>> KeyboardInterrupt
>>> math
<module 'math' (built-in)>
>>> ratio = siganl_power / noise_powerr
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ratio = siganl_power / noise_powerr
NameError: name 'siganl_power' is not defined
>>> radians = 0.7
>>> height = math.sin(radius)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    height = math.sin(radius)
NameError: name 'radius' is not defined. Did you mean: 'radians'?
>>> height = mat.sin(radians)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    height = mat.sin(radians)
NameError: name 'mat' is not defined. Did you mean: 'math'?
>>> height = math.sin(radians)
>>> radians = 0.7
>>> print(height)
0.644217687237691
>>> degrees = 45
>>> radians = degrees /180.0 * math.pi
>>> math.sin(radius)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    math.sin(radius)
NameError: name 'radius' is not defined. Did you mean: 'radians'?
>>> math.sine(radians)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    math.sine(radians)
AttributeError: module 'math' has no attribute 'sine'. Did you mean: 'sin'?
>>> math.sin(radians)
0.7071067811865476
>>> math.sqrt(2)/2.0
0.7071067811865476;
