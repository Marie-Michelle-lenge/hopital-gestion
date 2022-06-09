import random
liste_docteur = []


def enreg_docteur(nom, pnom, prenom, tel, matricule, special):
    horaire = "Disponible"
    docteur = []
    docteur.append(nom)
    docteur.append(pnom)
    docteur.append(prenom)
    docteur.append(tel)
    docteur.append(matricule)
    docteur.append(special)
    docteur.append(horaire)
    docteur.append(horaire)
    docteur.append(horaire)
    docteur.append(horaire)
    docteur.append(horaire)
    docteur.append(horaire)

    if len(list_docteurs) > 0:
        matr = False
        for i in range(len(liste_docteur)):
            if matricule == liste_docteur[i][4]:
                matr = True
        if matr == True:
            print("Désolé, le numéro matricule entré appartient déjà à un docteur!")
        else:
            liste_docteur.append(docteur)
            print("Le docteur \"", nom, pnom, prenom, "\" a été enregistré avec succès!")  # marie
    else:
        liste_docteur.append(docteur)
            text()



def aff_docteurs():
    if len(liste_docteur) == 0:
        print ("La liste des docteurs est toute vide!")
    else:
        for i in range(len(liste_docteur)):
            print (" Nom: ", liste_docteur[i][0], \
                      "\n Post-nom: ", liste_docteur[i][1], \
                      "\n Prénom: ", liste_docteur[i][2], \
                      "\n Telephonne: ", liste_docteur[i][3], \
                      "\n Numero matricule: ", liste_docteur[i][4], \
                      "\n Specialisation: ", liste_docteur[i][5], "\n")

    def disponibilite_medecin(matricule):
        if len(list_docteurs) == 0:
            print("La liste des docteurs est vide!")
        else:
            cle = -1
            for i in range(len(list_docteurs)):
                if matricule == list_docteurs[i][4]:
                    cle = i
            if cle == -1:
                print("Aucun medecin ne porte ce matricle!")
            else:
                print("Docteur ", list_docteurs[cle][2], list_docteurs[cle][0], ":")
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
                for i in range(len(jours)):
                    print(jours[i], ": ", list_docteurs[cle][i + 6])
                choix = input("Tapez 1 pour ajouter un rendez-vous, ou 0 pour retourner au menu principal:")
                while choix != "1" and choix != "0":
                    choix = input("Veuillez taper 1 ou 0 svp")

                if choix == "1":
                    try:
                        enreg_horaire(matricule,
                                      int(input("Entrez le numero du dossier du patient à prendre en charge:")))
                    except ValueError:
                        print("Vous avez entré une valeur inavlide!")
                        return
                else:
                    print("Merci")




