# This is a sample Python script.
print (" Welcome to the tip calculator")
bill=input("What was the total bill?  ")
tippercentage=input("What percentage tip would you like to give?  10, 12, or 15? ")
totalperson=input("How many people to split the bill? " )

asintbill=int(bill)
asinttippercentage=int(tippercentage)
astotalperson=int(totalperson)

totalbill=asintbill*(100+asinttippercentage)/100
splitbill=(totalbill/astotalperson)
a=( round(splitbill,2) )
print(f"Each person should pay:{a} dollar")
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
