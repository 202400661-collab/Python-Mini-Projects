square_feet=float(input("Enter house size(sq.ft):"))
rent=float(input("Enter monthly rental amount:"))
advance=float(input("Enter advance amount:"))
own_house=input("Is it your own house:")
#ESTIMATED HOUSE
house_price=(square_feet*4000)+(rent*12)+advance
#OWN HOUSE
if own_house.lower()=="Yes":
    house_price+=200000
#CATEGORY
if house_price>=5000000:
    category="Luxury House"
elif house_price>=3000000:
    category="Premium House"
elif house_price>=1500000:
    category="standard House"
else:
    category="Budget House"
#OUTPUT
print("\n---HOUSE PRICE PREDICTION---")
print("House size:",square_feet,"sq.ft")
print("Monthly Rent:",rent)
print("Advance Amount:",advance)
print("Own house:",own_house)
print("Estimated price:",house_price)
print("Category:",category)            
