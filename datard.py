import os
import datetime
import json
import os
import xlrd
first=8
lastend=6
def dump_cell(sheet, rowx, colx):
    c = sheet.cell(rowx, colx)
    xf = sheet.book.xf_list[c.xf_index]
    fmt_obj = sheet.book.format_map[xf.format_key]
#    print rowx, colx, repr(c.value), c.ctype, \\
#        fmt_obj.type, fmt_obj.format_key, fmt_obj.format_str
    
def getKey(row,icol):
    print(row[icol])
    print(row[icol].value)
    return row[icol].value
def getKeyfloat(row,icol):
    print(row[icol])
    print(row[icol].value)
    print(row[icol].ctype)
    if row[icol].ctype==2:
        print(float(row[icol].value))
        return float(row[icol].value)
    else:
        return 0
def getnrows(filename):
    
    data = xlrd.open_workbook(filename)
    datav=[]
    table = data.sheets()[0] 
    nrows = table.nrows
    for i in range(first, table.nrows-lastend):
        print(table.row(i))
        getKey(table.row(i),1)
        getKeyfloat(table.row(i),4)
        datav.append((getKey(table.row(i),1),getKeyfloat(table.row(i),4)))
    return datav
import os.path
def filemonitor(dir_name):
    file_path=os.path.join(dir_name,"应收总账.xlsx")
    
    return os.path.exists(file_path)
    