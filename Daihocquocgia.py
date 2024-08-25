# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:48:00 2024

@author: Admin
"""

print("bài 1")

print("tách kiểu 1")

chuoi="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

tach1=chuoi.split(', ')
for i in tach1:
    print(i)

print("tách kiểu 2")

tach2=(chuoi.replace('P.','').replace('Q.','').replace('Tp.','').split(', '))
for i in tach2:
    print(i)
    