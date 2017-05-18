
inventory={
    'gold':500,
    'pouch':['flint','twine','gemstone'],
    'backpack':['xylophone','dagger','bedroll','bread loaf']
    }

inventory['pocket']=['seacshell','strange','berry','lint']
print(inventory)

inventory['backpack'].sort()
print(inventory)

del (inventory['backpack'][2])
print(inventory)

inventory['gold']+=50
print (inventory)



