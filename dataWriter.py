import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def excel_writer(table1):
    NewFile = table1.to_excel(Output.xlsx)
