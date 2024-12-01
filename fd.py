import matplotlib.pyplot as plt
import numpy as np

# значения со спектрофотометра
yD_water = [1.879, 0.613, 0.516, 0.463, 0.386, 0.302]
water = 0.235

# вычесть воду из значений
yD = [y - water for y in yD_water]

# секунды
x = [40, 80, 140, 260, 440, 620]
y = np.array(yD)
x = np.array(x)


# написовать точки
plt.plot(x, y, "ro", ms=2, label="Data points")

# соединить точки
plt.plot(x, yD)

# надписи всякие
plt.xlabel("Секунды")
plt.ylabel("Absorbance at 600 nm")
plt.title("График зависимости детекции субстрата")

# сетка и легенда
plt.grid(True)
plt.legend()


plt.show()
