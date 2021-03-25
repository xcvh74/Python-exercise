a=(eval(input("請輸入一個正整數:\t")))
total=0
for i in range(1,a+1):
    if i % 7==0:
       total+=i
       i+1
print("從1到",a,"之間7的倍數的總和是:",total)
