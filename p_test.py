
import os,sys
print(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path.append(os.path.dirname(os.path.abspath(__file__))))
i = 10
i+1
print(i)
from package_test import test1
test1.test()
