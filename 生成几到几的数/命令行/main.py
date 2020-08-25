try:
    while True:from pprint import pprint;pprint([ i for i in range(int(input("起始的数：")), int(input("结束的数：")) + 1, int(input("步长：")))])       
except Exception as e:
    print(e)
