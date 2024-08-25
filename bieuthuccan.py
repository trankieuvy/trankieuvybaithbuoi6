# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:39:14 2024

@author: trankieuvy23717511
"""

"""
ketqua= (32)**0.2 - (1/64)**-0.25+(8/27)**(1/3)
print("giá trị của biểu thức là: ", round(ketqua,5))
"""

import math
a=float(input("nhập vào a: "))
b=float(input("nhập vào b: "))

x = math.sqrt(a)
y=math.sqrt(b)
z=a**(1/4)
x1= b**(1/4)
y2= (a*b)**(1/4)

ketqua= ((x-y)/(z-x1)) - ((x + y2 )/(z + x1))

print("kết quả của phép tính là: ", ketqua)

    

                                         
      
