import matplotlib.pyplot as plt

plt.title("Trigonometric functions")
plt.xlim(-10, 360+10)
plt.ylim(-1.2, 1.2)
plt.xlabel("angle")
plt.ylabel("value")

plt.grid(True)

plt.xticks([0, 90, 180, 270], ['0(2pi)', 'pi/2', 'pi', '3pi/2'])
plt.yticks([-1, -0.3, 0, 0.3, 1])

plt.tick_params(axis='x', width=6, direction='in', color='blue', labelsize=15, labelcolor='blue')
plt.tick_params(axis='y', width=3, color='red')
plt.legend(['sine', 'cosine'], loc=(0.05, 0.85))
plt.show()
