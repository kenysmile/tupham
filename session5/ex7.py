from turtle import *
def extract_even(t):
    list_t=[]
    for i in t:
        if i%2==0:
            list_t.append(i)
            print(list_t)
##        else:
##            print("1")

            
extract_even([1,4,5,-1,10])            
