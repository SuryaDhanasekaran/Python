Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/HP/OneDrive/Desktop/Programming/PYTHON/Learning Python/12_Adding_New_Functions.py
<function print_lyrics at 0x000001790F733F40>
<class 'function'>
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print("I sleep all night and I work all day.")
... 
>>> print(print_lyrics)
<function print_lyrics at 0x000001790F73C0D0>
>>> type(print_lyrics)
<class 'function'>
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def repeat_lyrics()
SyntaxError: expected ':'
>>> def repeat_lyrics():
...     print_lyrics()
...     print_lyrics()
... 
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
