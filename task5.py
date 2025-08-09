import numpy as np
import re
values = input().split()
rows = int(values[0])
cols = int(values[1])
mylist=[]
for i in range(rows):
        row = input()
        mylist.append(list(row))
numpy_array=np.array(mylist)
transposed=numpy_array.T
flattened=transposed.flatten()
text = ''.join(flattened)

#Regix
text = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', text)
print(text)
