"""
Filename: factorial_calculator.py
Author: <Escobar, John>
Created: <DATE>
Instructor: Holtslander
"""

def factorial():
    cal = int(input("Enter a non-negative whole number on the line below:\n"))
    print(f"{cal}!", end=" ")
    for cal in range(cal, 0, -1):
        if cal == 1:
            print(cal, end=" ")
        else:
            print(cal, end=" * ")
    print(f"= {cal * cal}", end=" \n")
    if cal == "0":
        print("0! = 1")


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()
