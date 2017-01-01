import matplotlib.pyplot as plt

x = [1,3,4,5,7]
y = [4,5,2,7,9]

plt.bar(x,y, label='Category1', width=0.3, align='center')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Bars Chart')
plt.legend()


plt.show()