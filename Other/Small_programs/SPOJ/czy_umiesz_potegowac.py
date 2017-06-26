__author__ = 'bocian'

count = int(input())
data = []

for i in range(0,count):
    data.append(input())

for i in range(0,len(data)):

    a = int((data[i])[0])
    b = int((data[i])[2])

    print(str(a**b)[-1])
