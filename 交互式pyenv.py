try:
    from os import system
    while True:
        a=input("pyenv>")
        system(f"pyenv {a}")
except Exception as e:
    print(e)