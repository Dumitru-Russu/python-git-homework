
from restaurant import *

#contains order data
order = {
    "items":[]
}

###############################################
food = loadFood()

while True:
    option = printMenu()

    if option==0:
        break

    if option ==1:
        printFood(food)
        input("Hit ENTER to continue")

    if option==2:
        selected_i = int(input("which item: ")) - 1
        print(f"You've selected <<{food[selected_i]['name']}>>")
        quantity = int(input("How many: "))
        if quantity <= food[selected_i]["avail"]:
            price_per_item = quantity * food[selected_i]['price']['amount']
            print(f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}")
            answer = input("Confirm your order?(yes/no)" )=="yes"

        else:
            print(f"Unfortunately, there are just {food[selected_i]['avail']} left.")
            answer_lq = input("Do you want to purchase just the left quantity?(yes/no)")=="yes"
            if answer_lq:
                quantity=food[selected_i]["avail"] 
                price_per_item = quantity * food[selected_i]['price']['amount']
                print(f"<<{food[selected_i]['name']}>> x {quantity} = {price_per_item:8.2f}{food[selected_i]['price']['currency']}")
                answer = input("Confirm your order?(yes/no)" )=="yes"

        
        if answer:
            order["items"].append\
            ({"name":food[selected_i]["name"],\
            "quantity": quantity, "total":{"amount":price_per_item,\
            "currency":food[selected_i]['price']['currency']}})



        input("Hit ENTER to continue")



print(order)