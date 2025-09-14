import random

# Historique des choix du joueur
historique = []

# Contre-coup : ce qui bat chaque coup
contre = {
    "Pierre": "Papier",
    "Papier": "Ciseaux",
    "Ciseaux": "Pierre"
}

# Fonction IA : prédire le prochain coup du joueur
def prediction_ia(historique):
    if not historique:
        return random.choice(["Pierre", "Papier", "Ciseaux"])
    
    # Compter les fréquences des coups précédents
    freq = {"Pierre": 0, "Papier": 0, "Ciseaux": 0}
    for coup in historique:
        freq[coup] += 1
    
    # Deviner le coup le plus probable du joueur
    coup_probable = max(freq, key=freq.get)
    return contre[coup_probable]  # L’ordi joue le contre

# Fonction principale du jeu
def jouer():
    print("Bienvenue dans Pierre-Papier-Ciseaux avec IA ! (tape 'stop' pour quitter)")
    while True:
        joueur = input("Ton choix (Pierre, Papier, Ciseaux) : ").capitalize()
        if joueur == "Stop":
            print("Merci d’avoir joué !")
            break
        if joueur not in ["Pierre", "Papier", "Ciseaux"]:
            print("Choix invalide. Réessaie.")
            continue

        ia = prediction_ia(historique)
        print(f"L’IA joue : {ia}")

        if joueur == ia:
            print("Égalité !")
        elif contre[joueur] == ia:
            print("Tu gagnes 🎉 !")
        else:
            print("L’IA gagne 🤖 !")

        historique.append(joueur)

# Lancer le jeu
jouer()