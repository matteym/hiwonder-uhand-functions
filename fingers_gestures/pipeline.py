#!/usr/bin/python3
# coding=utf8
"""
Pipeline automatique : Enchaîne les gestes de doigts pendant un temps défini.
"""
import subprocess
import time
import sys

# Liste des scripts avec leur durée d'exécution en secondes avant de passer au suivant
scripts_sequence = [
    ("middle_finger_brutal.py", 6),
    ("middle_finger_street.py", 6),
    ("middle_finger_brutal_180.py", 6),
    ("middle_finger_street_180.py", 6),
]

def main():
    print("=== Démarrage de la pipeline automatique de doigts ===")
    process = None
    try:
        for script, duration in scripts_sequence:
            print(f"\n--> Lancement de : {script} (pour {duration} secondes)")
            
            # Lance le script en arrière-plan
            process = subprocess.Popen(["python3", script])
            
            # Attend le temps imparti
            time.sleep(duration)
            
            # Arrête proprement le script en cours pour passer au suivant
            process.terminate()
            process.wait()
            
            time.sleep(0.5)
            
        print("\n=== Pipeline de doigts terminée avec succès ! ===")

    except KeyboardInterrupt:
        print("\nArrêt d'urgence de la pipeline.")
        if process:
            try:
                process.terminate()
            except:
                pass
        sys.exit(0)

if __name__ == '__main__':
    main()
