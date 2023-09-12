# Code AutoTyper

Code AutoTyper is a simple Python application that provides a GUI to input text, set a shortcut, and an initial delay. When the user presses the shortcut key, the application automatically types the text into the active window with proper handling of indentation, making it particularly useful for pasting Python code or other multiline content.

## Features

- **Custom Shortcut**: Set your own shortcut key to trigger the Code AutoTyper.
- **Initial Delay**: Define a delay before the Code AutoTyper starts to type, giving you time to focus on the desired input field.
- **Python Code Friendly**: Handles multiline Python code with proper indentation.
- **Simple GUI**: Easily paste the text and set the shortcut and delay using a simple interface.

## Prerequisites

Make sure you have the required libraries installed:

```bash
pip install pyautogui keyboard tkinter
```

**Note**: Ensure you run the script with the necessary privileges, as some systems may restrict apps from registering global hotkeys or simulating keyboard presses without appropriate permissions.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/AkshatRastogi-1nC0re/Code_AutoTyper.git
   ```

2. Navigate to the directory:
   ```bash
   cd Code_AutoTyper
   ```

3. Run the application:
   ```bash
   python Code_AutoTyper.py
   ```

4. Use the GUI to paste your text, set the shortcut key, and define the initial delay.

5. Click on "Start Listening". The application will now listen for the shortcut key.

6. Once you press the defined shortcut key, the application will type out the given text wherever your cursor is.

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
