choice = int(input("what type of convertion?"))

if choice == 1:
    type = int(input("enter number: "))
    print(format( type, "b"),)
elif choice == 2:
    type = int(input("enter number: "))
    print(format( type, "o"),)
elif choice == 3:
    type = int(input("enter number: "))
    print(format( type, "x"),)
else:
    print("invalid input. please try again.")

print("****************************")
print("| Number System Convertion |")
print("****************************")
print("By:Darapa, Hedjara")
print("Abdulkarim, Hakima")

print("**********************************************")
print("[1] Decimal Number to Binary Number")
print("[2] Decimal Number to Octal Number")
print("[3] Decimal Number to Hexadecimal Number")
print("**********************************************")





