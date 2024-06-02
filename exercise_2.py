import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def func(x):
    return x ** 2

a = 0  
b = 2  

def monte_carlo(a, b, num_experiments):
 
    x = np.random.uniform(a, b, num_experiments)
    y = np.random.uniform(0, func(b), num_experiments)

    points_under_curve = sum(y <= func(x))
    area_ratio = points_under_curve / num_experiments

    total_area = (b - a) * func(b)
    return total_area * area_ratio


# Number of experiments
# num_experiments = 100
# num_experiments = 1000
num_experiments = 10000


area_mc = monte_carlo(a, b, num_experiments)
print(f"Метод Монте-Карло:Інтеграл за {num_experiments} експериментів: {area_mc}")

# Checking
# Calculating using quad()
result, error = spi.quad(func, a, b)
print("Quad:Інтеграл: ", result)


x = np.linspace(-0.5, 2.5, 400)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = func(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

