# import subprocess
# lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# data = "your_data_here"
# data = bytes(data, 'utf-8')
# lpr.stdin.write(data)


import win32ui
import win32print
import win32con

# X from the left margin, Y from top margin
# both in pixels
X=50; Y=50
multi_line_string = """
     Ονομα μαγαζιου 
     Ονομα σερβιτορου
       Τραπεζι Χ   ωρα
προιον 1     
       σχολια
προιον 2    
       σχολια
       """
multi_line_string = multi_line_string.splitlines()
hDC = win32ui.CreateDC ()
hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
hDC.StartDoc ("Paraggelia")
hDC.StartPage ()
for line in multi_line_string:
     hDC.TextOut(X,Y,line)
     Y += 100
hDC.EndPage ()
hDC.EndDoc ()

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
