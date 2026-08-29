
#!/usr/bin/python3
# coding=utf8
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# Mapping
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    
    try:
        print("Séquence Pointage & Pressage lancée...")

        # --- PARTIE 1 : POINTAGE ---
        # Index à fond (1800), pouce un peu replié (1600), autres doigts repliés (1200)
        # On fait gauche (1800) -> droite (1200)
        print("Phase Pointage")
        for pos_wrist in [1800, 1200]:
            board.pwm_servo_set_position(0.5, [
                [THUMB, 1600], [INDEX, 1800], [MIDDLE, 1200], 
                [RING, 1200], [PINKY, 1200], [WRIST, pos_wrist]
            ])
            time.sleep(1.0)

        # --- PARTIE 2 : PRESSAGE ---
        print("Phase Pressage")
        OPEN = [[THUMB, 1200], [INDEX, 1800], [MIDDLE, 1800], [RING, 1800], [PINKY, 1800], [WRIST, 1500]]
        CLOSED = [[THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]]

        for _ in range(2):
            # Ouvrir
            board.pwm_servo_set_position(0.3, OPEN)
            time.sleep(0.4)
            # Fermer (presser)
            board.pwm_servo_set_position(0.3, CLOSED)
            time.sleep(0.4)

    except KeyboardInterrupt:
        pass
    finally:
        # Remise à plat
        board.pwm_servo_set_position(0.5, [[1, 1500], [2, 1500], [3, 1500], [4, 1500], [5, 1500], [6, 1500]])
        sys.exit(0)

if __name__ == '__main__':
    main()
EOF
