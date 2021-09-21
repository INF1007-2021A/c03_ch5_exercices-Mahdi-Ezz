#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *=-1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_noms=[]
    for lettre in prefixes:
        liste_noms.append(lettre+suffixe)
    return liste_noms


def prime_integer_summation()-> int:
    nombre=2
    diviseur=2
    nb_premiers=[2]
    while len(nb_premiers)<100:
        while nombre%diviseur!=0:
            diviseur+=1
            if diviseur==nombre:
                nb_premiers.append(nombre)
        nombre+=1
        diviseur=2
    return sum(nb_premiers)


def factorial(number: int) -> int:
    factoriel_nb=1
    while number > 1:
        factoriel_nb *= number
        number-=1
    return factoriel_nb


def use_continue() -> None:
    entiers=''
    for i in range (1,11):
        if i==5:
            continue
        else:
            print(i)

            
    


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance=[]
    for num_groupe in range(len(groups)):
        if len(groups[num_groupe])>10 or len(groups[num_groupe])<=3:
            acceptance.append(False)
            continue
        else:
            for age in groups[num_groupe]:
                if 25 in groups[num_groupe]:
                    acceptance.append(True)
                    break
                elif age<18:
                    acceptance.append(False)
                    break
                elif age>70 and 50 in groups[num_groupe]:
                    acceptance.append(False)
                    break
                else:
                    acceptance.append(True)
                    break

            

    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
