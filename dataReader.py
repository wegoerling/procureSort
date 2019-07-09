import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# Sorter excel table
def excel_sorter(file1, sheet1, name1):
    df = pd.read_excel(file1, sheet_name=sheet1)

    print('Before (Unsorted Table):')
    for i in range(9):
        print(df['Unique ID'][i] + ' / ' + df['IT Requestor Name'][i] + ' / ' + df['Purchase Description'][i])
    print(' ')

    ftable = df[df['IT Requestor Name'] == name1]

    return ftable


# print excel table
def excel_auto_printer():
    print('Showing the first ten entries in the sorted and unsorted tables')

    ftable = excel_sorter('Extract 1.xlsx', 'Extract 1', 'Brent, Tipton')
    for i, u in zip(ftable.index, range(9)):
        print('After: ')
        print(
            ftable['Unique ID'][i] + ' / ' + ftable['IT Requestor Name'][i] + ' / ' + ftable['Purchase Description'][i])
        print(' ')


# print excel table
def excel_printer(file2, sheet2, name2):
    ftable = excel_sorter(file2, sheet2, name2)
    for i, u in zip(ftable.index, range(9)):
        print('After: ')
        print(
            ftable['Unique ID'][i] + ' / ' + ftable['IT Requestor Name'][i] + ' / ' + ftable['Purchase Description'][i])
        print(' ')


# print excel table
def excel_select_printer():
    sheet = input()
    name = input()

    import Tkinter, tkFileDialog

    root = Tkinter.Tk()
    root.withdraw()

    file_path = tkFileDialog.askopenfilename()
    sheet = input()
    name = input()

    ftable = excel_sorter(file_path, sheet, name)
    for i, u in zip(ftable.index, range(9)):
        print('After: ')
        print(
            ftable['Unique ID'][i] + ' / ' + ftable['IT Requestor Name'][i] + ' / ' + ftable['Purchase Description'][i])
        print(' ')


