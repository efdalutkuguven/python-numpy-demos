import numpy as np

num1 = np.random.randint(10,100,6)
num2 = np.random.randint(10,100,6)

print(num1)
print(num2)

result = num1 + num2
result = num1 + 10
result = num1 - num2
result = num1 - 10
result = num1 * num2
result = num2 * 10
result = num1 / num2
result = num1 / 10

result = np.sin(num1)
result = np.cos(num2)
result = np.sqrt(num1)
result = np.log(num1)

mnum1= num1.reshape(2,3)
mnum2 = num2.reshape(2,3)

# print(mnum1)
# print(mnum2)

result = np.vstack((mnum1,mnum2))
result = np.hstack((mnum1,mnum2))

result = num1 >= 50
result = num1 % 2 == 0

print(num1[result])


print(result)