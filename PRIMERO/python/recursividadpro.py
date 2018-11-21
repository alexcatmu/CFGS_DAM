def fibonaci(num):

    if (num == 0):
        return 0

    elif (num == 1 or num == 2):
        return 1

        
    else:

        return fibonaci(num-1) + fibonaci(num-2)




def CuantosFibonaci(cantidad,array_fibo):


    fib = fibonaci(cantidad)
    array_fibo.append(fib)
    
    print(fib)
    if (cantidad > 0):
        CuantosFibonaci(cantidad-1,array_fibo)
    else:
        return array_fibo

array_fibo = []


CuantosFibonaci(9,array_fibo)

print(array_fibo)






















    






