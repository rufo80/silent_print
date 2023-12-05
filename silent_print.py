import win32print
import win32api

class Print_silent():
    def __init__(self, file_path, copies):
        self.file_path = file_path
        printer_name = win32print.GetDefaultPrinter()
        data = open(file_path, 'rb').read()

        for n in range(copies):
            try:
                hprinter = win32print.OpenPrinter(printer_name)
                hjob = win32print.StartDocPrinter(hprinter, 1, (file_to_print, None, "RAW"))
                try:
                    win32print.StartPagePrinter(hprinter)
                    win32print.WritePrinter(hprinter, data)
                    win32print.EndPagePrinter(hprinter)
                finally:
                    win32print.EndDocPrinter(hprinter)
            finally:
                win32print.ClosePrinter(hprinter)


file_to_print = 'My_FIle.pdf'
print_silent(file_to_print)
