TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    feed = input("Insert Celsius: ")
    try:
        value = float(feed)
    except:
        raise ValueError("could not convert string to float: '{}'".format(feed))

    if value < TEMP_MIN or value > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(value))

    return value


print("Program starting.")

try:
    c = collectCelsius()
    print("You inserted {} °C".format(c))
except Exception as e:
    print(e)

print("Program ending.")
