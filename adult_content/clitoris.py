#!/usr/bin/python3
# coding=utf8
"""
Stimulation réaliste avec l'index pour uHandPi.
- Descente lente
- Remontée plus rapide
- Variations de profondeur, de rythme et de pauses
"""

import sys
import time
import random

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

CURL = {
    THUMB: 1800,
    INDEX: 1200,
    MIDDLE: 1200,
    RING: 1200,
    PINKY: 1200,
}

EXTEND = {
    THUMB: 900,
    INDEX: 1850,
    MIDDLE: 1200,
    RING: 1200,
    PINKY: 1200,
}

WRIST_NEUTRAL = 1500
WRIST_IN      = 1220   # plus profond
WRIST_OUT     = 1780

# Positions de l'index
INDEX_DEEP     = 1920
INDEX_MEDIUM   = 1820
INDEX_SHALLOW  = 1720

def set_positions(board, positions, duration):
    board.pwm_servo_set_position(duration, positions)
    time.sleep(duration)

def set_base_gesture(board, duration=0.45):
    positions = [
        [THUMB,  CURL[THUMB]],
        [INDEX,  EXTEND[INDEX]],
        [MIDDLE, CURL[MIDDLE]],
        [RING,   CURL[RING]],
        [PINKY,  CURL[PINKY]],
        [WRIST,  WRIST_NEUTRAL],
    ]
    set_positions(board, positions, duration)

def stroke(board, depth="deep", down_speed=0.32, up_speed=0.18):
    """
    Un cycle réaliste :
    - Descente lente
    - Petite pause en bas (parfois)
    - Remontée plus rapide
    """
    if depth == "deep":
        index_pos = INDEX_DEEP
        wrist_in  = WRIST_IN
    elif depth == "medium":
        index_pos = INDEX_MEDIUM
        wrist_in  = 1320
    else:  # shallow
        index_pos = INDEX_SHALLOW
        wrist_in  = 1420

    # === Descente (lente) ===
    positions_down = [
        [THUMB,  CURL[THUMB]],
        [INDEX,  index_pos],
        [MIDDLE, CURL[MIDDLE]],
        [RING,   CURL[RING]],
        [PINKY,  CURL[PINKY]],
        [WRIST,  wrist_in],
    ]
    set_positions(board, positions_down, down_speed)

    # Petite pause en bas (aléatoire)
    if random.random() < 0.35:
        time.sleep(random.uniform(0.08, 0.22))

    # === Remontée (plus rapide) ===
    positions_up = [
        [THUMB,  CURL[THUMB]],
        [INDEX,  INDEX_SHALLOW],
        [MIDDLE, CURL[MIDDLE]],
        [RING,   CURL[RING]],
        [PINKY,  CURL[PINKY]],
        [WRIST,  WRIST_OUT],
    ]
    set_positions(board, positions_up, up_speed)

def main():
    board = Board()
    try:
        print("Position de départ...")
        set_base_gesture(board)
        time.sleep(0.9)

        print("Début de la stimulation réaliste (Ctrl+C pour arrêter)...")

        # ===== Phase 1 : très lent et doux =====
        for _ in range(5):
            stroke(board, depth="shallow", down_speed=0.42, up_speed=0.28)
            time.sleep(random.uniform(0.05, 0.15))

        # ===== Phase 2 : rythme moyen + variations =====
        for i in range(12):
            depth = random.choice(["shallow", "medium", "deep", "medium"])
            down = random.uniform(0.28, 0.38)
            up   = random.uniform(0.16, 0.24)
            stroke(board, depth=depth, down_speed=down, up_speed=up)

            if random.random() < 0.25:
                time.sleep(random.uniform(0.12, 0.30))  # pause irrégulière

        # ===== Phase 3 : plus intense et irrégulier =====
        for i in range(14):
            depth = random.choice(["deep", "deep", "medium"])
            down = random.uniform(0.22, 0.32)
            up   = random.uniform(0.12, 0.20)
            stroke(board, depth=depth, down_speed=down, up_speed=up)

            # Parfois double coup rapide
            if random.random() < 0.18:
                stroke(board, depth="medium", down_speed=0.15, up_speed=0.12)

        # ===== Phase 4 : ralentissement final =====
        for _ in range(4):
            stroke(board, depth="shallow", down_speed=0.40, up_speed=0.30)
            time.sleep(0.15)

        print("Retour position neutre...")
        set_base_gesture(board, duration=0.6)
        time.sleep(0.4)

        # Tout replié
        positions_rest = [
            [THUMB,  CURL[THUMB]],
            [INDEX,  CURL[INDEX]],
            [MIDDLE, CURL[MIDDLE]],
            [RING,   CURL[RING]],
            [PINKY,  CURL[PINKY]],
            [WRIST,  WRIST_NEUTRAL],
        ]
        set_positions(board, positions_rest, 0.5)

    except KeyboardInterrupt:
        print("\nArrêt demandé.")
        set_base_gesture(board, duration=0.4)

    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
