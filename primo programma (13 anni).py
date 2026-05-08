import math
from collections import Counter
 
dati=(3.83,3.79,3.85,3.76,3.80,3.86,3.80,3.78)
 
 
valore_massimo=max(dati)
valore_minimo=min(dati)
 
 
dato1=3.84
dato2=3.79
dato3=3.85
dato4=3.76
dato5=3.80
dato6=3.86
dato7=3.80
dato8=3.78
 
 
 
print("Ecco i tuoi dati:")
for dato in dati:
    print(dato)
 
print("I dati sono in totale:")
numero_dati=len(dati)
 
print (numero_dati)
 
somma_dati=dato1+dato2+dato3+dato4+dato5+dato6+dato7+dato8
 
print("La somma tuoi dati e':") 
print (somma_dati)
 
print("La media dei tuoi dati e':")
 
media=somma_dati/numero_dati
 
print(media)
 
 
scarto1=dato1-media
scarto2=dato2-media
scarto3=dato3-media
scarto4=dato4-media
scarto5=dato5-media
scarto6=dato6-media
scarto7=dato7-media
scarto8=dato8-media
 
 
print("Ecco i tuoi scarti")
print(scarto1,scarto2,scarto3,scarto4,scarto5,scarto6,scarto7,scarto8)    
 
 
scarto_quadrato1=(scarto1*scarto1)
scarto_quadrato2=(scarto2*scarto2)
scarto_quadrato3=(scarto3*scarto3)
scarto_quadrato4=(scarto4*scarto4)
scarto_quadrato5=(scarto5*scarto5)
scarto_quadrato6=(scarto6*scarto6)
scarto_quadrato7=(scarto7*scarto7)
scarto_quadrato8=(scarto8*scarto8)
 
 
 
print("Ecco i tuoi scarti quadratici")
 
print (scarto_quadrato1,scarto_quadrato2,scarto_quadrato3,scarto_quadrato4,scarto_quadrato5,scarto_quadrato6,scarto_quadrato7,scarto_quadrato8,)
 
somma_scarti_quadratici=scarto_quadrato1+scarto_quadrato2+scarto_quadrato3+scarto_quadrato4+scarto_quadrato5+scarto_quadrato6+scarto_quadrato7+scarto_quadrato8
 
 
print("Ecco la somma dei tuoi scarti quadratici")
print(somma_scarti_quadratici)
 
 
scarto_medio=somma_scarti_quadratici/numero_dati
 
print("Ecco il tuo scarto quadratico medio")
 
print (scarto_medio)
 
sigma=math.sqrt(scarto_medio)
 
print("Ecco il tuo sigma")
 
print(sigma)
 
 
 
print("Calcolando invece l'incertezza con la semidispersione massima,avremo questo risultato:")
 
differenza_valore_massimo_e_valore_minimo=(valore_massimo)-(valore_minimo)
 
incertezza=differenza_valore_massimo_e_valore_minimo/2
 
print(incertezza)
 
differenza=incertezza-sigma
 
 
print("L'incertezza data dalla semidispersione massima si sbaglia di")
print(differenza)
print("rispetto al sigma")
 
 
print("Per quanto riguarda l'incertezza relativa data dalla semidispersione massima,il risultato e'")
 
incertezza_relativa=incertezza/media
 
print(incertezza_relativa)
 
print("Per quanto riguarda l'incertezza relativa prendendo in considerazione il sigma, il risultato e'")
incertezza_relativa_sigma=sigma/media
print(incertezza_relativa_sigma)
 
 
print("Ecco l'incertezza percentuale,con la semidispersione massima")
incertezza_percentuale=incertezza_relativa*100
print(incertezza_percentuale)
 
print("Ecco invece l'incertezza percentuale con il sigma:")
incertezza_percentuale_sigma=incertezza_relativa_sigma*100
print(incertezza_percentuale_sigma)