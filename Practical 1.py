fh = open("prac 1.txt",'w')
c=float(input("enter celsius value : "))
f=(c*(9/5)+32)
fh.write("fahrenheit is : "+str(f)+"\n")
    
f=int(input("enter fahrenheit value : "))
c=((f-32)*5/9)
fh.write("celsius convertion is: "+str(c))
fh.close()

