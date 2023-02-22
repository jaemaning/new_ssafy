from collections import deque
from collections import OrderedDict

a = OrderedDict()
print(a)
for i in range(5):
    a[i] = 1
a[2] = 66
print(a)

b = deque(a)
print(b)