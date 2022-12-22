
import os
import csv
import ModuleCSV
clear = lambda: os.system('cls')

print("________________")
print("INTERFACE MENU")
print("________________")


fileName = ModuleCSV.fileName
fileFound = False
exitedMenu = False

personnes = []

def creerPersonne(nom, prenom, age, ville):
    nouvellePersonne = {
        
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "ville":ville
    }
    return nouvellePersonne

def ajouterPersonne(newPersonne):
    for personne in personnes:
        if newPersonne == personne["nom"]:
            return False

    personnes.append(newPersonne)
    return True

def printPersonnes():
    print("Nom de famille | Prénom | Age | Ville")
    for personne in personnes:
        print(personne['nom'], "  ", personne['prenom'] ,"  ", personne['age'], "  ", personne['ville'])

def modifierPersonne(selectedPersonne, nom, prenom, age, ville):
    found = False
    for personne in personnes:
        if selectedPersonne == personne["nom"]:
            personne["nom"] = nom
            personne["prenom"] = prenom
            personne["age"] = age
            personne["ville"] = ville
            found= True 
    return found

def supprimerPersonne(selectedPersonne):
    found = False
    for personne in personnes:
        if selectedPersonne == personne["nom"]:
            personnes.remove(personne) 
            found= True 
    return found
        

def loadPersonnes():
    lines = ModuleCSV.getLines()

    for line in lines:
        if len(line)>3:
            print(line[0])
            ajouterPersonne(creerPersonne(line[0],line[1],line[2],line[3]))

try :
    file= open(fileName, "r")
except FileNotFoundError :
    print("Fichier personnes.csv introuvable")
    fileName = str(input("Entrez le nom du fichier CSV : "))
    fileName += ".csv"
    try:
        file= open(fileName, "r")
    except FileNotFoundError :
        print("Fichier ",fileName, " introuvable")
        exitedMenu = True

loadPersonnes()

while(exitedMenu == False):
    print("\n[1] pour Afficher les personnes,[2] Ajout d'une personne, [3] pour Modifier une personne, [4] pour Supprimer une personne, [5] pour Quitter")
    print("________________")
    

    selectedOption = str(input("Choisissez une option : "))
    print(selectedOption)
    
    if(selectedOption== "1"):
        clear()
        print("| Affichage de la liste des personnes |")
        printPersonnes()


    elif(selectedOption == "2"):
        clear()
        print("| Ajout d'une nouvelle personne |")
        nom = prenom = age = ville = ""

        while (nom == "" or prenom == "" or age == "" or ville ==""):

            nom = str(input("Nom de famille : "))
            prenom = str(input("Prénom : "))
            age = str(input("Age : "))
            ville = str(input("Ville : "))
            added = ajouterPersonne(creerPersonne(nom,prenom,age,ville))
            if nom !="" and  prenom !="" and age !="" and ville !="" :
                if added:
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne ajouté avec succès")
                else:
                    clear()
                    print("La personne n'a pas été ajouté (existe déjà).")
            else:
                print("Pas d'ajout, aucun champs ne doit être vide.")

                
            

    elif(selectedOption =="3"):
        print("| Modification d'une personne |")
        selectedPersonne = str(input("Entrez le nom de famille de personne : "))
        nom = prenom = age = ville = ""
        while (nom == "" or prenom == "" or age == "" or ville ==""):
            nom = input("Nouveau nom : ") 
            prenom = input("Nouveau prénom : ")
            age = input("Nouvel age : ")
            ville = input("Nouvelle ville : ")
            if nom !="" and  prenom !="" and age !="" and ville !="" :
                modify = modifierPersonne(selectedPersonne,nom, prenom, age, ville)
                if modify:
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne modifié avec succès")
                else:
                    clear()
                    print("Aucune personne de ce nom trouvé")
            else:
                print("Aucun champs ne doit être vide.")

    elif(selectedOption == "4"):
        print("Suppression d'une personne")
        lastName = str(input("Entrez le nom famille d'une personne : "))
        validate = ""
        while(validate != "oui" and validate != "non"):
            validate = input("Etes-vous sûr de vouloir supprimer " + lastName+ " ? ")
            if(validate == "oui"):
                delete = supprimerPersonne(lastName)
                if delete:
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne supprimé avec succès")
                else:
                    clear()
                    print("Aucune personne de ce nom trouvé")
                   
            
        
    elif(selectedOption == "5"):
        clear()
        break;
    else:
        clear()
        print("Option incorrecte")
    

print("Fin du programme")