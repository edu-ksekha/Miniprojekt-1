# main.py

def meny():
    print("1. Visa alla citat")
    print("2. Lägg till nytt citat")
    print("3. Visa slumpmassigt citat")
    print("4. Avsluta")

def main(lista):
    while True:
        meny()
        val = input("Välj:")