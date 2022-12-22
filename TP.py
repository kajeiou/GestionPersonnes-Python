
import os
import csv
import ModuleCSV
clear = lambda: os.system('cls')

fileName = ModuleCSV.fileName
fileFound = False
exitedMenu = False

# Initialisation du dictionnaire Personnes

personnes = []
# Function Création d'une personne
def creerPersonne(nom, prenom, age, ville):
    nouvellePersonne = {
        
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "ville":ville
    }
    return nouvellePersonne

# Function Ajout Personne dans le dictionnaire
def ajouterPersonne(newPersonne):
    for personne in personnes:
        if newPersonne == personne["nom"]:
            return False

    personnes.append(newPersonne)
    return True

# Function Affichage du dictionnaire
def printPersonnes():
    print("Nom de famille | Prénom | Age | Ville")
    for personne in personnes:
        print(personne['nom'], "  ", personne['prenom'] ,"  ", personne['age'], "  ", personne['ville'])

# Function Modification Personne dans le dictionnaire
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

# Function Suppression d'une personne dans le dictionnaire
def supprimerPersonne(selectedPersonne):
    found = False
    for personne in personnes:
        if selectedPersonne == personne["nom"]:
            personnes.remove(personne) 
            found= True 
    return found
        
# Function Remplissage du dictionnaire à partir du CSV
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

print("________________")
print("INTERFACE MENU")
print("________________")

# Remplissage du dictionnaire
loadPersonnes()

# Script du Menu
while(exitedMenu == False):
    print("\n[1] pour Afficher les personnes,[2] Ajout d'une personne, [3] pour Modifier une personne, [4] pour Supprimer une personne, [5] pour Quitter")
    print("________________")
    

    selectedOption = str(input("Choisissez une option : "))
    print(selectedOption)
    
    # Choix listage des personnes
    if(selectedOption== "1"):
        clear()
        print("| Affichage de la liste des personnes |")
        printPersonnes()

    # Choix ajout d'une personne
    elif(selectedOption == "2"):
        clear()
        print("| Ajout d'une nouvelle personne |")
        nom = prenom = age = ville = ""

        while (nom == "" or prenom == "" or age == "" or ville ==""):

            # Formulaire ajout d'une nouvelle personne
            nom = str(input("Nom de famille : "))
            prenom = str(input("Prénom : "))
            age = str(input("Age : "))
            ville = str(input("Ville : "))
            added = ajouterPersonne(creerPersonne(nom,prenom,age,ville))
            if nom !="" and  prenom !="" and age !="" and ville !="" :
                if added:

                    # Mise à jour du CSV
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne ajouté avec succès")
                else:
                    clear()
                    print("La personne n'a pas été ajouté (existe déjà).")
            else:
                print("Pas d'ajout, aucun champs ne doit être vide.")

                
            
    # Choix édition d'une personne
    elif(selectedOption =="3"):
        print("| Modification d'une personne |")
        # Champs sélection d'une personne
        selectedPersonne = str(input("Entrez le nom de famille de personne : "))
        nom = prenom = age = ville = ""
        while (nom == "" or prenom == "" or age == "" or ville ==""):
            # Formulaire modification de la personne
            nom = input("Nouveau nom : ") 
            prenom = input("Nouveau prénom : ")
            age = input("Nouvel age : ")
            ville = input("Nouvelle ville : ")
            if nom !="" and  prenom !="" and age !="" and ville !="" :
                modify = modifierPersonne(selectedPersonne,nom, prenom, age, ville)
                if modify:
                    # Mise à jour du CSV
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne modifié avec succès")
                else:
                    clear()
                    print("Aucune personne de ce nom trouvé")
            else:
                print("Aucun champs ne doit être vide.")

    # Choix suppression d'une personne
    elif(selectedOption == "4"):
        print("Suppression d'une personne")
        # Champs sélection d'une personne
        lastName = str(input("Entrez le nom de famille d'une personne : "))
        validate = ""
        while(validate != "oui" and validate != "non"):
            validate = input("Etes-vous sûr de vouloir supprimer " + lastName+ " ? ")
            if(validate == "oui"):
                delete = supprimerPersonne(lastName)
                if delete:
                    # Mise à jour du CSV
                    ModuleCSV.newLines(personnes)
                    clear()
                    print("Personne supprimé avec succès")
                else:
                    clear()
                    print("Aucune personne de ce nom trouvé")
                   
            
    # Choix sortie programme
    elif(selectedOption == "5"):
        clear()
        break;

    # Choix incorrecte
    else:
        clear()
        print("Option incorrecte")
    

print("Fin du programme")