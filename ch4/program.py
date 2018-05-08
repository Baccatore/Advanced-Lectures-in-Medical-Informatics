import Q0401
import Q0402
import pandas as pd

import MyModule0401
import MyModule0402
import MyModule0403
import MyModule0404

if __name__ == "__main__":
    print("[--Today's Quiz!--]")
    xmin, ymin = Q0401.getMax(2, 3, -1)
    print(xmin, ymin)
    nx, ny = Q0402.getNormalVec(0,0)
    print(nx, ny, "\n")
    
    print("[--MyModule0401--]")
    book = pd.ExcelFile("data2.xlsx")
    sheet1=book.parse("TomoData")
    data1=sheet1.AverageTemp
    print("sheet")
    print(sheet1[:])
    print("data1")
    print(data1[1:9+1])
    MyModule0401.mySaveExcel(sheet1[:],"Test_File.xlsx", "Test_Sheet")
    print("Saved exel file\n")
    
    print("[--MyModule0402--]")
    s1 = MyModule0402.extract(data1, 3, 10)
    print(s1)
    print("\n")

    print("[--MyModule0403--]")
    df = MyModule0403.myConcat(sheet1.AverageTemp, sheet1.YearDate)
    print(df)
    print("\n")

    print("[--MyModule0404--]")
    s2 = MyModule0404.MyMA(data1,5)
    print(s2)
    print("\n")
