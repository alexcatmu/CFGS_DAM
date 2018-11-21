def funcio(p, *args, **kwargs):
    print("p: ", p)
    print("args", args)
    print("kwargs", kwargs)

def funcio2(p, q, *args, **kwargs):
    print("p: ", p)
    print("q: ", q)
    print("args", args)
    print("kwargs", kwargs)


funcio(1,2,3)
print()
funcio(1, 2, 3, quatre=4)
print()
funcio("holi", cuatre = 4, cinco=5, seis = 6)


print()

funcio2(1, 2, 3, quatre = 4, cinc = 5)

print()

funcio2(1, 2, quatre = 4, cinc = 5)
