# import subprocess
# lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# data = "your_data_here"
# data = bytes(data, 'utf-8')
# lpr.stdin.write(data)


import os, sys
from win32 import win32print
# p = win32print.GetDefaultPrinter()
p = win32print.OpenPrinter("PDFCreator")



job = win32print.StartDocPrinter(p, 1, ("data", None, "RAW"))
win32print.StartPagePrinter(p)
data = "your_data_here"
data = bytes(data, 'utf-8')
win32print.WritePrinter (p, data)
win32print.EndPagePrinter (p)
# if sys.version_info >= (3,):
#   raw_data = bytes ("This is a test", "utf-8")
# else:
#   raw_data = "This is a test"

# hPrinter = win32print.OpenPrinter (printer_name)
# try:
#   hJob = win32print.StartDocPrinter (hPrinter, 1, ("test of raw data", None, "RAW"))
#   try:
#     win32print.StartPagePrinter (hPrinter)
#     win32print.WritePrinter (hPrinter, raw_data)
#     win32print.EndPagePrinter (hPrinter)
#   finally:
#     win32print.EndDocPrinter (hPrinter)
# finally:
#   win32print.ClosePrinter (hPrinter)
