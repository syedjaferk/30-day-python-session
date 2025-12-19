commodity_price = {
	"rice": 40,
	"wheat": 50,
	"egg": 6,
	"oil": 118,
	"curd": 10,
	"carrot": 90
}

print("Commodities Available")
for key, value in commodity_price.items():
	print(key, value)

total_items = int(input("Enter Total Grocery Items :"))
print("Total Items", total_items)

groceries = []
user_picked_commodity = {}
bill_items = []
for itr in range(total_items):
 	grocery_name = input("Enter grocery item name: " + str(itr) + " ")
 	groceries.append(grocery_name)
 	
 	weight = float(input("Weight of " + grocery_name + " "))
 	user_picked_commodity[grocery_name] = weight * commodity_price.get(grocery_name, 0)
 	
 	billed_res = (
 					grocery_name,
 					weight,
 					commodity_price.get(grocery_name, 0),
 					user_picked_commodity.get(grocery_name)
 					)
 	bill_items.append(billed_res)


 
print("Groceries collected ", user_picked_commodity)

for item in bill_items:
	print(item)
