#!/usr/init/python3
# coding=utf8
"""
Pipeline automatique : Salut -> Rock and Roll -> Rock and Roll Moving
"""
import subprocess
import time
import sys

# Liste des scripts (comme on est dans 'others', on appelle directement les fichiers du dossier)
scripts_sequence = [
    ("salut.py", 8),
    ("rock_and_roll.py", 8),
    ("rock_and_roll_moving.py", 8)
]

def main():
    print("=== Démarrage de la pipeline automatique Salut & Rock ===")
    try:
        for script, duration in scripts_sequence:
            print(f"\n--> Lancement de : {script} (pour {duration} secondes)")
            
            # Lancement du script
            process = subprocess.Popen(["python3", script])
            
            # Attente
            time.sleep(duration)
            
            # Arrêt propre pour passer au suivant
            process.terminate()
            process.wait()
            
            time.sleep(0.5)
            
        print("\n=== Pipeline automatique terminée avec succès ! ===")

    except KeyboardInterrupt:
        print("\nArrêt d'urgence de la pipeline.")
        try:
            process.terminate()
        except:
            pass
        sys.exit(0)

if __name__ == '__main__':
    main()
