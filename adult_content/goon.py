#!/usr/init/python3
# coding=utf8
"""
Chorégraphie : Main tendue, pouce ajusté, vague subtile des doigts,
et micro-oscillations infinies du poignet jusqu'à Ctrl+C.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    print("Lancement de la chorégraphie finale... (Ctrl+C pour arrêter)")

    try:
        while True:
            # --- ÉTAPE 1 : Position initiale ---
            print("Position initiale : Main tendue, poignet à droite...")
            initial_pos = [
                [THUMB,  1300],  # Pouce initial un peu moins ouvert
                [INDEX,  2200],  # Tendu
                [MIDDLE, 2200],  # Tendu
                [RING,   2200],  # Tendu
                [PINKY,  2200],  # Tendu
                [WRIST,  2500],  # Poignet max à droite
            ]
            board.pwm_servo_set_position(1.0, initial_pos)
            time.sleep(1.5)

            # --- ÉTAPE 2 : Baisse en vague très subtile (doigts + pouce plus léger) ---
            print("Baisse en vague ultra-subtile...")
            
            # Petit doigt + léger mouvement du pouce
            board.pwm_servo_set_position(0.3, [[PINKY, 1350], [THUMB, 1400]])
            time.sleep(0.15)

            print("Annulaire...")
            board.pwm_servo_set_position(0.3, [[RING, 1350]])
            time.sleep(0.15)

            print("Majeur...")
            board.pwm_servo_set_position(0.3, [[MIDDLE, 1350]])
            time.sleep(0.15)

            print("Index...")
            board.pwm_servo_set_position(0.3, [[INDEX, 1350]])
            time.sleep(0.5)

            # --- ÉTAPE 3 : Mouvement gauche/droite infini du poignet ---
            print("Oscillations continues du poignet... (Fais Ctrl+C pour arrêter)")
            while True:
                board.pwm_servo_set_position(0.08, [[WRIST, 2350]])
                time.sleep(0.08)
                board.pwm_servo_set_position(0.08, [[WRIST, 2650]])
                time.sleep(0.08)

    except KeyboardInterrupt:
        print("\nArrêt du script – Remise au neutre des moteurs.")
        safe_pos = [[i, 1500] for i in range(1, 7)]
        board.pwm_servo_set_position(0.5, safe_pos)
        sys.exit(0)

if __name__ == '__main__':
    main()
