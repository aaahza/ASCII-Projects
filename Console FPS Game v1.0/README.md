# Console Game v1.0

This project demonstrates a simple raycasting engine implemented in C++ that renders a 3D-like scene in a console window.

## Overview

The program uses raycasting techniques to simulate a 3D environment within the constraints of a console window. It renders walls, floors, and ceilings based on a map defined in the code. The player can move within the map and rotate the view using keyboard input.

## Features

- Raycasting rendering of walls with different shading based on distance.
- Dynamic movement and rotation of the player.
- Floor and ceiling rendering based on player's view angle.
- Real-time statistics display including player position, angle, and FPS.

## Controls

- **W**: Move forward.
- **S**: Move backward.
- **A**: Rotate counter-clockwise.
- **D**: Rotate clockwise.

## Dependencies

- Windows.h: Required for Windows console functions.
- chrono: For time measurement and frame rate control.
- vector, algorithm: Standard C++ library for data structures and algorithms.

## How to Run

1. **Compile**: Use a C++ compiler that supports C++11 or later (e.g., g++, Visual Studio).
   
   Example for g++:
   ```
   g++ -o raycaster raycaster.cpp
   ```

2. **Run**: Execute the compiled binary.

   Example for Windows:
   ```
   raycaster.exe
   ```

## Configuration

- **Screen Dimensions**: Adjust `nScreenWidth` and `nScreenHeight` for desired console size.
- **Map Dimensions**: Modify `nMapWidth` and `nMapHeight` to change the size of the map.
- **Player Start Position and Angle**: Update `fPlayerX`, `fPlayerY`, and `fPlayerAngle` to change where and how the player starts.

## Notes

- Ensure the console window size is sufficient to display the entire screen (`nScreenWidth` x `nScreenHeight`).
- The rendering performance may vary depending on the hardware and console window size.
