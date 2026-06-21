#It is a beginner python project related to cafe restaurant
hotelmenu = { "Pasta" : 100,
              "Salad" : 200,
              "FrenchFries" : 300,
              "soup" : 100,
              "coke" : 20,
              "Burger" : 250,
              "Pizza": 400
             }
print("<<< Welcome to the CafeHome >>>")
print("Pasta : Rs100\nSalad : Rs200\nFrenchFries : Rs300\nsoup: Rs100\ncoke : Rs20\nBurger:Rs250\nPizza:Rs400")
print("** Place your order **")
while True:
 order_total = 0
 item_1 = input("Enter the food item you are craving for\n")
 if item_1 in hotelmenu:
  order_total += hotelmenu[item_1]
  print(f"Your food {item_1} is coming at your service")
 else:
     print(f"OOps the food {item_1} is not in our service")
     print(" <3 Try something else ")
 another = input(f"Do you want another item ? (yes:no)")
 if another.lower() != "yes":
   break
 item_2 = input(f"Enter the another item you want to have it?(yes:no):, so that you tummy feels great\n")
 if item_2 in hotelmenu:
   order_total += hotelmenu[item_2]
   print(f"Your food {item_2} is added in bucket")
 else:
   print("Ordered Item is not available")
print("f Amount to Be payed {order_total}")
print(order_total)
print("Mode of payment")
list1 = ["pay","Phonepe","Paytm","Sbipay"]
print(list1)
l_2 = input("Enter the method for payment : ")
print(f"{l_2} is choosed for payment method")



    

