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

### 飛ばす

plt.scatter(data_x, data_vy, label='tartget')
plt.show()

