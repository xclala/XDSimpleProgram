try:
    from os import system
    while True:
        system("素数判断")
except Exception as e:
    print(e)