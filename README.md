# quiz-game-project-of-Micro-IT
# Online Quiz Game
make sure the files are in same directory .

This is a simple online quiz game implemented in Python using the `tkinter` library for the GUI and the `requests` library to fetch questions from the Open Trivia Database API.

## Features

* Fetches quiz questions from the Open Trivia Database API.
* Presents multiple-choice questions in a user-friendly graphical interface.
* Provides feedback on correct and incorrect answers.
* Keeps track of the user's score.
* Plays sound effects for correct and incorrect answers.
* Includes animated question display.

## Requirements

* Python 3.x
* tkinter (usually included with Python)
* requests
* playsound (install using pip: `pip install playsound==1.2.2`  **Note:** Version 1.2.2 is recommended to avoid blocking issues)
* Sound files ("correct.wav" and "wrong.wav")

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install requests playsound==1.2.2
    ```

4.  Place `correct.wav` and `wrong.wav` in the same directory as the script. You can find or create your own sound files and name them accordingly.

## Usage

1.  Run the script:

    ```bash
    python quiz_game.py
    ```

2.  Answer the questions presented in the GUI.
3.  Click the "Next" button to proceed to the next question.
4.  At the end of the quiz, your score will be displayed.

## Code Description

* `quiz_game.py`:  The main Python script containing the `QuizApp` class, which handles the GUI, fetches questions, and manages the game logic.

    * `QuizApp` class:
        * `__init__`: Initializes the GUI, variables, and fetches questions.
        * `create_widgets`: Creates the GUI elements (labels, radio buttons, buttons).
        * `fetch_questions`: Fetches questions from the Open Trivia Database API and prepares them for display.
        * `animate_label`: Animates the display of the question text.
        * `play_correct_sound`, `play_wrong_sound`:  Plays sound effects.
        * `load_question`:  Loads and displays a question and its options.
        * `next_question`:  Handles the logic when the "Next" button is clicked, checks the answer, updates the score, and loads the next question.

## Credits

* Uses questions from the [Open Trivia Database API](https://opentdb.com/).
* Developed by \[gajula jyothindra/jyothidra-coder]


##  Troubleshooting

* **`playsound` blocking issue:** Ensure you are using `playsound==1.2.2`.  Later versions might cause the GUI to freeze while playing sound.
* **API Errors:** If you encounter errors fetching questions, check your internet connection and ensure the Open Trivia Database API is accessible.
* **Missing Sound Files:** Make sure `correct.wav` and `wrong.wav` are in the same directory as `quiz_game.py`.
