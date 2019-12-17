from Huffman import Huffman

tipo = input("C para comprimir o D para descomprimir: ")

if(tipo == "C"):
    fichero_comprimir = input("Ruta/nombre del archivo que desea comprimir: ")
    fichero_destino = input("Ruta/nombre del destino del archivo comprimido: ")
    fichero_claves = input("Ruta/nombre del fichero de claves, importante no perderlo!!: ")
    # fichero a comprimir, nombre del fichero de destino, fichero de claves
    # hofman_comprime = Huffman("intel.bmp","intel.estonofunciona", "intel.key", "C")
    Huffman(fichero_comprimir, fichero_destino,fichero_claves, "C")
elif(tipo == "D"):
    fichero_descomprimir = input("Ruta/nombre del archivo que desea descomprimir: ")
    fichero_destino = input("Ruta/nombre del destino del archivo comprimido: ")
    fichero_claves = input("Ruta/nombre del fichero de claves: ")
    # fichero a descomprimir, nombre del fichero de destino, fichero de claves
    # hofman_descomprime = Huffman("intel.estonofunciona", "inteldescomprimido.bmp", "intel.key","D")
    Huffman(fichero_descomprimir, fichero_destino, fichero_claves, "D")
else:
    print("No has introducido un tipo valido, el programa se cerrará")