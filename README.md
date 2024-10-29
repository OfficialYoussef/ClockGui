# Digital Clock with Day/Night Mode Toggle

This Python program creates a digital clock GUI with a toggle button to switch between day and night modes. Built using the `tkinter` library, the clock displays the current time and allows users to switch themes seamlessly.

## Features

- **Digital Clock Display**: The main display shows the current time in a large, easy-to-read font.
- **Day/Night Theme Toggle**: A button allows the user to switch between light (day) and dark (night) themes.
- **Automatic Time Update**: The clock updates every second to keep the displayed time accurate.

## Code Components
![Screenshot from 2024-10-29 10-49-24](https://github.com/user-attachments/assets/38646126-958e-4e8f-9284-743d6e201821)

1. **Imports**:
   - `time`: Used for retrieving the current time.
   - `os`: Used for file path handling.
   - `tkinter`: The GUI library for creating the clock display and toggle button.

2. **Main Window Setup**:
   - Creates a `Tk` window titled `Clock` with a unique icon (`digital-clock.png`).
   - Sets the initial background to light mode with a light purple color (`#9381FF`).

3. **Clock Label**:
   - The time display is a large label (`Lbel`) with custom fonts and colors, updated every 100 milliseconds.

4. **Theme Toggle**:
   - A `Button` widget (`switch`) allows switching between day (light) and night (dark) modes.
   - Clicking the button updates the background color and button icon based on the `switch_value` (True for light mode, False for dark mode).

## How to Use
![Screenshot from 2024-10-29 10-49-19](https://github.com/user-attachments/assets/baabf00b-5ecd-4bf7-819c-9304499a3e9e)
### `font.ttf`: Install font on your laptop
1. Ensure the following images are in an `img` folder within the working directory:
   - `digital-clock.png`: Clock icon
   - `sun(1).png`: Icon for light mode
   - `sun(3).png`: Icon for dark mode
   
2. Run the script. The digital clock will appear with the current time and an icon in the top left for theme toggling.

3. Click the icon to switch between day and night themes.

## Example Usage

```python
python digital_clock.py
