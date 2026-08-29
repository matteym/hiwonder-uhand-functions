#!/usr/init/python3
# coding=utf8
"""
Chorégraphie 'Au revoir' : Un seul mouvement fluide et continu.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    
    TENDU = 2000
    LEGER_DETENDU = 1750

    print("Chorégraphie 'Au revoir' fluide lancée ! (Ctrl+C pour arrêter)")
    try:
        while True:
            # 1. Position initiale : Poignet à gauche (1800) + Doigts tendus
            board.pwm_servo_set_position(0.5, [
                [THUMB, 1200], [INDEX, TENDU], [MIDDLE, TENDU], 
                [RING, TENDU], [PINKY, TENDU], [WRIST, 1800]
            ])
            time.sleep(0.5)

            # 2. Passage du poignet vers la droite (1200) en effectuant la petite vague des doigts
            board.pwm_servo_set_position(0.6, [[WRIST, 1200]])
            
            # Vague légère en cascade pendant que le poignet bouge
            time.sleep(0.1)
            board.pwm_servo_set_position(0.15, [[PINKY, LEGER_DETENDU]])
            time.sleep(0.15)
            board.pwm_servo_set_position(0.15, [[RING, LEGER_DETENDU]])
            time.sleep(0.15)
            board.pwm_servo_set_position(0.15, [[MIDDLE, LEGER_DETENDU]])
            time.sleep(0.15)
            board.pwm_servo_set_position(0.15, [[INDEX, LEGER_DETENDU]])
            time.sleep(0.4)

            # 3. Retour propre au centre (1500) en retendant les doigts
            board.pwm_servo_set_position(0.5, [
                [THUMB, 1200], [INDEX, TENDU], [MIDDLE, TENDU], 
                [RING, TENDU], [PINKY, TENDU], [WRIST, 1500]
            ])
            time.sleep(1.05) # Petite pause avant de recommencer un coucou propre

    except KeyboardInterrupt:
        board.pwm_servo_set_position(0.5, [[i, 1500] for i in range(1, 7)])
        print("\nArrêt de l'au revoir.")
        sys.exit(0)

if __name__ == '__main__':
    main()
