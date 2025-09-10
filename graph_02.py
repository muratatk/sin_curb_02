import numpy as np
import matplotlib.pyplot as plt

# データの生成
# 0から8πまでの範囲を1000個の点で分割してxの値を生成します。
# サインカーブの1周期は2πなので、4周期分は8πとなります。
x = np.linspace(0, 4 * 2 * np.pi, 1000)
y = np.sin(x)

# グラフの描画設定
plt.figure(figsize=(10, 5))  # グラフのサイズを指定
plt.plot(x, y)               # xとyの値をプロット

# グラフの装飾
plt.title("Sine Curve (4 Cycles)")  # グラフのタイトル
plt.xlabel("Radian [rad]")          # x軸のラベル
plt.ylabel("Value")                 # y軸のラベル
plt.grid(True)                      # グリッド線を表示
plt.axhline(0, color='black', linewidth=0.5) # y=0の線を引く

# グラフの表示
plt.show()