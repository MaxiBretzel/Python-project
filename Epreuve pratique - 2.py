# Créé par Dorian, le 21/02/2022 en Python 3.7

#Exercice 1 :
def recherche_occurence(elt,tab):
    for i in range (len(tab)):
        if tab[i]==elt:
            return True
    return False

assert recherche_occurence(2,[1,3,5,2,4])==True
assert recherche_occurence(2,[1,3,5,3,4])==False

def recherche(elt,tab):
    ind=0
    for i in range(len(tab)):
        if tab[i]==elt:
            ind=i
            return ind
    return -1

assert recherche(1,[2,3,4])==-1
assert recherche(1,[10,12,1,56])==2
assert recherche(50,[1,50,1])==1
assert recherche(15,[8,9,10,15])==3

#Exercice 2 :
def inverse_chaine(chaine):
    result=('')
    for caractère in chaine:
        result=chaine[::-1]
    return result

assert inverse_chaine('bac')=='cab'

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    if inverse==chaine:
        return True
    return False

assert est_palindrome('NSI')==False
assert est_palindrome('BOB')==True

def est_nbre_palindrome(nbre):


assert est_nbre_palindrome(214312)==False
assert est_nbre_palindrome(213312)==True





