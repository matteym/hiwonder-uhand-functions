#!/usr/bin/python3
# coding=utf8
"""
Script "Titten" : Mouvement de pressage double avec la main uHandPi et le buzzer.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# Mapping des servos
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    
    # Positions
    OPEN = [[THUMB, 1200], [INDEX, 1800], [MIDDLE, 1800], [RING, 1800], [PINKY, 1800], [WRIST, 1500]]
    CLOSED = [[THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]]

    try:
        print("Titten ! (Ctrl+C pour arrêter)")
        
        # Position initiale ouverte
        board.pwm_servo_set_position(0.3, OPEN)
        time.sleep(0.5)

        while True:
            # Double pressage en boucle
            for _ in range(2):
                # Fermeture (Pressage) + Son
                board.pwm_servo_set_position(0.15, CLOSED)
                board.set_buzzer(2000, 0.1, 0.9, 1)
                time.sleep(0.2)
                
                # Ouverture
                board.pwm_servo_set_position(0.15, OPEN)
                time.sleep(0.2)
            
            # Pause entre chaque séquence
            time.sleep(1.0)

    except KeyboardInterrupt:
        # Remise à plat propre
        board.pwm_servo_set_position(0.5, [[1, 1500], [2, 1500], [3, 1500], [4, 1500], [5, 1500], [6, 1500]])
        print("\nArrêt.")
        sys.exit(0)

if __name__ == '__main__':
    main()
EOFcat << 'EOF' > titten.py
#!/usr/bin/python3
# coding=utf8
"""
Script "Titten" : Mouvement de pressage double avec la main uHandPi et le buzzer.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# Mapping des servos
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    
    # Positions
    OPEN = [[THUMB, 1200], [INDEX, 1800], [MIDDLE, 1800], [RING, 1800], [PINKY, 1800], [WRIST, 1500]]
    CLOSED = [[THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]]

    try:
        print("Titten ! (Ctrl+C pour arrêter)")
        
        # Position initiale ouverte
        board.pwm_servo_set_position(0.3, OPEN)
        time.sleep(0.5)

        while True:
            # Double pressage en boucle
            for _ in range(2):
                # Fermeture (Pressage) + Son
                board.pwm_servo_set_position(0.15, CLOSED)
                board.set_buzzer(2000, 0.1, 0.9, 1)
                time.sleep(0.2)
                
                # Ouverture
                board.pwm_servo_set_position(0.15, OPEN)
                time.sleep(0.2)
            
            # Pause entre chaque séquence
            time.sleep(1.0)

    except KeyboardInterrupt:
        # Remise à plat propre
        board.pwm_servo_set_position(0.5, [[1, 1500], [2, 1500], [3, 1500], [4, 1500], [5, 1500], [6, 1500]])
        print("\nArrêt.")
        sys.exit(0)

if __name__ == '__main__':
    main()
EOFcat << 'EOF' > titten.py
#!/usr/bin/python3
# coding=utf8
"""
Script "Titten" : Mouvement de pressage double avec la main uHandPi et le buzzer.
"""
import sys
import time

sys.path.append('/home/pi/uhandpi/common_sdk')
from common.ros_robot_controller_sdk import Board

# Mapping des servos
THUMB, INDEX, MIDDLE, RING, PINKY, WRIST = 1, 2, 3, 4, 5, 6

def main():
    board = Board()
    
    # Positions
    OPEN = [[THUMB, 1200], [INDEX, 1800], [MIDDLE, 1800], [RING, 1800], [PINKY, 1800], [WRIST, 1500]]
    CLOSED = [[THUMB, 1800], [INDEX, 1200], [MIDDLE, 1200], [RING, 1200], [PINKY, 1200], [WRIST, 1500]]

    try:
        print("Titten ! (Ctrl+C pour arrêter)")
        
        # Position initiale ouverte
        board.pwm_servo_set_position(0.3, OPEN)
        time.sleep(0.5)

        while True:
            # Double pressage en boucle
            for _ in range(2):
                # Fermeture (Pressage) + Son
                board.pwm_servo_set_position(0.15, CLOSED)
                board.set_buzzer(2000, 0.1, 0.9, 1)
                time.sleep(0.2)
                
                # Ouverture
                board.pwm_servo_set_position(0.15, OPEN)
                time.sleep(0.2)
            
            # Pause entre chaque séquence
            time.sleep(1.0)

    except KeyboardInterrupt:
        # Remise à plat propre
        board.pwm_servo_set_position(0.5, [[1, 1500], [2, 1500], [3, 1500], [4, 1500], [5, 1500], [6, 1500]])
        print("\nArrêt.")
        sys.exit(0)

if __name__ == '__main__':
    main()
