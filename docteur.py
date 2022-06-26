import random
from datetime import date

liste_docteur = []  # La liste qui va contenir tout les docteurs et leurs  indentité


def enregistre_docteur(
                        nom_doc, prenom_doc, postnom_doc,
                        telephone_doc, specialisation_doc,
                        liste_matricule_doc
                                  
):
    liste_docteur.append(
                            [
                                nom_doc, prenom_doc, postnom_doc,
                                telephone_doc, matricule_docteur(nom_doc, postnom_doc, liste_matricule_doc),
                                specialisation_doc
                            ]
    )


def afficher_tout_les_docteurs():
    return liste_docteur


def enregistre_horaire_docteur(matricule_doc, horaires):
    for i in range(len(liste_docteur)):
        if matricule_doc == liste_docteur[i][8]:
            liste_docteur[i].append(horaires)


def prendre_rendez_vous_avec_docteur(matricule_doc, rendez_vous):
    for docteur in liste_docteur:
        if matricule_doc == docteur[4]:
            if len(docteur[-1]) >= 7:
                print("Désolé le docteur", docteur[0], docteur[1], docteur[2], "n'est pas disponible cette semaine ")
            else:
                print("Voici les jours ou le docteur n'est pas libre:\n ", docteur[-1])
                if rendez_vous in docteur[-1]:
                    print("Jour déjà occuper")
                else:
                    docteur[-1].append([rendez_vous])


def matricule_docteur(nom_doc, postnom_doc, liste_matricule_doc):
    today = str(date.today().year)
    """
    cette fonction nous permet de 
    généré un numéro unique du patient
    """
    chiffre = "0123456789"
    number = "".join(random.sample(chiffre, 3))
    number = today[2::] + (nom_doc[0] + postnom_doc[0]).capitalize() + number
    while number in liste_matricule_doc:
        chiffre = "0123456789"
        number = "".join(random.sample(chiffre, 3))
    liste_matricule_doc.append(number)
    return number
