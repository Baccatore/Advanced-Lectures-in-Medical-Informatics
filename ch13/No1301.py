import pandas as pd
import matplotlib.pyplot as plt
import MyModule as m

if __name__ == '__main__':
    book = pd.ExcelFile('../nirs.xlsx')
    dF = book.parse('01')
    series = m.row2list(dF)
    data = []
    data_size = 1000
    for record in series:
        data.append(m.extractRow(record,1500,data_size))

    brain_wave=[]
    time_step = .1
    fs = 1/time_step
    for ch in data:
        brain_wave.append(m.getFAlff(ch,fs))
    
    lowf=0.01; highf=0.1
    data = [m.getTimeSBand(ch,fs,lowf,highf,order=3) for ch in data]

    plt.figure(figsize=(16,18))
    t_vec = [i*time_step for i in range(data_size)]
    for i, ch in enumerate(data):
        if i == 0:
            continue
        plt.subplot(6,4,i)
        plt.title('CH{0}'.format(i))
        plt.plot(t_vec,ch)
    plt.subplots_adjust(wspace=0.3,hspace=0.4)
    plt.show()

