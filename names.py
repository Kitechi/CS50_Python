import sys

names = ["Bill", "Charlie", "Salah", "Sarim", "Hareera"]

name = input("Name: ")

if name in names:
    print("Found")
    sys.exit(0)
        
print("Not found")
sys.exit(1)