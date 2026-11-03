import numpy as np

a=np.array([10,20,30,40,50])

print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
import numpy as np
a = np.array([10, 20, 30, 40, 50])

print(np.where(a > 25, "High", "Low"))
print(np.clip(a, 15, 40))
print(np.argmax(a))
print(np.argmin(a))
print(np.cumsum(a))
print(np.cumprod(a))