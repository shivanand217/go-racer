import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\anand\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\anand\AppData\Local\Programs\Python\Python35\tcl\tk8.6'

executables = [cx_Freeze.Executable("go_racer.py")]

cx_Freeze.setup(
    name = "go racer",
    author = "shiv anand",
    options={"build_exe": {"packages":["pygame"],
                          "include_files":["car.png"]}},
    executables = executables 
    )
