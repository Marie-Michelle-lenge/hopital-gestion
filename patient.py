liste_patients = []


def enreg_patient(nom, pnom, prenom, tel, poids, taille, genre, age):
    patient = []
    patient.append(nom)
    patient.append(pnom)
    patient.append(prenom)
    patient.append(tel)
    patient.append(poids)
    patient.append(taille)
    while genre.lower() != "masc" and genre.lower() != "fem":
        genre = input("Le genre est invalide! entrer \"Masc\" ou \"Fem\" svp:")  # marie michelle
    patient.append(genre)
    try:
        while age < 0 or age > 150:
            age = int(input("Age incorrect! réessayer svp:"))
        patient.append(age)
    except ValueError:
        print("valeur invalide!")
        return
    if len(liste_patients) > 0:
        for i in range(len(liste_patients)):
            num_dossier = random.randint(10000000, 100000000)
            while num_dossier == list_patients[i][8]:
                num_dossier = random.randint(10000000, 100000000)
    else:
        num_dossier = random.randint(10000000, 100000000)
    patient.append(num_dossier)
    liste_patients.append(patient)
    if genre.lower() == "masc":
        print("Le patient \"", nom, pnom, prenom, "\" a été enregistré avec succès!")
    else:
        print("La patiente \"", nom, pnom, prenom, "\" a été enregistrée avec succès!")


def chercher_nom_patient(nom, pnom, prenom):
    if len(liste_patients) == 0:
        print("La liste des patients est vide!")
    else:
        noms_patients = []
        for i in range(len(list_patients)):
            noms = liste_patients[i][0] + liste_patients[i][1] + liste_patients[i][2]
            noms_patients.append(noms.lower())

        nouveau_nom = nom + pnom + prenom
        resultats = []
        for i in range(len(liste_patients)):
            if nouveau_nom.lower() == noms_patients[i]:
                resultats.append(liste_patients[i])
        if resultats == []:
            print("Aucun patient ne porte ce nom dans notre liste!")
        else:
            for i in range(len(resultats)):
                print(" Nom: ", resultats[i][0], \
                      "\n Post-nom: ", resultats[i][1], \
                      "\n Prénom: ", resultats[i][2], \
                      "\n Telephonne: ", resultats[i][3], \
                      "\n Poids: ", resultats[i][4], " Kg", \
                      "\n Taille: ", resultats[i][5], " m.", \
                      "\n Genre: ", resultats[i][6] + ".", \
                      "\n Age: ", resultats[i][7], " ans", \
                      "\n Dossier n° ", resultats[i][8], "\n")


