#dragon loot March 3, 2016

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']




def addToInventory(inventory, addItems):
    for new_item in addItems:
        if new_item in inventory:
            inventory[new_item] += 1
        else:
            inventory.setdefault(new_item, 1)
    return(inventory)




"""continue from here

        inventory.setdefault(loot, 0)
        print(inventory)
    for k, v in inventory:
        k =
"""

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
            print(str(v) + ' ' + str(k))
            item_total = item_total + int(v)
    print ("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


