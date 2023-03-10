# -*- coding: utf-8 -*-
"""ihagverdi_the4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M3GopRXl0DTvtCT_4Woji0c_PvWdDoN0
"""

def import_inventory():
  files = open("products.txt","r")
  process = (files.read()).replace("\n","-")
  product_list_mess = ((process.replace("_","-")).lower()).split("-") 
  productName_mess = product_list_mess[::2] 
  productCount = product_list_mess[1::2] 
  productName = []

  for a in productName_mess:
    if a not in productName:
      productName.append(a)

  clear_list = []  

  for a in productName:
    values = 0
    for b in range(len(productCount)):
      if productName_mess[b] == a :
        if a not in clear_list :
          clear_list.append(a)
          values = int(productCount[b])
        else:
          values += int(productCount[b])
    clear_list.append(values)
  products = {}
  counter = 1

  for a in clear_list[::2] :
    products[a] = clear_list[counter]
    counter += 2
  return products

  files.close()

products = import_inventory()

def sell_product(products):

  sell_input = input("Please enter products to sell: ")

  sell_2 = ((sell_input.replace("_","-")).lower()).split("-") 

  sellNames = sell_2[::2]
  sellCounts = sell_2[1::2]  
  nezaret = 0

  for a in sellNames:
    if products[a] == 0 :
      print(a,"does not exist in inventory.")
    else:
      products[a] -= int(sellCounts[nezaret])
      if products[a] < 0 :
        print("There is not enough", a, "in inventory.")
        products[a] +=  int(sellCounts[nezaret])
        nezaret += 1

      elif products[a] >= 0:
        print(int(sellCounts[nezaret]),a,"sold.")
        nezaret += 1

  return products

def show_remaining(products):
  sum = 0
  of = 0
  for a in products.values():
    sum += a 
  if sum == 0:
    print("Inventory is empty!")

  else:
    for a in products.items():
      print(a[0],":",a[1])

products = import_inventory()
decision = ""
while decision != "3":
  print("*---------------------------")
  print("[1] Sell products")
  print("[2] Show remaining inventory")
  print("[3] Terminate")

  decision = input("Please enter your decision: ")
  print("____________________________")
  if decision == "1":
    sell_product(products)
  elif decision == "2":
    show_remaining(products)
  elif decision == "3":
    print("Terminating...")
  else:
    print("Invalid input!")