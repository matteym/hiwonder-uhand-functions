#!/usr/bin/python3
# coding=utf8
"""
Geste "deux doigts du milieu" (majeur + annulaire)
qui montent et descendent ensemble.
Les autres doigts sont légèrement ouverts pour un rendu plus naturel.
Accélération progressive et douce.
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

# Positions intermédiaires (légèrement ouvertes) pour un rendu plus naturel
SEMI = {
    THUMB: 1400,   # un peu ouvert
    INDEX: 1450,   # légèrement déplié
    PINKY: 1450,   # légèrement déplié
}

WRIST_NEUTRAL = 1500

def set_positions(board, positions, duration):
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)

def set_two_middle_fingers(board, up=True, duration=0.30):
    """
    Majeur + Annulaire qui montent/descendent.
    Les autres doigts restent légèrement ouverts.
    """
    middle_pos = EXTEND[MIDDLE] if up else CURL[MIDDLE]
    ring_pos   = EXTEND[RING]   if up else CURL[RING]

    positions = [
        [THUMB,  SEMI[THUMB]],
        [INDEX,  SEMI[INDEX]],
        [MIDDLE, middle_pos],
        [RING,   ring_pos],
        [PINKY,  SEMI[PINKY]],
        [WRIST,  WRIST_NEUTRAL],
    ]
    set_positions(board, positions, duration)

def main():
    board = Board()
    try:
        print("Position de départ...")
        set_two_middle_fingers(board, up=False, duration=0.5)
        time.sleep(0.7)

        print("Début du mouvement – accélération douce (Ctrl+C pour arrêter)")

        start_duration = 0.45
        end_duration   = 0.11
        total_cycles   = 70

        for i in range(total_cycles):
            progress = i / (total_cycles - 1)
            ease = progress * progress          # accélération progressive
            duration = start_duration - (start_duration - end_duration) * ease
            duration *= random.uniform(0.93, 1.07)

            # Monte
            set_two_middle_fingers(board, up=True, duration=duration)

            # Descend
            set_two_middle_fingers(board, up=False, duration=duration)

            if i > 8 and i % random.randint(9, 14) == 0:
                time.sleep(random.uniform(0.08, 0.22))

        print("Fin – retour position neutre...")
        set_two_middle_fingers(board, up=False, duration=0.5)
        time.sleep(0.4)

    except KeyboardInterrupt:
        print("\nArrêt demandé.")
        set_two_middle_fingers(board, up=False, duration=0.4)

    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
