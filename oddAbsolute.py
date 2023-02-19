def calculateAbsolute():
    
    # This first line is provided for you
        try:
            in_num  = input("Enter a number: ")
            n = int(in_num)
            if n > 21:
                x = n - 21
                print("Result:", 2 * x)
            else:
                print("Result:", 21 - n)
        except:
            print("Please enter numerical digit")
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
