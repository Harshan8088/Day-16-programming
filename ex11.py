import numpy as np

marks=np.array([90,40,20,60,56,69])

result=np.where(marks>=35,"pass","fail")
print(result)