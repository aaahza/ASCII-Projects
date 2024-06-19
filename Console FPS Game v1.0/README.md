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

To run this project, follow these steps:

1. **Load Project Files**: Open the project folder in Visual Studio or your preferred IDE.
   
2. **Compile and Build**: Build the project to compile all source files together.
   
3. **Run the Project**: Execute the compiled binary within the IDE's environment or locate the executable file in the project directory and run it directly.

For Visual Studio:
- Open Visual Studio.
- Load the entire project folder into Visual Studio.
- Build the project to compile all source files.
- Run the project using Visual Studio's debugging features or directly from the output directory.

## Configuration

- **Screen Dimensions**: Adjust `nScreenWidth` and `nScreenHeight` in the source code for the desired console size.
- **Map Dimensions**: Modify `nMapWidth` and `nMapHeight` to change the size of the map displayed.
- **Player Start Position and Angle**: Update `fPlayerX`, `fPlayerY`, and `fPlayerAngle` in the source code to change the starting position and orientation of the player within the map.

## Notes

- Ensure the console window size is sufficient to display the entire screen (`nScreenWidth` x `nScreenHeight`).
- The rendering performance may vary depending on the hardware capabilities and console window size.
  
By following these instructions, you can successfully compile, build, and run the raycasting engine project in your development environment.
