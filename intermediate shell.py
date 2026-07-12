Python 3.14.0 (v3.14.0:ebf955df7a8, Oct  7 2025, 08:20:14) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
Traceback (most recent call last):
  File "/Users/mostafaanwar/Desktop/Data science course /intermediate p1.py", line 7, in <module>
    new_names.append.upper(names)
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
Traceback (most recent call last):
  File "/Users/mostafaanwar/Desktop/Data science course /intermediate p1.py", line 7, in <module>
    new_names.append.upper(names)
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
Traceback (most recent call last):
  File "/Users/mostafaanwar/Desktop/Data science course /intermediate p1.py", line 7, in <module>
    new_names.append.upper(Names)
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['MAHMOUD', 'FARIDA', 'ALI', 'HASSAN', 'MOHAMED', 'KHALED', 'TAHA']

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
<map object at 0x10aa92540>

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['MAHMOUD', 'FARIDA', 'ALI', 'HASSAN', 'MOHAMED', 'KHALED', 'TAHA']

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
[<built-in method upper of str object at 0x1067a8390>, <built-in method upper of str object at 0x1067a8360>, <built-in method upper of str object at 0x1067a83c0>, <built-in method upper of str object at 0x1019e5170>, <built-in method upper of str object at 0x106822fa0>, <built-in method upper of str object at 0x106822fd0>, <built-in method upper of str object at 0x106823000>]

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
[<built-in method upper of str object at 0x1087bad30>, <built-in method upper of str object at 0x108acad30>, <built-in method upper of str object at 0x108ac8150>, <built-in method upper of str object at 0x108ac8120>, <built-in method upper of str object at 0x108ac8180>, <built-in method upper of str object at 0x108acb120>, <built-in method upper of str object at 0x108b42d30>]

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['MAHMOUD', 'FARIDA', 'ALI', 'HASSAN', 'MOHAMED', 'KHALED', 'TAHA']

================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
Traceback (most recent call last):
  File "/Users/mostafaanwar/Desktop/Data science course /intermediate p1.py", line 46, in <module>
    new_names = [ n for n in Nmaes if 'a' in n ]
NameError: name 'Nmaes' is not defined. Did you mean: 'Names'?
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
[]
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
[None, None, None, None, None, None, 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['farida', 'hassan', 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['farida', 'hassan', 'taha']
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
Traceback (most recent call last):
  File "/Users/mostafaanwar/Desktop/Data science course /intermediate p1.py", line 103, in <module>
    print(new_names)
NameError: name 'new_names' is not defined. Did you mean: 'new_nams'?
>>> 
================= RESTART: /Users/mostafaanwar/Desktop/Data science course /intermediate p1.py =================
['farida', 'hassan', 'taha']
>>> Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
>>> a,*b = Names
>>> a
'mahmoud'
>>> b
['farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']
>>> a,*_,b = Names
>>> a
'mahmoud'
>>> b
'taha'
>>> a,b,*_ = Names
>>> a
'mahmoud'
>>> b
'farida'
