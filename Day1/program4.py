x=float(input("enter the cost price of the item"))
y=float(input("enter the selling price of the item"))
if (x>y):
    print("there is loss")
    loss=x-y
    print("loss on item is",loss)
else:
    print("there is profit")
    profit=y-x
    print("profit on item is",profit)
    print("to gain 5% more profit ")
    sp=(profit*(105/100)+x)  
    print("selling price should be :",sp)  
