import u
import pandas as pd

def getInitP(file_name,n):
    book = pd.ExcelFile(file_name)
    dF = book.parse('01')
    series = u.row2list(dF)
    m = len(dF)
    P = [ [0]*n for i in range(m) ]

    for j in range(n):
        for i, xi in enumerate(series):
            P[i][j] = xi
    return P
