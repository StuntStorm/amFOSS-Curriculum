def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(v, ' ', k)
        total += v
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    updatedInventory = dict(inventory)
    for item in addedItems:
        updatedInventory.setdefault(item, 0)
        updatedInventory[item] += 1
    return updatedInventory


print("Fantasy Game Inventory\n")
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
print("\n\nList to Dictionary Function for Fantasy Game Inventory\n")
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
