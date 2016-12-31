import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [4,3,6,2,4]

plt.plot(x,y, label='line1', color='r')
plt.plot([0,1.5,2,4,5],[3,4,2,5,7], label='line2', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple line', color='m')
plt.legend()

plt.show()
