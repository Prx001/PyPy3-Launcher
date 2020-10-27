# PyPy3 Launcher
 A launcher for python files with PyPy implementation
 Before using this launcher you have to have PyPy3 installed and added it's directory(PyPy directory) to the path.
 [Download and install PyPy3](https://www.pypy.org/download.html)
# What is PyPy?
 PyPy is one of the most famous Python implementations which is mainly used for it's incredible speed.
 PyPy is between 4 to 50 times faster than the Python default implementation depends on your tasks.
 It doesn't change your code, it doesn't have any other syntax, it just executes your program in another way.
 We will talk about it more.
# What are Python implementations?
 An "implementation" of Python should be taken to mean a program or environment which provides support for the execution of programs written in the Python language,
 as represented by the CPython reference implementation.
 [Learn more](https://wiki.python.org/moin/PythonImplementations)
# What's my implementation?
 The default Python implementation is 'CPython'. If you downloaded Python from [python.org](https://python.org) your implementation is CPython.
 You can also check your implementation whenever you want using the scripts below:
 ```py
 import platform
 print(platform.python_implementation())
 ```
 This simple program prints the implementation which you're using.
# Why to change my implementation?
 Different Python implementations are for different tasks which usually you're not able to do it in default one (CPython).
 There are lots of implementations for Python such as PyPy, IronPython, Jython and ... (Those are the most famous ones).
 But the one we're talking about is PyPy.
# How much is PyPy faster than CPython? Is it worth using?
 On the average, PyPy speeds up Python by about 7.6 times, with some tasks accelerated 50 times or more!
 The CPython interpreter simply doesn't perform the same kinds of optimizations as PyPy, and probably never will, since that is not one of its design goals.
 And simply there won't be any changes in your code, you just code Python, and Run it with PyPy instead of CPyhton!
# Why is PyPy so fast?
 PyPy often runs faster than CPython because PyPy is a just-in-time compiler which known as JIT compiler, while CPython is an interpreter.
 Since interpreters are usually easier to write than compilers, but run slower, this technique can make it easier to produce efficient implementations of programming languages.
# Where to download PyPy?
 You can download PyPy [here](https://www.pypy.org/download.html). It doesn't need an extra installation just unpack it and move the folder somewhere;
 such as ```C:\Users\username\AppData\Local\Programs\Python``` which is the directory in which usually Python installed.
 Don't forget to install the libraries, modules and packages that you need or already installed on CPython.
# How to install packages as ```pip install``` does it for CPython?
 since pip itself is written in Python, and ```pip install``` is actually ```python -m pip install```, you can use
 ```pypy3``` to do so. After you added PyPy to path, you can use the commands below:
 ```pypy3 ensurepip```
 ```pypy3 -m pip install <package>```
# How to use PyPy?
 After you setted up PyPy, you can find interpreter setting in your IDE and change it PyPy. (Your IDE may ask for the directory of the interpretet, give the directory to
 pypy3.exe, e.g ```C:\Users\username\AppData\Local\Programs\Python\pypy\pypy3.exe```)
 Then run your code and it will use PyPy interpreter!
# Where to use PyPy3 Launcher? What does it do?
 This program, is just like the Python default launcher which installs with Python and gives you the ability to run .py files with a simple double click;
 except that the default Python launcher, runs your program on CPython, However PyPy Launcher runs them on PyPy implementation without using your IDE and setting the interpreter!
 You can also set PyPy Lancher as default program to open your .py files and make it as simple as double clicks!
# Also see
 [PyPy official website](https://www.pypy.org)
 [PyPy documentation](https://doc.pypy.org/en/latest)
 [PyPy frequently asked questions](https://doc.pypy.org/en/latest/faq.html)
 [PyPy at Wikipedia](https://en.wikipedia.org/wiki/PyPy)
 [PyPy at PyCon](https://www.youtube.com/watch?v=1n9KMqssn54)
 [PyPy at Real Python](https://www.youtube.com/watch?v=Ri8sU5DphEE)
