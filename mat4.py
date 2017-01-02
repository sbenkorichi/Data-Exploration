import matplotlib.pyplot as plt

x = [1,3,4,5,7]
y = [4,5,2,7,9]

plt.scatter(x,y, label='Category1', marker='+', s=60)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter Chart')
plt.legend(loc='upper center')

plt.show()