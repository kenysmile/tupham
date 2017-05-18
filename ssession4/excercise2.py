price={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

purchased=[["banana",5],["orange",3]]
    

total=0
def print_fruit(a,b,c):
    print(a ,"quantity: ",b," Unit price: ",c)

for fruit,quantity in purchased:
    print_fruit(fruit,quantity,price[fruit])
    total+=quantity*price[fruit]

print("total: ",total)




