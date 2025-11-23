class DistanceConverter:
    # The conversion factor provided in the question
    factor = 0.621371

    @staticmethod
    def kilometres_to_miles(km):
        return km * DistanceConverter.factor

    @staticmethod
    def miles_to_kilometres(miles):
        return miles / DistanceConverter.factor
        
print("1. Convert Kilometres to Miles")
print("2. Convert Miles to Kilometres")

choice = input("Choose an option (1 or 2): ")

distance = float(input("Enter the distance: "))

if choice == "1":
    result = DistanceConverter.kilometres_to_miles(distance)
    unit = "miles"
    
elif choice == "2":
    result = DistanceConverter.miles_to_kilometres(distance)
    unit = "kilometres"
    
else:
    print("Invalid choice")
    result = 0
    unit = ""
if choice in ["1", "2"]:
    print(f"Converted distance: {result:.2f} {unit}")