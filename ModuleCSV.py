import csv

fileName = "personnes.csv"

def getFileName():
    return fileName

# Function retourne toutes les lignes dans un tableau
def getLines():
    lines = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines

# Function mise à jour du CSV

def newLines(personnes):

    with open(fileName,"w", newline="") as outfile:

        writer = csv.DictWriter(outfile, fieldnames=["Nom", "Prenom",  "Age", "Ville"])
        for personne in personnes:
            #print(personne["nom"])
            new_row = {"Nom": personne["nom"], "Prenom": personne["prenom"], "Age" : personne["age"], "Ville": personne["ville"]}
        
            writer.writerow(new_row)