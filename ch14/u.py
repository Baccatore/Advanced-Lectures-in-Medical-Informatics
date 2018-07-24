from scipy import fftpack
import numpy as np
from scipy.signal import butter, lfilter
from scipy.stats import pearsonr


def row2list(dF):
    a = []
    for series in dF:
        a.append(dF[series])
    return a


def extractRow(s1,n1,n2):
    s2 = s1[n1:n1+n2]
    return s2


def getFAlff(s1,fs):
    time_step = 1/fs
    X = fftpack.fft(s1)
    X = np.absolute(X)
    df = fs/len(X)
    sum1 = X[int(0.01/df):int(0.1/df)]
    sum2 = X[:int(0.25/df)]
    return sum1.sum()/sum2.sum()


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def getTimeSBand(data, fs, lowcut, highcut, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def myCorr(s1,s2):
    result = pearsonr(s1,s2)
    return result[0]
