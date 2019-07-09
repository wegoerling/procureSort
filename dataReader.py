import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Sorter Method
def excel_sorter( file1, sheet1, name1):
    df = pd.read_excel(file1, sheet_name=sheet1)

    print('Before:')
    for i in range(9):
        print(df['Unique ID'][i] + ' / ' +  df['IT Requestor Name'][i] + ' / ' + df['Purchase Description'][i])
    print(' ')

    finaltable = df[df['IT Requestor Name'] == name1]

    return finaltable

# implementation
print('Showing the first ten entries in the sorted and unsorted tables')
ftable = excel_sorter('Extract 1.xlsx', 'Extract 1', 'Brent, Tipton')
print('After: ')
u=0
for i,u in zip(ftable.index,range(9)):
    print(ftable['Unique ID'][i] + ' / ' +  ftable['IT Requestor Name'][i] + ' / ' + ftable['Purchase Description'][i])