def chercher_num_dossier(dossier):
    if len(liste_patients) == 0:
        print("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == liste_patients[i][8]:
                cle = i
        if cle == -1:
            print("Ce numero de dossier n'est pas attribué!")
        else:
            print(" Nom: ", liste_patients[cle][0], \
                  "\n Post-nom: ", liste_patients[cle][1], \
                  "\n Prénom: ", liste_patients[cle][2], \
                  "\n Telephonne: ", liste_patients[cle][3], \
                  "\n Poids: ", liste_patients[cle][4], " Kg", \
                  "\n Taille: ", liste_patients[cle][5], " m.", \
                  "\n Genre: ", liste_patients[cle][6] + ".", \
                  "\n Age: ", liste_patients[cle][7], " ans", \
                  "\n Dossier n° ", liste_patients[cle][8], "\n")


def aff_patients():
    if len(liste_patients) == 0:
        print("La liste des patients est vide!")
    else:
        for i in range(len(liste_patients)):
            print(" Nom: ", liste_patients[i][0], \
                  "\n Post-nom: ", liste_patients[i][1], \
                  "\n Prénom: ", liste_patients[i][2], \
                  "\n Telephonne: ", liste_patients[i][3], \
                  "\n Poids: ", liste_patients[i][4], " Kg", \
                  "\n Taille: ", liste_patients[i][5], " m.", \
                  "\n Genre: ", liste_patients[i][6] + ".", \
                  "\n Age: ", liste_patients[i][7], " ans", \
                  "\n Dossier n° ", liste_patients[i][8], "\n")


def enreg_plainte(dossier):
    if len(liste_patients) == 0:
        print("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(liste_patients)):
            if dossier == liste_patients[i][8]:
                cle = i
        if cle == -1:
            print("le numero de dossier n'est pas attribué!")
        else:
            plainte = input("Entrez une plainte pour " + liste_patients[cle][2] + " " + liste_patients[cle][0] + " :")
            liste_patients[cle].append(plainte)
            print("La plainte de ", liste_patients[cle][2], liste_patients[cle][0], " a été enregistrée avec succès!")


def enreg_horaire(matricule, dossier):
    if len(liste_docteur) == 0:
        print("La liste des docteurs est vide!")
    else:
        cle = -1
        for i in range(len(list_docteurs)):
            if matricule == liste_docteurs[i][4]:
                cle = i
        if cle == -1:
            print("Aucun medecin porte ce matricle!")
        else:
            if len(liste_patients) == 0:
                print("La liste des patients est vide!")
            else:
                cle2 = -1
                for i in range(len(liste_patients)):
                    if dossier == liste_patients[i][8]:
                        cle2 = i
                if cle2 == -1:
                    print("le numero de dossier n'est pas attribué!")
                else:
                    if len(liste_patients[cle2]) <= 9:
                        print("aucune plainte n'est disponible pour ", liste_patients[cle2][2], liste_patients[cle2][0])
                    else:
                        try:
                            for i in range(9, len(liste_patients[cle2])):
                                print("Plainte ", i - 8, ": ", liste_patients[cle2][i])
                            c1 = int(input("Entrez le numero de la plainte à ajouter"))
                            while c1 >= len(liste_patients[cle2]) - 8 or c1 <= 0:
                                c1 = int(input("Numero invalide! Entrez le numero d'une plainte à ajouter"))
                        except ValueError:
                            print("valeur invalide!")
                            return

                        c2 = input(
                            "Tapez un jour de la semaine en toute lettre (du lundi au samedi) auquel sera attachée la plainte:")
                        while c2.lower() != "lundi" and c2.lower() != "mardi" and c2.lower() != "mercredi" and \
                                c2.lower() != "jeudi" and c2.lower() != "vendredi" and c2.lower() != "samedi":
                            c2 = input("Veuillez réesayer svp (entre lundi et samedi uniquement!")

                        if c2.lower() == "lundi":
                            if liste_docteur[cle][6] == "Disponible":
                                liste_docteur[cle][6] = "Dossier n° " + str(liste_patients[cle2][8]) + ": " + \
                                                        liste_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", liste_patients[cle2][2], liste_patients[cle2][0],
                                      " prise en compte")
                            else:
                                c3 = input("Le docteur " + liste_docteur[cle][2] + " " + liste_docteur[cle][
                                    0] + " n'est pas disponible le lundi. Voulez-vous changer l'ancien programme?)
                                while c3.lower() != "oui" and c3.lower() != "non":  # marie michelle lenge
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                if c3.lower() == "oui":
                                    liste_docteurs[cle][6] = "Dossier n° " + str(liste_patients[cle2][8]) + ": " + \
                                                             liste_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", liste_patients[cle2][2],
                                          liste_patients[cle2][0], " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été cangée")

                        elif c2.lower() == "mardi":
                            if list_docteurs[cle][7] == "Disponible":
                                liste_docteurs[cle][7] = "Dossier n° " + str(liste_patients[cle2][8]) + ": " + \
                                                         liste_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", liste_patients[cle2][2], liste_patients[cle2][0],
                                      " a été prise en compte")
                            else:
                                c3 = input("Le docteur " + liste_docteurs[cle][2] + " " + list_docteurs[cle][
                                    0] + " n'est pas disponible le mardi. Voulez-vous ecraser l'ancien programme?")
                                while c3.lower() != "oui" and c3.lower() != "non":
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                if c3.lower() == "oui":
                                    list_docteurs[cle][7] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                            list_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                          " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été ecrasée.")

                        elif c2.lower() == "mercredi":
                            if list_docteurs[cle][8] == "Disponible":
                                list_docteurs[cle][8] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                        list_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                      " a été prise en compte")
                            else:
                                c3 = input("Le docteur " + list_docteurs[cle][2] + " " + list_docteurs[cle][
                                    0] + " n'est pas disponible le mercredi. Voulez-vous ecraser l'ancien programme?")
                                while c3.lower() != "oui" and c3.lower() != "non":
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                if c3.lower() == "oui":
                                    list_docteurs[cle][8] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                            list_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                          " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été ecrasée.")

                        elif c2.lower() == "jeudi":
                            if list_docteurs[cle][9] == "Disponible":
                                list_docteurs[cle][9] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                        list_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                      " a été prise en compte")
                            else:
                                c3 = input("Le docteur " + list_docteurs[cle][2] + " " + list_docteurs[cle][
                                    0] + " n'est pas disponible le jeudi. Voulez-vous ecraser l'ancien programme?")
                                while c3.lower() != "oui" and c3.lower() != "non":
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")  # lenge
                                if c3.lower() == "oui":
                                    list_docteurs[cle][9] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                            list_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                          " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été ecrasée.")

                        elif c2.lower() == "vendredi":
                            if list_docteurs[cle][10] == "Disponible":
                                list_docteurs[cle][10] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                         list_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                      " a été prise en compte")
                            else:
                                c3 = input("Le docteur " + list_docteurs[cle][2] + " " + list_docteurs[cle][
                                    0] + " n'est pas disponible le vendredi. Voulez-vous ecraser l'ancien programme?")
                                while c3.lower() != "oui" and c3.lower() != "non":
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                if c3.lower() == "oui":
                                    list_docteurs[cle][10] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                             list_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                          " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été ecrasée.")

                        elif c2.lower() == "samedi":
                            if list_docteurs[cle][11] == "Disponible":
                                list_docteurs[cle][11] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                         list_patients[cle2][c1 + 8]
                                print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                      " a été prise en compte")
                            else:
                                c3 = input("Le docteur " + list_docteurs[cle][2] + " " + list_docteurs[cle][
                                    0] + " n'est pas disponible le samedi. Voulez-vous ecraser l'ancien programme?")
                                while c3.lower() != "oui" and c3.lower() != "non":
                                    c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                if c3.lower() == "oui":
                                    list_docteurs[cle][11] = "Dossier n° " + str(list_patients[cle2][8]) + ": " + \
                                                             list_patients[cle2][c1 + 8]
                                    print("La plainte n° ", c1, " de ", list_patients[cle2][2], list_patients[cle2][0],
                                          " a été prise en compte")
                                else:
                                    print("Merci! La plainte en cours n'a pas été ecrasée.")

def aff_plaintes(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
                if len(list_patients[cle]) <= 9:
                        print("Il n'y a aucune plainte disponible pour ", list_patients[cle][2], list_patients[cle][0])
                else:
                        print (list_patients[cle][2], list_patients[cle][0], ":")
                        for i in range(9, len(list_patients[cle])):
                                print ("Plainte ",i-8, ": ", list_patients[cle][i])


def afficher_IMC(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
            imc = list_patients[cle][4]/list_patients[cle][5]
            if imc < 18.5:
                    print(list_patients[cle][2], list_patients[cle][0], ": Insuffisance pondérale (maigreur)")
            elif imc >= 18.5 and imc < 25:
                    print(list_patients[cle][2], list_patients[cle][0], ": Corpulence normale")
            elif imc >= 25 and imc < 30:
                    print(list_patients[cle][2], list_patients[cle][0], ": Surpoids")
            elif imc >= 30 and imc < 35:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité modérée")
            elif imc >= 35 and imc < 40:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité sévère")
            else:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité morbide ou massive")

