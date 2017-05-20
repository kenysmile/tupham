from turtle import *

def remove_dollar_sign(text):

    new=""
    new=text.replace("$","")
    
    return new
    
string_with_no_dollars=remove_dollar_sign("$80% percent of $life is to show $up")
    
if string_with_no_dollars=="80% percent of life is to show up":
        print("Your function is correct")
else:
        print("0pps,there's ia bug")







