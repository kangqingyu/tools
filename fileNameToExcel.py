#-*-coding:utf-8-*-
__author__ = 'kqy'

import os
import sys
import os.path
import xlrd
import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')

def travel(rootdir, list):
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in  dirnames:
            list.append(dirname)

def insertToExcel(list):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    for i in range(len(list)):
        char = list[i]
        print char
        char = unicode(char, 'utf-8')
        sheet1.write(i, 0, char)
    f.save('/Users/kqy/Documents/manpao/t2018.xls')

def main():
    list = []
    rootdir = "/Users/kqy/Documents/manpao/mp3Learn/ximalaya"
    travel(rootdir, list)
    insertToExcel(list)

if __name__ == "__main__":
    main()
