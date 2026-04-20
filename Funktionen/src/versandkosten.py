def berechne_versandkosten(bestell_summe: float) -> float:
        
    if bestell_summe <= 50.00:
        return 5.00
    else:
        return 0.00

summe = 37.75
vsk = berechne_versandkosten(summe)    
print("Bestellsumme: " + str(summe) + ", Versandkosten: " + str(vsk))

summe = 65.83
vsk = berechne_versandkosten(summe)    
print("Bestellsumme: " + str(summe) + ", Versandkosten: " + str(vsk))