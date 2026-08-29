#!/usr/bin/python3
# coding=utf8
"""
Geste "deux doigts du milieu" (majeur + annulaire) qui montent et descendent ensemble.
Le poignet (servo 6) bouge de gauche à droite.
Les autres doigts sont légèrement ouverts pour un rendu plus naturel.
Accélération progressive et douce, mais plus rapide qu'avant.
"""

import sys
import time
import random

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# --- Mapping ---
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

# Positions
CURL = {
    THUMB: 1800,
    INDEX: 1200,
    MIDDLE: 1200,
    RING: 1200,
    PINKY: 1200,
}

EXTEND = {
    THUMB: 900,
    INDEX: 1900,
    MIDDLE: 1900,
    RING: 1900,
    PINKY: 1900,
}

# Positions intermédiaires (légèrement ouvertes)
SEMI = {
    THUMB: 1400,   # un peu ouvert
    INDEX: 1450,   # légèrement déplié
    PINKY: 1450,   # légèrement déplié
}

# Positions poignet
WRIST_LEFT   = 1200
WRIST_RIGHT  = 1800
WRIST_NEUTRAL = 1500


def set_positions(board, positions, duration):
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)


def set_two_middle_fingers(board, up=True, wrist_pos=WRIST_NEUTRAL, duration=0.20):
    """
    Majeur + Annulaire qui montent/descendent.
    Les autres doigts restent légèrement ouverts.
    Le poignet est positionné selon wrist_pos.
    """
    middle_pos = EXTEND[MIDDLE] if up else CURL[MIDDLE]
    ring_pos   = EXTEND[RING]   if up else CURL[RING]

    positions = [
        [THUMB,  SEMI[THUMB]],
        [INDEX,  SEMI[INDEX]],
        [MIDDLE, middle_pos],
        [RING,   ring_pos],
        [PINKY,  SEMI[PINKY]],
        [WRIST,  wrist_pos],
    ]
    set_positions(board, positions, duration)


def main():
    board = Board()
    try:
        print("Position de départ...")
        set_two_middle_fingers(board, up=False, wrist_pos=WRIST_NEUTRAL, duration=0.4)
        time.sleep(0.5)

        print("Début du mouvement – poignet gauche/droite + doigts plus rapides (Ctrl+C pour arrêter)")

        # Durées plus courtes = mouvements plus rapides
        start_duration = 0.28
        end_duration   = 0.08
        total_cycles   = 70

        for i in range(total_cycles):
            progress = i / (total_cycles - 1)
            ease = progress * progress  # accélération progressive
            duration = start_duration - (start_duration - end_duration) * ease
            duration *= random.uniform(0.93, 1.07)

            # Alterne le poignet gauche / droite à chaque cycle
            wrist_pos = WRIST_LEFT if (i % 2 == 0) else WRIST_RIGHT

            # Monte
            set_two_middle_fingers(board, up=True, wrist_pos=wrist_pos, duration=duration)
            # Descend
            set_two_middle_fingers(board, up=False, wrist_pos=wrist_pos, duration=duration)

            # Petite pause aléatoire de temps en temps
            if i > 8 and i % random.randint(9, 14) == 0:
                time.sleep(random.uniform(0.06, 0.15))

        print("Fin – retour position neutre...")
        set_two_middle_fingers(board, up=False, wrist_pos=WRIST_NEUTRAL, duration=0.4)
        time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nArrêt demandé.")
        set_two_middle_fingers(board, up=False, wrist_pos=WRIST_NEUTRAL, duration=0.3)
    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
