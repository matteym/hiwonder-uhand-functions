#!/usr/bin/python3
# coding=utf8
"""
Script d'enchaînement : Titten -> Clitoris -> Fingering -> Toz
Fais Ctrl+C pour passer au script suivant ou arrêter le show.
"""
import subprocess
import time
import sys
import signal

scripts_sequence = [
    "titten.py",
    "clitoris.py",
    "fingering.py",
    "toz.py"
]

def main():
    print("=== Démarrage du show complet ===")
    print("(Appuie sur Ctrl+C pour passer au script suivant)")
    
    try:
        for script in scripts_sequence:
            print(f"\n--> Exécution de : {script} (En cours... Fais Ctrl+C pour avancer)")
            
            # Lance le script
            process = subprocess.Popen(["python3", script])
            
            try:
                # Attend que le script se termine (ou que tu fasses Ctrl+C)
                process.wait()
            except KeyboardInterrupt:
                # Quand tu fais Ctrl+C, on arrive ici : 
                # On arrête le script en cours proprement
                print(f"\n[Interruption] Passage au script suivant...")
                process.terminate()
                process.wait()
                # Petite pause pour laisser le temps aux moteurs de respirer
                time.sleep(0.5)
                continue

            time.sleep(1.0)

        print("\n=== Show terminé avec succès ! ===")

    except KeyboardInterrupt:
        print("\nFin définitive du pipeline.")
        sys.exit(0)

if __name__ == '__main__':
    main()
