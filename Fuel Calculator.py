uname = input("User name :")
u_vehicle_type = int(input("User Vehicle Type 1- Car, 2- Bike, 3-SUV :"))
v_f_t_capacity = int(input("Vehicle Fuel Tank Capacity (L)"))
fuel_type = int(input("Fuel Type 1- 92 Petrol, 2- 95 Petrol, 3- Super Diesel :"))
fuel_price = int(input("Fuel Price (Per L)"))
p_meter_r = float(input("Previous Meter Reading (Km) :"))
c_meter_r = float(input("Current Meter Reading (Km) :"))
h_m_f_p = float(input("How many Fuel you pumped Now (L) :"))
yon = input("Confirm or No (y- Confirm, n-No) :")
if(yon=="y"):
    print("hi ",uname )
    print("Previous Meter reading :",p_meter_r)
    print("Current Meter Reading :",c_meter_r)
    print("Pumped Fuel Type :",fuel_type)
    print("Fuel Price (Per 1 L) :",fuel_price)

    total_price = (c_meter_r-p_meter_r)*fuel_price
    print("Total Price :",total_price)

    fuel_efficiency = (c_meter_r-p_meter_r)/h_m_f_p
    print("Total Price :",fuel_efficiency)

    cost = (h_m_f_p)*fuel_price
    print("Cost (Per 1L) :",cost)

if yon=="n":
    print("not calculated")
else:
    print("syntax error")

input()


