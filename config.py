import os
import shutil
user = os.getlogin()
running = os.path.dirname(os.path.realpath(__file__))
destination = os.path.join("C:\\", "Users", user, "Documents")
directory_py = os.path.join(destination, "config.py")
directory_exe = os.path.join(destination, "PyPy3Launcher.exe")
try:
    if not os.path.exists(directory_py):
        shutil.copy2("config.py", destination)
    if not os.path.exists(directory_exe):
        shutil.copy2("PyPy3Launcher.exe", destination)
except FileNotFoundError:
	pass
if running != destination:
    try:
        os.startfile(directory_py)
        os.remove("config.py")
    except FileNotFoundError:
        pass
try:
    from context_menu import menus
except ImportError:
    os.system("python -m pip install context-menu")
import winreg
def foo(filenames, parameter):
    filenames = str(filenames)
    file = filenames.replace("[", "")
    file = file.replace("]", "")
    file = file.replace("\"", "")
    file = file.replace("'", "")
    file = file.replace("\\\\", "\\")
    file = f"\"{file}\""
    os.system(f"pypy3 {file}")
fc = menus.FastCommand("Run with PyPy", type="FILES", python=foo)
# fc = menus.FastCommand("Run with PyPy", type=".py", command='''"C:\Users\HKB\AppData\Local\Programs\Python\Python39\python.exe" -c "import sys; sys.path.insert(0, "C:/Users/HKB/Documents"); import config; config.foo([' '.join(sys.argv[1:]) ],'')" "%1""''')
fc.compile()
if running != destination:
	os.system(f'%SystemRoot%\\System32\\reg.exe ADD "HKEY_CURRENT_USER\Software\\Classes\\*\\shell\\Run with PyPy" /f /t REG_SZ /v "Icon" /d "{directory_exe}"')