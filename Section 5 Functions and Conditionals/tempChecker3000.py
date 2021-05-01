def tempChecker3000(temp):
    if temp > 25:
        return "Hot"
    elif temp in range(15, 25+1):
        return "Warm"
    elif temp < 15:
        return "Cold"
    
    
test = tempChecker3000(15)
print(test)