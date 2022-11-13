uname = input("User name :")
UVehicalType = int(input("User Vehicle Type 1- Car, 2- Bike, 3-SUV :"))
VFTCapacity = int(input("Vehicle Fuel Tank Capacity (L) :"))
Fuel_Type = int(input("Fuel Type 1- 92 Petrol, 2- 95 Petrol, 3- Super Diesel :"))
Fuel_Price = int(input("Fuel Price (Per L) :"))
PMeterR = float(input("Previous Meter Reading (Km) :"))
CMeterR = float(input("Current Meter Reading (Km) :"))
HMFP = float(input("How many Fuel you pumped Now (L) :"))
YoN = input("Confirm or No (y- Confirm, n-No) :")
if(YoN=="y"):
	print("hi ",uname )
	print("Previous Meter reading :",PMeterR)
	print("Current Meter Reading :",CMeterR )
	print("Pumped Fuel Type :",Fuel_Type)
	print("Fuel Price (Per 1 L) :",Fuel_Price)

	Total_Price = (CMeterR-PMeterR)*Fuel_Price
	print("Total Price :",Total_Price)

	Fuel_Efficiency = (CMeterR-PMeterR)/HMFP
	print("Fuel Efficiency (Per 1L): ",str(Fuel_Efficiency )+"Km")

	Cost = (Fuel_Efficiency)*Fuel_Price
	print("Cost (Per 1L) :",Cost)




	