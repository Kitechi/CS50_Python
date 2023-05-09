def main():
    height = get_height()
    for i in range(height):
        print("#")
    for i in range(height):
        print("#", end="")
    print()
    print("#" * 4)
        
def get_height():
    while True:
        try:
            n = int(input("Height:"))
            if n>0:
                return n
        except ValueError:
            print("Not an integer")
    
main()
