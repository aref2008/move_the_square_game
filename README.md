
# Move the Square Game

## Overview

This Flask application utilizes the **spaCy** library for natural language processing (NLP) to interpret user commands, allowing control of a shape's movement and appearance on the webpage. The app supports various user commands like "move left," "change color," or "jump," and processes these inputs through the `process_command` function. The function extracts meaningful actions based on keywords, updating the state of the shape accordingly.

The commands are categorized into:
- **Movement**: Move the shape (left, right, up, down)
- **Color**: Change the shape’s color
- **Shape**: Alter the shape type (e.g., from square to circle)
- **Jump**: Move the shape to random positions on the screen

The state dictionary keeps track of the shape's position, color, and type, and is updated in real-time as per the user's commands.

## Screenshot

Here is a screenshot of the main page of the application:

![Main Page Screenshot](https://github.com/aref2008/move_the_square_game/blob/main/screenshot.png?raw=true)

## Demo Video

Watch the [demo video](https://www.youtube.com/watch?v=LY2hIWl8IvU) showcasing the functionality of the app in action.

## Challenges Faced

### 1. **Designing Shape Movement Within Borders**
   - Ensuring the shape remains within defined boundaries was a significant challenge. Precise calculations for the x and y coordinates were necessary to prevent the shape from overlapping the edges of the box.

### 2. **Testing Command Variations**
   - Recognizing different sentence structures for commands (e.g., "move left" vs. "please move it left") required thorough testing and effective NLP processing. It was essential to interpret a wide variety of inputs while accurately triggering the appropriate actions.

## Potential Improvements

1. **Adding More Commands**
   - Introduce more complex commands, such as "dance" or "spin," to create additional animations for the shape.

2. **Adding More Shapes and Characters**
   - Expand beyond basic shapes (like squares and circles) by adding more complex characters such as Dora or Mickey Mouse for a more interactive experience.

3. **Allowing Users to Control Velocity and Colors**
   - Provide users with more control by allowing them to adjust the movement speed (velocity) and customize the shape's colors.

4. **Feedback System**
   - Implement a feedback system to confirm successful command processing or notify users if the input is invalid.

5. **Mobile Responsiveness**
   - Optimize the app for mobile devices to ensure the interface adapts to smaller screens and provides a better user experience.

6. **User Profiles and Preferences**
   - Allow users to save their preferences for shape, color, and velocity, enabling a more personalized and engaging experience.

## Requirements

- Flask
- spaCy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aref2008/move_the_square.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the spaCy language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage

1. Access the application via `http://localhost:5000/`.
2. Input commands in the text box to control the shape's movement and appearance. Examples include:
   - "move left"
   - "change color"
   - "jump"
   - "please move it right"
