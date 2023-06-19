>>> s
{False, True, 2}
>>> s.remove('Ravi')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Ravi'
>>> 
>>> s.discard('Ravi')
>>> s
{False, True, 2}
>>> 
