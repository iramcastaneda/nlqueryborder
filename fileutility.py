with open("data/ciudadecompleta","r") as file:
    for i in file:
        a=i.strip()
        print("ciudad[SEM='\P.P("+a+")'] -> '"+a+"'")

    file.close()
