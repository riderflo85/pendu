#! /usr/bin/env python3.7
# coding: utf-8
import donnees
import fonctions

welcome = "Bonjour et bienvenu à toi !"
# Vérifie si le fichier 'score' est présent (fait appel à une fonction)
# 'score' est un dict
fonctions.load_file_score
score = fonctions.load_file_score()

# Dire bonjour et demander le nom du joueur (input)
print(welcome.upper().center(44))
print("Quel est ton prénom ? :")
name = input(" ")

# Vérifie si le joueur est présent dans le fichier 'score' (fait appel à une fonction)
state = fonctions.joueur_present(name)


parti_continue = "o"
# Boucle qui demande au joueur de saisir une lettre du mot pris au hasard
while parti_continue != "n":
    mot_a_trouver = fonctions.mot_choisi()
    # Contenir les lettres trouvées dans une liste
    lettre_trouvées = []
    mot_trouve = fonctions.done_word(mot_a_trouver, lettre_trouvées)
    nb_chance = 8
    
    # Vérifier que la lettre saise est bien dans le mot
    while mot_trouve != mot_a_trouver and nb_chance > 0:
        print("Mot à trouver {} (encore {} chances)".format(mot_trouve, nb_chance))
        lettre = fonctions.done_letters()
        # Lettre déjà saisie
        if lettre in lettre_trouvées:
            print("Tu as déjà trouver cette lettre")
        elif lettre in mot_a_trouver:
            lettre_trouvées.append(lettre)
            print("Bien jouer !")
        else:
            nb_chance -= 1
            print("...Cette lettre ne se trouve pas dans le mot...")
        mot_trouve = fonctions.done_word(mot_a_trouver, lettre_trouvées)

    if mot_trouve == mot_a_trouver:
        print("Bien jouer tu as trouver le mot {}".format(mot_a_trouver))
    else:
        print("PENDU !!! tu as perdu la parti")
    
    score[name] += nb_chance

    print("Ton score est actuellement de {} point(s)".format(score[name]))
    
    parti_continue = input("Souhaite tu continuer la partie ? (o/n) : ")

# On enregistre le score avec la fonction save_score(score) en passant en paramètre le dicotionnaire 'score'
fonctions.save_score(score)
print("Merci et à bientôt !")