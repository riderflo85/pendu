#! /usr/bin/env python3.7
# coding: utf-8
import random
import pickle
import donnees

"""Fichier contenant les principales fonctions du jeu"""


# Vérifie si le fichier 'score' existe (try:)
def load_file_score():
    # Si il existe pas, le créer et y mettre un dico vierge (pickle)
    try:
        with open(donnees.score_file, "rb") as fichier:
            data_download = pickle.Unpickler(fichier)
            return data_download.load()
    except FileNotFoundError:
        with open(donnees.score_file, "wb") as fichier:
            data_upload = pickle.Pickler(fichier)
            data_upload.dump(donnees.scores)


# Vérifie si le joueur est dans le fichier 'score'
def joueur_present(name):
    # Si le joueur n'y est pas, le mettre ainsi que le score 0 dans le dico et l'envoyer dans le fichier
    score = load_file_score()
    
    if name not in score.keys():
        score[name] = 0
        data = open(donnees.score_file, "wb")
        ecriture = pickle.Pickler(data)
        ecriture.dump(score)
        data.close()
    return score

# Enregistrer le score dans le fichier 'score'
# Prend en paramètre le dictionnaire des scores
def save_score(score):
    data = open(donnees.score_file, "wb")
    ecriture = pickle.Pickler(data)
    ecriture.dump(score)
    data.close()


# Piocher un mot au hasard (random.choice(my_list)) dans la LISTE 'liste_mots'
def mot_choisi():
    mot = random.choice(donnees.liste_mots)
    return mot

# Réupère une lettre saisie par le joueur
def done_letters():
    lettre = input("Saisi une lettre que tu pense être dans le mot : ")
    lettre = lettre.lower()
    return lettre

# Récupère le mot (en: word) masqué return mot_masque
# Cacher les lettres du mot à trouver par '*'
def done_word(mot_complet, lettres_trouvées):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvées:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque