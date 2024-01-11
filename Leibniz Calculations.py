
"""
Created on 1/11/2024
@author: Ethan Magursky
Description: To write a program in Python that given a positive integer k, returns the sum of the
 first k terms of the series from the Leibniz Formula
 """
digits = input("Enter digits: ")

digits = int(digits)
my_list = []
k = 1
for k in range(digits):
    sub_list=((-1)**k)/(2*k + 1)
    my_list.append(sub_list)
print ( sum (my_list))



