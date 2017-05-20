
def get_even_list(t):
    even_list=[]
    for i in t:
        if i%2==0:
            even_list.append(i)
            print(even_list)
##        else:
##            print("1")
    return even_list
even_list=get_even_list([1,2,5,-10,9,6])
if set(even_list)==set([2,-10,6]):
    print("Your function is correct")
else:
    print("0oop,bufs detected")
    

