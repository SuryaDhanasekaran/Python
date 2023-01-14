Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> start = (6*60+52)*60
... >>> easy = (8*60+15)*2
... >>> fast = (7*60+12)*3
... >>> finish_hour = (start + easy + fast)/(60*60.0)
... >>> finish_floored = (start + easy + fast)//(60*60)  #int() function can also be used to get integer value, but it hasn't taught yet.
... >>> finish_minute  = (finish_hour - finish_floored)*60
... >>> print ('Finish time was %d:%d' % (finish_hour,finish_minute))
... Finish time was 7:30
