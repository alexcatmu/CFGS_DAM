def recogeNum():
    array_num = []
    for i in range(4):
        try:
            num = int(input("Introduce un numero"))
        except Exception as e:#Es de ValueError cuando introducimos una letra
            print("Detectat error "+ str(e))
            num = 0
        array_num.append(num)

    return array_num


print(recogeNum())