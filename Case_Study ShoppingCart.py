#!/usr/bin/env python
# coding: utf-8

# In[2]:


shop_cart = {
    1 : {"Item":"Biscuit", 'Quantity':5,'cost':20},
    
    2 : {"Item":"Chocolate", 'Quantity':12,'cost':10},
    
    3 : {"Item":"Tea", 'Quantity':8,'cost':60},
    
    4 : {"Item":"Maggi", 'Quantity':30,'cost':80},
    
    5 : {"Item":"Masala", 'Quantity':40,'cost':30},}

name = input("Say Your name please Sir/Madam = ")
print("Hello {}, Welcome to A-Mart ".format(name))
choice = input("\nYou want to shop yes/no ? = ")


def cart():
    print("\nAll available items are listed here with quantity and cost :\n")
    print("%10s %10s %15s %10s"%("Sr.No","Item","Quantity","Cost"))
    print("%10s %10s %15d %10d"%('1',shop_cart[1]['Item'],shop_cart[1]['Quantity'],shop_cart[1]['cost']))
    print("%10s %10s %15d %10d"%('2',shop_cart[2]['Item'],shop_cart[2]['Quantity'],shop_cart[2]['cost']))
    print("%10s %10s %15d %10d"%('3',shop_cart[3]['Item'],shop_cart[3]['Quantity'],shop_cart[3]['cost']))    
    print("%10s %10s %15d %10d"%('4',shop_cart[4]['Item'],shop_cart[4]['Quantity'],shop_cart[4]['cost']))
    print("%10s %10s %15d %10d"%('5',shop_cart[5]['Item'],shop_cart[5]['Quantity'],shop_cart[5]['cost']))

    print("\n{} , Please tell your requirements : \n".format(name))
    biscuit = int(input("How many biscuits required ? "))
    chocolate = int(input("How many chocolate required ? "))
    tea = int(input("How many tea required ? "))
    maggi = int(input("How many maggi required ? "))
    masala = int(input("How many masala required ? "))
    return biscuit,chocolate,tea,maggi,masala


def essentials():
    biscuit_x = 5-biscuit
    cost_of_biscuits = 20*biscuit

    chocolate_x=12-chocolate
    cost_of_chocolates = 10*chocolate

    tea_x = 8-tea
    cost_of_tea=60*tea


    maggi_x = 30-maggi
    cost_of_maggi = 80 * maggi


    masala_x=40-masala
    cost_of_masala = 30*masala

    print("\nHere your shopping list with Bill :\n")
    print("\n%10s %10s %18s %25s %20s"%("Sr.No","Item","Quantity wants","Cost Amount","Stock Available"))
    print("%10s %10s %18d %25d %20d"%("1","Biscuit",biscuit,cost_of_biscuits,biscuit_x))
    print("%10s %10s %18d %25d %20d"%("2","Chocolate",chocolate,cost_of_chocolates,chocolate_x))
    print("%10s %10s %18d %25d %20d"%("3","Tea",tea,cost_of_tea,tea_x))
    print("%10s %10s %18d %25d %20d"%("4","Maggi",maggi,cost_of_maggi,maggi_x))
    print("%10s %10s %18d %25d %20d"%("5","Masala",masala,cost_of_masala,masala_x))

    Total_cost = cost_of_biscuits+cost_of_chocolates+cost_of_tea+cost_of_maggi+cost_of_masala
    print("\nCost = ",Total_cost)
    return cost_of_biscuits,cost_of_chocolates,cost_of_tea,cost_of_maggi,cost_of_masala,Total_cost


def generate_bill():
    

    delivery = 0
    print("\nHello {}, What is your loaction in km from Mart!".format(name))
    location = int(input("Enter your Address in Km from Mart = "))

    
    if location < 5:
        delivery = 10+delivery
        print("\nDilivery charge for {}km : ".format(location),delivery)
        Total_Bill_Amount = delivery + Total_cost
        print("\nTotal Bill Amount : ",Total_Bill_Amount)

    elif location >=5 and location < 10:
        delivery = 12+delivery
        print("\nDilivery charge for {}km : ".format(location),delivery)
        Total_Bill_Amount = delivery + Total_cost
        print("\nTotal Bill Amount : ",Total_Bill_Amount)

    elif location >= 10 and location <15:
        delivery = 14+delivery
        print("\nDilivery charge for {}km : ".format(location),delivery)
        Total_Bill_Amount = delivery + Total_cost
        print("\nTotal Bill Amount : ",Total_Bill_Amount)

    else:
        delivery = 20+delivery
        print("\nDilivery charge for {}km : ".format(location),delivery)
        Total_Bill_Amount = delivery + Total_cost
        print("\nTotal Bill Amount : ",Total_Bill_Amount)
    return delivery,location,Total_Bill_Amount

'''def e_generate_bill():
    
    Total_cost = cost_of_biscuits+cost_of_chocolates+cost_of_tea+cost_of_maggi+cost_of_masala
    print("\nCost = ",Total_cost)
    
    print("\nHello {}, What is your loaction in km from Mart!".format(name))
    location = int(input("Enter your Address in Km from Mart = "))
    Total_amount = Total_Bill_Amount + Total_cost
    print("Overall Bill Amount = ",Total_amount)'''
    
            
        
while True:
    if choice == 'yes' or choice == 'Yes' or choice == 'YES':
        
        biscuit,chocolate,tea,maggi,masala=cart()
        cost_of_biscuits,cost_of_chocolates,cost_of_tea,cost_of_maggi,cost_of_masala,Total_cost=essentials()
        delivery,location,Total_Bill_Amount=generate_bill()
     
        print("\n{},Thank u for Shopping in A-Mart".format(name))
        print("Visit Again!")
    else:
        print("\nThank u for visiting in A-Mart")
        print("{},Next Time Please buy something from A-Mart".format(name))
        break
    
    
    break


# In[ ]:




