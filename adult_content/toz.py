#!/usr/bin/python3
# coding=utf8
"""
Geste "Toz" séquentiel pour uHandPi avec boucle de battement du majeur.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# Mapping des servos
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    try:
        # 1. Position de repos (fermé)
        board.pwm_servo_set_position(0.3, [
            [THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]
        ])
        time.sleep(0.4)

        # 2. Étape 1 : On déplie TOUS les doigts en entier (main ouverte)
        board.pwm_servo_set_position(0.4, [
            [THUMB,  1200],  
            [INDEX,  1800],  
            [MIDDLE, 1800],  
            [RING,   1800],  
            [PINKY,  1800],  
            [WRIST,  1500]
        ])
        time.sleep(1)  

        # 3. Étape 2 : On replie uniquement le majeur pour faire le "toz"
        board.pwm_servo_set_position(0.3, [
            [THUMB,  1200],  
            [INDEX,  1800],  
            [MIDDLE, 1200],  # Replié à 1200
            [RING,   1800],  
            [PINKY,  1800],  
            [WRIST,  1500]
        ])
        time.sleep(0.5)  

        # 4. Étape 3 : Le majeur se relève et se rebaisse de 40 en boucle
        print("Battement du majeur (Ctrl+C pour arrêter)...")
        while True:
            # Relever de 40 (1200 + 40 = 1240)
            board.pwm_servo_set_position(0.15, [[MIDDLE, 1240]])
            time.sleep(0.25)
            
            # Rebaisser de 40 (retour à 1200)
            board.pwm_servo_set_position(0.15, [[MIDDLE, 1200]])
            time.sleep(0.25)

    except KeyboardInterrupt:
        # Retour position neutre propre à l'arrêt
        board.pwm_servo_set_position(0.5, [
            [THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]
        ])
        pass
    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
