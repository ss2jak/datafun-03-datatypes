"""
Jakiel David
1/31/23
Trinidad 
"""
#Create some tuples
WeatherA = (24,33,27,29,30,27,29)
WeatherB = (28,28,30,26,27,29,29)
print()

#tuple concentration
Weather_2weeks = WeatherA + WeatherB
print()

Weather3 = WeatherA * 3
print()

print(f"{WeatherA = }")
print(f"{WeatherB = }")
print(f"{Weather_2weeks = }")
print(f"{Weather3 = }")
print()

#tuple indexing
Weeks_Forecast = (27,28,29,30,30,32,20)
sunday = Weeks_Forecast[0]
monday = Weeks_Forecast[1]
tuesday = Weeks_Forecast[2]
wednesday = Weeks_Forecast[3]
thursday = Weeks_Forecast[-3]
friday = Weeks_Forecast[-2]
saturday = Weeks_Forecast[-1]

print("Forcast this week:")
print(f"Temperature for sunday is {sunday}")
print(f"Temperature for monday is {monday}")
print(f"Temperature for tuesday is {tuesday}")
print(f"Temperature for wednesday is {wednesday}")
print(f"Temperature for thursday is {thursday}")
print(f"Temperature for friday is {friday}")
print(f"Temperature for saturday is {saturday}")
print()

#Use tuples to return multiple values from a function
def temperature_info(temperature):
    temperature_status = "hot" if temperature >= 25 else "cold"
    temperature_category = "humid" if temperature >= 28 else "kinda windy"
    return temperature_status, temperature_category

temperature = 28
temperature_status, temperature_category = temperature_info(temperature)
print(f"Temperature on monday will be {temperature}. Its going to be {temperature_status} and {temperature_category}.")

temperature = 20
temperature_status, temperature_category = temperature_info(temperature)
print(f"Temperature on saturday is {temperature}. It will be {temperature_status} and {temperature_category}.")



#Sets

setA = {24,33,27,29,30,27,29}
setB = {28,28,30,26,27,29,29}

#Set union: contains all elements that are in either set. 
setC = setA | setB

#Set intersection: that contains all elements that are in both sets. 
setD = setA & setB

#set difference: Set difference:contains all elements that are in one set but not in the other. 
setE = setA - setB

print()
print(f"The union of SetA and B {setC}")
print(f"Set A and Set B have {setD} in common")
print(f"The difference in set A and B is {setE}")
print()

#Dictionaries of Countries in Caribbean Country, their indepdence, national dish
print("List of Cities in TT with no duplicates")
Cities_in_Trinidad = ["Chaguanas","Chaguanas","PortofSpain","Arima","Couva","Laventille","Cunupia","PortofSpain"]
setCities = set(Cities_in_Trinidad)
Cities_NoDupes= [setCities]
print(setCities)
print()

print("Dictionaries of Countries in Caribbean and their indepdence, national dish")
Country1_dict={"Country": "Jamaica", "Indendence": "08/06/1962","Dish": "Ackee&Saltfish"}
Country2_dict={"Country": "Trinidad & Tobago", "Indendence": "08/31/1962","Dish": "Roti"}
Country3_dict={"Country": "Haiti", "Indendence": "01/01/1804","Dish": "Djon Djon"}

data_dict = {
    "County": ["Jamaica", " Trinidad & Tobago","Haiti"],
    "Indendence": ["08/06/1962", "08/31/1962","01/01/1804"],
    "Dish": ["Ackee & Saltfish","Roti","Djon Djon"],}

Caribbean_Countries = (f"{Country1_dict, Country2_dict, Country3_dict}")

print(Caribbean_Countries)

