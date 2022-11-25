
from errno import ENOSYS


devices = []
file = open("devices", "a")
while True:
    answer = input("Do you want to add the device? ")
    if answer == "no":
        break
    elif answer == "yes":
        newDevice = input("Enter device name: ")
        file.seek(0, 2)
        file.write(newDevice)
        for item in file:
            print(item)
            if newDevice == "exit":
                break
    else:
        print("I don't understand")
file.close()