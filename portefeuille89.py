b = [1, 5, 10, 20, 50, 89, 100]

def porteFeuilleLePlusLegerEnSommes(l):
    billetsChoisisParSomme = []
    for t in range(len(b)-1, -1, -1):  # iterer du billet le plus grand au billet le plus petit
        while l >= b[t]:  # tant que le montant est superieur au billet
            billetsChoisisParSomme.append(b[t])
            l -= b[t] #soustraire la valeur du billet au montant
    return billetsChoisisParSomme

def porteFeuillePlusLegerEnMultiples(l):
    billetsChoisisParMultiplesDe89 = []
    if l >= 89: #car il doit etre superieur a 89 pour etre un multiple de 89  
        while l >= 89:  # tant que le montant est superieur au billet
            if l % 89 == 0: #si l multiple direct de 89
                y = l / 89 #trouver le diviseur
                y = int(y)
                for i in range(y): #ajouter y fois 89 dans la liste
                    billetsChoisisParMultiplesDe89.append(89)
                return billetsChoisisParMultiplesDe89
            elif l % 89 != 0: #si ce n'est pas un multiple direct de 89
                r = l % 89 #trouver le reste de la division de l par 89
                y = (l-r)/89 #trouver le diviseur en enlvant le reste
                y = int(y) 
                for i in range(y): #ajouter y fois 89 dans la liste
                    billetsChoisisParMultiplesDe89.append(89)
                for t in range(len(b)-1, -1, -1):
                    while r >= b[t]: 
                        billetsChoisisParMultiplesDe89.append(b[t])
                        r -= b[t]
                return billetsChoisisParMultiplesDe89

    elif l < 89:
        return porteFeuilleLePlusLegerEnSommes(l)
    return billetsChoisisParMultiplesDe89

def optimalPorteFeuille(l):
    if len(porteFeuilleLePlusLegerEnSommes(l)) <= len(porteFeuillePlusLegerEnMultiples(l)):
        return porteFeuilleLePlusLegerEnSommes(l)
    else:
        return porteFeuillePlusLegerEnMultiples(l)
    
print(optimalPorteFeuille(179))
