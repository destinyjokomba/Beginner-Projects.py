#Create products and give them a price

p1_name, p1_price = "Merlot Red wine", 13.99
p2_name, p2_price = "Salon Fillets", 11.49
p3_name, p3_price = "Basmati Rice", 3.49


#Create a store name with information 
store_name = "Quick Stop"
store_address = "7 Dalmation Road"
store_city = "Winchester"

#End message 
Message = "Thank you for shopping at Quick Stop!"

#Create a top border
print("*"*50)

#Print store information at the top
print("\t\t{}".format(store_name.title()))
print("\t\t{}".format(store_address))
print("\t\t{}".format(store_city))

#Sectioning each part 
print("*"*50)

#Header for items
print("\t Product Name \t Product Price")

#Print statement for each price 
print("\t{}\t\t£{}".format(p1_name.title(), p1_price))
print("\t{}\t\t£{}".format(p2_name.title(), p2_price))
print("\t{}\t\t£{}".format(p3_name.title(), p3_price))


#Line between each section 
print("*"*50)

#Print header for each section for the total
print("\t\t\t Total")

#Calculate Total cost and print out 
total = p1_price + p2_price + p3_price
print("\t\t\t£{}".format(f"{total:.2f}"))

#Print line between section 
print("*"*50)

#Output ending message 
print("\n\t{}\n".format(Message))


#Create bottom boarder 
print("*"*50)
