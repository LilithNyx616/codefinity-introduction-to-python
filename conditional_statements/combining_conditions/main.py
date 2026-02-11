# The item's discount and stock status have been defined
discounted = False
lowStock = True
#task - define booleans and print message
movingProduct = discounted or lowStock
promotion = not discounted and not lowStock
print("Is the item eligible for promotion?", promotion)