b = [1, 5, 10, 20, 50, 100]

def portefeuillePlusLeger(l):
    billetsSelectionne = []
    for t in range(len(b)-1, -1, -1):  # iterate from the largest to the smallest bill
        while l >= b[t]:  # while we can use the current bill
            billetsSelectionne.append(b[t])
            l -= b[t]
    return billetsSelectionne

print(portefeuillePlusLeger(189)) 