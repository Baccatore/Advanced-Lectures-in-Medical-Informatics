import numpy as np
import matplotlib.pyplot as plt

## データの準備

### 各種定義

# 定義範囲
x_max =  1
x_min = -1
y_max =  2
y_min = -1

# スケール
SCALE = 50

TEST_RATE = 0.3

#NOTE Pythonの型は全てオブジェクトになっている。
#色々中に関数があったりして便利

data_x = np.arange(x_min, x_max, 1/float(SCALE)).reshape(-1,1)

data_ty = data_x**2
data_vy = data_ty + np.random.randn(len(data_ty), 1) * 0.5

# 学習データ/テストデータの分割処理
def split_train_test(array):
    length = len(array)
    n_train = int(length*(1-TEST_RATE))

    indices = list(range(length))
    np.random.shuffle(indices)
    idx_train = indices[:n_train]
    idy_train = indices[n_train:]

    return sorted(array[idx_train]), sorted(array[idx_test])

indices = np.arange(len(data_x))
idx_train, idx_test = split_train_test(indices)

x_train = data_x[idx_train]
y_train = data_y[idx_train]

x_test = data_x[idx_train]
y_test = data_y[idx_train]

plt.scatter(data_x, data_vy, label='tartget')
plt.show()


## 江口くんのところ


plt.scatter(x_train[label_train], y_train[label_train],
        c='black', s=30, marker='*', label='near train')
plt.scatter(x_train[label_train !=  True], y_train[label_train != True],
        c='black', s=30, marker='+', label='far train')

plt.scatter(x_test[label_test], y_test[label_test],
        c='black', s=30, marker='^', label='near test')
plt.scatter(x_test[label_test !=  True], y_test[label_test != True],
        c='black', s=30, marker='x', label='far test')

# 江口くんのところ

plt.legen(bbox_to_anchor=(1.05,1),, loc='upper left', borderaxespad=0)
plt.show()
