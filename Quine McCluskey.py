def read_minterms():
    minterm_string = input("Ingresar minterminos separados por espacios: ")
    dont_care_string = input("Ingresar don't care separados por espacios: ")
    dont_care = dont_care_string.split(" ")
    minterms = minterm_string.split(" ")
    return minterms, dont_care

if __name__ == "__main__":  
    # leer los mintérminos
    minterms, dont_care = read_minterms()

    # convertir a binario
    minterms = [bin(int(i))[2:].zfill(4) for i in minterms]
    dont_care = [bin(int(i))[2:].zfill(4) for i in dont_care]

    # ordenar
    minterms.sort()
    dont_care.sort()

    #agrupar
    groups = {}
    for i in range(4):
        groups[i] = []
    for i in minterms:
        groups[i.count('1')].append(i)
    for i in dont_care:
        groups[i.count('1')].append(i)

    print(groups.keys()[1])



