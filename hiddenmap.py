n = int(input())
al1=[None]*n
al2=[None]*n
al3=[None]*n

for i in range(0 , n):
    al1[i]=int(input())
    
for i in range(0 , n):
    al2[i]=int(input())
    
output = "["
for i in range(0 , n):
    al3[i]=str(bin(al1[i]|al2[i])).replace("1","#").replace("0"," ").replace(" b","")
    while(len(al3[i])!=2):
        al3[i]=" "+al3[i]
    if(i != n-1): output += '"'+al3[i]+'", '
    else:  output += '"'+al3[i]+'"]'
    
print(output)
