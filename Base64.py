import base64

print("__________                        ________   _____  ")
print("\______   \_____    ______ ____  /  _____/  /  |  | ")
print(" |    |  _/\__  \  /  ___// __ \/   __  \  /   |  |_")
print(" |    |   \ / __ \_\___ \\  ___ /\  |__\  \/    ^   /")
print(" |______  /(____  /____  >\___  >\_____  /\____   | ")
print("        \/      \/     \/     \/       \/      |__|  ")

def Decode():
    test= input("Enter Base64...")
    data_encoded = base64.b64decode(test)
    print("\n -------------------------")
    print(data_encoded.decode())
    print("\n")
    input("Press Enter to exit..")

def Encode():
    test = input("Enter text for Encoding...")
    data = base64.b64encode(test.encode())
    print("\n ------------------")
    print(data.decode())
    print("\n")
    input("Press Enter to exit...")

print("##########################################################")
choise = input("Enter\n -Encoding:1 \n -Decoding:2\n")

if choise == "2":
    Decode()
if choise == "1":
    Encode()
else:
    print("Error")




