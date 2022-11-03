import openpyxl
from generaldata import data
def exceldata(sheetname):
    sheet = openpyxl.load_workbook(data('excel', 'path'))
    sheet2 = sheet[sheetname]
    datalist = []
    for i in sheet2:
        datalist.append([i[0].value,i[1].value])
    datalist.pop(0)
    return datalist
