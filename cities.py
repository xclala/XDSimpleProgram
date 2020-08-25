while True:
    try:
        import os
        os.system ("cities_")
        a=input ("(完成后输入'ctrl+z'或者'ctrl+c'。)")
        b=input ("你喜欢它吗？(0/1)")
        if b=='0':
	        print ("我讨厌去"+a+"！")
        elif b=='1':
	        print ("我喜欢去"+a+"！")
        else:
	        print ("\a")
	        os.system ("cities__")
    except:
	    break


	
    
