#!/usr/bin/python3
# coding=utf8
"""
Geste "rock and roll" (cornes) pour uHandPi
+ balancement de la main de gauche à droite en même temps.

Index + auriculaire tendus, pouce/majeur/annulaire repliés.
Le poignet oscille gauche ↔ droite pendant le geste.
"""

import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# --- Mapping servo -> doigt ---
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

CURL = {
    THUMB: 1800,   # replié (sens inversé)
    INDEX: 1200,
    MIDDLE: 1200,
    RING: 1200,
    PINKY: 1200,
}

EXTEND = {
    THUMB: 900,    # tendu (sens inversé)
    INDEX: 1900,
    MIDDLE: 1800,
    RING: 1800,
    PINKY: 1800,
}

# Positions poignet pour le balancement gauche/droite
WRIST_LEFT   = 1200
WRIST_RIGHT  = 1800
WRIST_NEUTRAL = 1500

DURATION = 0.35          # vitesse du balancement (plus petit = plus rapide)

def set_rock_and_roll(board, wrist_pos, duration=DURATION):
    """Pose le geste rock and roll avec une position de poignet donnée."""
    positions = [
        [THUMB,  EXTEND[THUMB]],   # pouce légèrement tendu (comme ton original)
        [INDEX,  EXTEND[INDEX]],
        [MIDDLE, CURL[MIDDLE]],
        [RING,   CURL[RING]],
        [PINKY,  EXTEND[PINKY]],
        [WRIST,  wrist_pos],
    ]
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)

def main():
    board = Board()
    try:
        print("Position de départ...")
        # Tout replié, poignet neutre
        positions_rest = [
            [THUMB, CURL[THUMB]],
            [INDEX, CURL[INDEX]],
            [MIDDLE, CURL[MIDDLE]],
            [RING, CURL[RING]],
            [PINKY, CURL[PINKY]],
            [WRIST, WRIST_NEUTRAL],
        ]
        board.pwm_servo_set_position(0.4, positions_rest)
        time.sleep(0.5)

        print("Rock and roll + balancement gauche/droite (Ctrl+C pour arrêter)")

        # Boucle de balancement
        while True:
            # Gauche
            set_rock_and_roll(board, WRIST_LEFT)
            # Droite
            set_rock_and_roll(board, WRIST_RIGHT)

    except KeyboardInterrupt:
        print("\nArrêt demandé – retour position neutre")
        set_rock_and_roll(board, WRIST_NEUTRAL, duration=0.4)
        time.sleep(0.3)

        # Tout replié
        positions_rest = [
            [THUMB, CURL[THUMB]],
            [INDEX, CURL[INDEX]],
            [MIDDLE, CURL[MIDDLE]],
            [RING, CURL[RING]],
            [PINKY, CURL[PINKY]],
            [WRIST, WRIST_NEUTRAL],
        ]
        board.pwm_servo_set_position(0.4, positions_rest)
        time.sleep(0.3)

    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
