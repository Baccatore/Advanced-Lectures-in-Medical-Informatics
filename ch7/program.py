import pandas as pd
import matplotlib.pyplot as plt
import pickle

import Q0705 as Q
import MyModule0701 as m1
import MyModule0702 as m2
import MyModule0703 as m3
import MyModule0708 as m8

if __name__== '__main__':
    book  = pd.ExcelFile("nirs.xlsx")
    dF = book.parse("01")
    s1 = dF.CH1

    print('[--Today\'s Quiz!]')
    print(Q.transMoveAve(s1))
    plt.scatter(dF.Time,Q.transMoveAve(s1))
    plt.scatter(dF.Time,dF.CH1)
    plt.savefig('test.png')


    print('\nTask 1')
    dF = dF.iloc[1500:2500,0:25]
    #print(dF)
    a = m1.row2list(dF.iloc[:,1:25])
    df = pd.DataFrame(columns=[])
    for si in a:
        m3.addDF(df,si)
    #print(df)

    print('\nTask 2')
    print('Type int from 1 to 24 as CHN')
    #chN = int(input())
    chN = 10
    for ai in a:
        print(m8.getCorr(a[chN-1],ai))

    print('\nTask 3')
    with open('output','wb') as of:
        pickle.dump(df,of)
    
    print('\nTask4')
    with open('output','rb') as input_file:
        df_loaded = pickle.load(input_file)
    print(df_loaded)
    for i, ai in enumerate(a):
        plt.subplot(6,4,i+1)
        plt.plot(dF.Time,ai)
    plt.show()
    plt.clf()

    print('\nTask5')
    for i, ai in enumerate(a):
        plt.subplot(6,4,i+1)
        plt.plot(dF.Time,Q.transMoveAve(ai))
    plt.show()
    plt.clf()

    print('\nTaks6')
    df_shifted= pd.DataFrame(columns=[])
    for ai in a:
        df_shifted[ai.name] = Q.transMoveAve(ai) 
    with open('df_shifted','wb') as shifted_file:
        pickle.dump(df_shifted,shifted_file)

    print('\nTaks7')
    plt.figure(figsize=(16,18))
    for i, ai in enumerate(a):
        amplitude = ai.max() - ai.min()
        df_shifted[ai.name] = (ai - ai.min()) / amplitude
        plt.subplot(6,4,i+1)
        plt.title(ai.name)
        plt.plot(dF.Time,(ai-ai.min())/amplitude)
    plt.subplots_adjust(wspace=0.3, hspace=0.4)
    plt.savefig('task7.png')
    plt.clf()
    with open('df_standarized','wb') as standarized_file:
        pickle.dump(df_shifted,standarized_file)

    print('\nTaks8')
    print(df_shifted)


