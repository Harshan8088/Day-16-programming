import numpy as np

sales=np.array([
    [100,200,300],
    [400,500,600],
    [700,800,900]
])

result=np.sum(sales,axis=0)
print(result)

a=np.sum(sales,axis=1)
print(a)