# Import Module
from win32com import client
import openpyxl, os
import getpass

username = getpass.getuser()
print(username)

# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")
excel_path = 'C:/Users/%s/Documents/Important/Loan Balance History.xlsx' % username

wb = openpyxl.load_workbook(excel_path)
ws = wb.active

ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.page_setup.fitToHeight = False

wb.save(excel_path)
wb.close()
wb = None

pdf_path = 'C:/Users/%s/Documents/Important/Loan Balance History.pdf' % username

# Read Excel File
sheets = excel.Workbooks.Open(excel_path)

# Auto-fit column in active sheet
work_sheets = sheets.Worksheets[0]

# Convert into PDF File
work_sheets.ExportAsFixedFormat(0, pdf_path)
sheets.Close(False)
print("Completed")
