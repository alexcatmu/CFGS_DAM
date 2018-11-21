#examen

array_fin = []
def aplana_EOL(num):
    
    if(isinstance(num,int) == True):
        array_fin.append(num)

    elif(isinstance(num,list) == True):
        for i in range(len(num)):
            
            if (isinstance(num[i],int) == True):
                array_fin.append(num[i])
                
            elif(isinstance(num[i],list) == True):
                
                aplana_EOL(num[i])
    return array_fin

#codigo

array_num = [[9,32,83],[[4]],[],8]

print(aplana_EOL(array_num))
