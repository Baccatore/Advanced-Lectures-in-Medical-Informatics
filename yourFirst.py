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

plt.scatter(data_x, data_vy, label='tartget')
plt.show()

