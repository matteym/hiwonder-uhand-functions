hiwonder-uhand-functions
Custom and open-source Python functions for the Hiwonder uHandPi robotic hand.

Contributing
Contributions are welcome! Feel free to open a Pull Request to add new gestures or improve existing functions. Please ensure your files are placed in the appropriate directories.

Raspberry Pi Connection Guide
1. Connect the Hand / Network
Ethernet cable: Plug it directly into the robot to establish the initial connection.

Wi-Fi network (from your computer): Connect to HW-...

Wi-Fi Password: hiwonder

2. SSH Connection
Open your terminal and connect to the robot via SSH:

Bash
ssh pi@192.168.149.1
SSH Password: raspberrypi

How to Clone This Repository
Navigate to the functions directory and clone the repository:

Go to the target directory:

Bash
cd uhandpi/functions
Clone the repository using SSH:

Bash
git clone git@github.com:matteym/hiwonder-uhand-functions.git
(Note: If you haven't set up an SSH key on your robot yet, you can use HTTPS instead: git clone [https://github.com/matteym/hiwonder-uhand-functions.git](https://github.com/matteym/hiwonder-uhand-functions.git))

Navigate into the project folder:

Bash
cd hiwonder-uhand-functions
Setup and Connection Script (connect.sh)
To initialize or connect everything using the provided script, run:

Bash
chmod +x connect.sh
bash connect.sh
Folders Directory Structure
Project files are organized under the following directories:

adult_content/ — Freaky gestures, adult content, etc.

fingers_gestures/ — Middle fingers and hand sign variations.

others/ — Rock 'n' roll, greetings, and miscellaneous functions.