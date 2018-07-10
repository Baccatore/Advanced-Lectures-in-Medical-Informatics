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

    #plt.figure(figsize=(16,18))
    #t_vec = [i*time_step for i in range(data_size)]
    #for i, ch in enumerate(data):
    #    if i == 0:
    #        continue
    #    plt.subplot(6,4,i)
    #    plt.title('CH{0}'.format(i))
    #    plt.plot(t_vec,ch)
    #plt.subplots_adjust(wspace=0.3,hspace=0.4)
    #plt.savefig('lecture13.png')

    plt.clf()
    cor2ch1  = [m.myCorr(signal,data[1])  for signal in data]
    cor2ch16 = [m.myCorr(signal,data[16]) for signal in data]
    plt.scatter(cor2ch1,cor2ch16)

    plt.plot([-1.2,1.2],[0,0],color='black',linestyle='dashed',linewidth = 0.5)
    plt.plot([0,0],[-1.2,1.2],color='black',linestyle='dashed',linewidth = 0.5)
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.show()
    


