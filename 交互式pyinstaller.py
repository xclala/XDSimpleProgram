try:
    from os import system
    while True:
        a=input("pyinstaller>")
        system(f"pyinstaller {a}")
except Exception as e:
    print(e)