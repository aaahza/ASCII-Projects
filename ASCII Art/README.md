
---

# ASCII Art Display using Pygame

This Python script converts an image into ASCII art and displays it using Pygame in fullscreen mode.

## Requirements

- Python 3.x
- Pygame
- PIL (Python Imaging Library)

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install Pygame and PIL using pip:

   ```bash
   pip install pygame pillow
   ```

## Usage

1. Place your desired image file (e.g., `eye.jpeg`) in the same directory as the script.
2. Run the script:

   ```bash
   python ascii_art_display.py
   ```

3. The script will display the ASCII representation of the image on your screen.

## Configuration

- Adjust the `ASCII_CHARS` variable in the script to modify the characters used for ASCII art representation.
- Fine-tune the `max_width` and `max_height` variables to control the resolution of the ASCII art displayed on your screen.

## Controls

- Press `ESC` key to exit the program.

## Notes

- Ensure the image file (`eye.jpeg` in the example) exists in the same directory as the script.
- The script resizes the image to fit the screen while maintaining aspect ratio.
- ASCII characters used can be customized for different visual effects.

---

Feel free to customize and expand this README according to your specific needs or additional features of the script!
