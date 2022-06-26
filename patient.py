import random
from datetime import date

liste_patient = []  # la liste qui contiendra les patients
plainte_patient = []  # liste des plaintes des patients


def enregistre_patient(
        nom_patient, prenom_patient, postnom_patient,
        telephone_patient, poids_patient,
        taille_patient, genre_patient,
        age_patient, dossier_numero_patient
):

    liste_patient.append(
        [
            nom_patient, prenom_patient, postnom_patient,
            telephone_patient, poids_patient,
            taille_patient, genre_patient,
            age_patient, gerence_numero_unique(nom_patient, postnom_patient, dossier_numero_patient)
        ]
    )


def afficher_tout_les_patients():
    return liste_patient


def recherche_patient_par_indentifiant(identifiant):
    # la fonction nous permet de rechercher
    # un patient par ces indentifiants
    # l'indentifiant peut être le nom,prenom
    # ou postnom du patient)

    for i in range(len(liste_patient)):
        if identifiant == liste_patient[i][0] or \
                identifiant == liste_patient[i][1] or \
                identifiant == liste_patient[i][2]:
            return liste_patient[i]


def recherche_patient_numero_unique(numero_unique_patient):
    # L'ID ou indentifiant unique du
    # patient nous permet de trouver
    # un patient par son numero unique

    for i in range(len(liste_patient)):
        if numero_unique_patient == liste_patient[i][8]:
            return liste_patient[i]


def enregistre_plainte_patient(numero_unique_patient):
    for i in range(len(liste_patient)):
        if numero_unique_patient == liste_patient[i][8]:
            liste_patient[i].append(plainte_patient)


def afficher_plainte_patient(numero_unique_patient):
    # on affiche les plaintes du patients
    # avec son numéro unique ou indentifiant unique

    for i in range(len(liste_patient)):
        if numero_unique_patient == liste_patient[i][8]:
            return liste_patient[i][9]


def gerence_numero_unique(nom_patient, postnom_patient, dossier_numero_patient):
    today = str(date.today().year)
    """
    cette fonction nous permet de 
    généré un numéro unique du patient
    """
    chiffre = "0123456789"
    number = "".join(random.sample(chiffre, 3))
    number = today[2::] + (nom_patient[0] + postnom_patient[0]).capitalize() + number
    while number in dossier_numero_patient:
        chiffre = "0123456789"
        number = "".join(random.sample(chiffre, 3))
        dossier_numero_patient.append(number)
    return number


def imc(numero_unique_patient):
    i = 0
    while numero_unique_patient != liste_patient[i][8]:
        i += 1
    else:
        Imc = float(liste_patient[i][4] / (liste_patient[i][5]) ** 2)
        if Imc < 18.5:
            return "Insuffisance pondérale(maigre)"
        elif 18.5 <= Imc < 25:
            return "Corpulence normal"
        elif 25 <= Imc < 30:
            return "Surpoids"
        elif 30 <= Imc < 35:
            return "Obésité modérée"
        elif Imc <= 35 and Imc < 40:
            return "Obésitée sévère"
        elif Imc > 40:
            return "Obésitée morbide ou massive"
