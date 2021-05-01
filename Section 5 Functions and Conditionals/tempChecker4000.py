import os

os.system("cls") #clear the screen at start
def tempChecker3000(temp):
    if temp > 25:
        return "Hot"
    elif temp in range(15, 25+1):
        return "Warm"
    elif temp < 15:
        return "Cold"
    
user_name = str(input("Hello there! What is your first name: \n"))
user_temp = float(input(f"Hello {user_name}, please enter a temperature: \n"))
print(f"It is {tempChecker3000(user_temp)} outside at {user_temp} degrees. Have a great day!")