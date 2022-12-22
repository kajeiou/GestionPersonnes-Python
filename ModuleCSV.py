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

    with open(fileName,"w", newline="", encoding="utf-8-sig") as outfile:

        writer = csv.DictWriter(outfile, ["Nom", "Prenom",  "Age", "Ville"])
        for personne in personnes:
            new_row = {"Nom": personne["nom"], "Prenom": personne["prenom"], "Age" : personne["age"], "Ville": personne["ville"]}
        
            writer.writerow(new_row)