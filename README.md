# Clash of Clans Automation Script

This Python script automates troop training and base attacks in the game "Clash of Clans" using computer vision and automation libraries.

## Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (version 3.x recommended)
- Required Python packages: `mss`, `cv2`, `screeninfo`, `time`, `pyautogui`

You can install the necessary packages using the following command:

```bash
pip install mss opencv-python screeninfo pyautogui
```

## Usage

1. Clone or download this repository to your local machine.

2. Ensure the game window is visible on your screen (BlueStacks).

3. Run the script:

```bash
python clash_of_clans_script.py
```

4. The script will take control of your mouse and perform the following actions:

   - Open Barracks
   - Open Troop Training
   - Train Barbarians for 60 times
   - Close troop training
   - Start a matchmaking session
   - Open Attack menu
   - Deploy troops for 60 times
   - Go back to the main screen

5. Adjust the timings in the script according to your game's responsiveness.

## Notes

- This script uses computer vision techniques to locate and interact with in-game elements. Ensure the game window is visible and undisturbed during script execution.

- The provided template images (`Barracks.png`, `Train_troops.png`, etc.) should match the in-game elements for successful automation. You may need to update these images if the game interface changes.

- Use this script responsibly and in compliance with the game's terms of service. Unauthorized automation may result in account suspension.

## Disclaimer

This script is for educational and informational purposes only. The author is not responsible for any consequences arising from the use of this script. Use it at your own risk.

---
