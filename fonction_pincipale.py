from docteur import *
from patient import *

liste_matricule_doc = []
horaires = []
dossier_numero_patient = []


def main():
    print("****** Bienvenue ****** ")
    print("Voici les options pour enregistre :"
          "\n1 :pour enregistre le docteur"
          "\n2 :pour enregistre un patient"
          "\n3 :pour chercher un patient par ses identifiants(nom,postnom ou prenom)"
          "\n4 :rechercher le patient par le numero de son dossier"
          "\n5 :affichez tout les patients"
          "\n6 :afficher tout les docteur"
          "\n7  :Enregistre plainte patient "
          "\n8 :Enregistre horaire des docteurs"
          "\n9 :Affichez l'IMC d'un patient a partir de son numero "
          "\n10:Affichez plainte d'un patient a partir de son numero unique "
          "\n11:Verifier la disponibilite du docteur"
          "\n12:Enregistre plainte patient par numero doc"
          "\n13:Arreter les operations")
    reponse = 'oui'
    while reponse == 'oui':
        reponse = (input("Voulez vous  enregistre quelque chose ?(oui/non): ")).lower()
        if reponse != 'oui':
            break

        choix = input("Veillez choisir une option : ")

        if choix == "1":

            nom_doc = (input("Entrez le nom du docteur : ")).capitalize()
            prenom_doc = (input("Entrez le prenom du docteur : ")).capitalize()
            postnom_doc = (input("Entrez le postnom du docteur : ")).capitalize()
            telephone_doc = input("Entrez le numero de telephone du docteur : ")
            specialisation_doc = input("Entrez la specialisation du docteur : ")

            enregistre_docteur(
                nom_doc, prenom_doc, postnom_doc,
                telephone_doc, specialisation_doc,
                liste_matricule_doc
            )

        elif choix == "2":

            nom_patient = (input("Entrez le nom du patient : ")).capitalize()
            prenom_patient = (input("Entrez le prenom du patient : ")).capitalize()
            postnom_patient = (input("Entrez le postnom du patient : ")).capitalize()
            telephone_patient = input("Entrez le numero de telephone du patient : ")
            poids_patient = int(input("Entrez le poids du patient; ex : 35 : "))
            taille_patient = float(input("Entrez la taille du patient; ex : 1.60 : "))
            genre_patient = input("Entrez le genre du patient; Ex : F/M : ")
            age_patient = input("Entrez l'âge du patient; Ex : 20 ans : ")

            enregistre_patient(
                nom_patient, prenom_patient, postnom_patient,
                telephone_patient, poids_patient,
                taille_patient, genre_patient, age_patient,
                dossier_numero_patient
            )
        elif choix == "3":

            identifiant = (input("Entrez le nom,postnom ou prenom pour trouver votre malade : ")).capitalize()
            print(recherche_patient_par_indentifiant(identifiant))

        elif choix == "4":

            numero_unique_patient = input("Entrez le numero du document du patient: ")
            print(recherche_patient_numero_unique(numero_unique_patient))

        elif choix == "5":

            print(afficher_tout_les_patients())

        elif choix == "6":

            print(afficher_tout_les_docteurs())

        elif choix == "7":
            numero_unique_patient = input("Entrezle numero unique du patient: ")
            reponse = 'oui'
            while reponse == 'oui':
                reponse = (input("Voulez vous enregistre des plaintes ? : ")).lower()
                if reponse != "oui":
                    enregistre_plainte_patient(numero_unique_patient)
                break
            plainte = input("Que ressentez vous ? : ")
            plainte_patient.append(plainte)

        elif choix == "8":

            matricule_doc = input("Veiller entrez le matricule du docteur: ")
            reponse = 'oui'
            while reponse == 'oui':
                reponse = (input("Voulez vous enregistre vos jours de travail à l'hopital ? : ")).lower()
                if reponse != "oui":
                    enregistre_horaire_docteur(matricule_doc, horaires)
                break
            jour = (input("Entrez un jour ou vous serez à l'hopital  : ")).capitalize()
            if jour in horaires:
                print("Oups !!!, viellez entre un nautre jour car celui ci est reservé !.")
            else:
                horaires.append(jour)

        elif choix == "9":
            numero_unique_patient = input("Entrez le numéro de document de notre patient : ")
            print(imc(numero_unique_patient))

        elif choix == "10":
            numero_unique_patient = input("Entrez le numero du document du patient: ")
            print(afficher_plainte_patient(numero_unique_patient))

        elif choix == "11":
            if len(liste_docteur) == 0:
                print("Opération pas encore disponible !")
            else:
                matricule_doc = input("Entrez le numero_unique_doc du docteur : ")
                rendez_vous = (input("prenez votre le rendez_vous avec docteur : ")).capitalize()
                prendre_rendez_vous_avec_docteur(matricule_doc, rendez_vous)

        elif choix == "12":
            numero_unique_patient = input("Entrez le numero du document du patient : ")
            enregistre_plainte_patient(numero_unique_patient)

        elif choix == "13":
            break


main()
