from turtle import *

def remove_dolar_sign(text):

    new=""
    new=text.replace("$","")
    return new
      
text=("toi co 3$")
print(remove_dolar_sign(text))

