# weight converter using if else #

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "L" or "l":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit == "K" or "k":
    converted = weight / 0.45
    print(f"You are {converted} pounds")


