# Enhanced Notepad with Voice Control and Sentiment Analysis

This project is a feature-rich desktop Notepad application built with Python and Tkinter. It goes beyond basic text editing by incorporating voice commands for hands-free operation, sentiment analysis of your text, and robust security features like file encryption.

The core design principles are:
*   **Accessibility:** Voice commands allow users to perform many actions without needing a keyboard or mouse, making it easier to use for individuals with certain physical limitations.
*   **Security:** Offers an option to save files in an encrypted format (`.ntxt`), protecting sensitive information.
*   **Minimalism & Ease of Use:** While packed with features, the interface remains clean and intuitive, ensuring a smooth user experience.

This Notepad is designed for users who want a simple yet powerful tool for daily note-taking, with the added benefits of modern AI-powered features and enhanced security.

## Features

This Notepad application offers a wide array of functionalities:

**File Management:**
*   **New, Open, Save, Save As:** Standard file operations.
*   **Encryption:** Save and open files in an encrypted `.ntxt` format for enhanced security. Files saved with `.txt` or other extensions are stored as plain text.

**Text Editing & Formatting:**
*   **Standard Editing:** Copy, Paste, Cut, Clear All.
*   **Find & Replace:** Easily search for text and replace it.
*   **Font Customization:** Change font family, size, style (bold, italic, underline), and color.
*   **Text Alignment:** Align text to the left, center, or right.

**Advanced Capabilities:**
*   **Voice Commands:** Control various application functions using your voice (e.g., "open file", "save file", "text bold", dictation).
*   **Sentiment Analysis:** Real-time sentiment analysis of the text (Positive, Neutral, Negative) displayed in the status bar.
*   **Text-to-Speech:** Listen to your notes read out loud.
*   **Multiple Color Themes:** Choose from various color themes for the editor interface to suit your preference.

**User Interface:**
*   **Toolbar & Status Bar:** Toggle visibility for a cleaner workspace.
*   **Intuitive Design:** Easy-to-navigate menus and toolbar.

## Setup and Installation

There are two ways to run this Notepad application:

**1. Running the pre-built executable (Windows):**
*   Navigate to the `build/exe.win-amd64-3.8/` directory.
*   Run `NotepadView.exe`.

**2. Running from source:**
This method is recommended if you want to modify the code or contribute to the project.

*   **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```
    *(Please replace `https://github.com/your-username/your-repository-name.git` with the actual repository URL if you know it, otherwise leave it as a placeholder for the user to fill in.)*

*   **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

*   **Install dependencies:**
    Make sure you are in the project's root directory where `requirements.txt` is located.
    ```bash
    pip install -r requirements.txt
    ```

*   **Run the application:**
    ```bash
    python NotepadView.py
    ```

## Usage

Once the application is running, you can perform various actions through the menu bar, toolbar, or voice commands.

**Basic Operations:**
*   Use the **File** menu to create new files, open existing ones, save, or save as.
*   The **Edit** menu provides options for copy, paste, cut, clear all, and find/replace.
*   Customize the editor's appearance using the **Color Theme** menu.
*   Adjust font settings (family, size, style) and text alignment using the **Toolbar**.

**Key Features:**

*   **Voice Commands:**
    *   Click the microphone icon on the toolbar to activate voice command mode.
    *   Speak clearly into your microphone.
    *   Examples of voice commands:
        *   *"New file"*
        *   *"Open file"*
        *   *"Save file"*
        *   *"Text bold"*
        *   *"Search"*
        *   You can also dictate text directly.

*   **Sentiment Analysis:**
    *   As you type, the sentiment of your text (Positive, Neutral, or Negative) is automatically analyzed and displayed on the left side of the **Status Bar** at the bottom of the window.
    *   Word and character counts are also displayed in the status bar.

*   **Encrypted Files (`.ntxt`):**
    *   To save an encrypted file, choose "Save As" from the File menu and ensure the file extension is `.ntxt`. You can also type the filename with `.ntxt` (e.g., `mysecurenotes.ntxt`).
    *   When opening a `.ntxt` file, the application will automatically decrypt and display its content.
    *   Files saved with other extensions (e.g., `.txt`) will be stored as plain text.

*   **Text-to-Speech:**
    *   Click the speaker icon on the toolbar to have the current text content read out loud.

## Dependencies

*   **Python:** Version 3.8 or higher is recommended.
*   **Libraries:** All required Python libraries are listed in the `requirements.txt` file. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Contributing

Contributions are welcome! If you'd like to improve this Notepad application, please follow these steps:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature-or-bugfix-name
    ```
3.  **Make your changes** and commit them with clear messages.
4.  **Push your branch** to your forked repository:
    ```bash
    git push origin feature-or-bugfix-name
    ```
5.  **Create a Pull Request** from your forked repository to the original repository's `main` (or `master`) branch.

Please ensure your code adheres to any existing style guidelines and that your changes are well-tested (if applicable).

## License

This project is not currently licensed. You are free to add a `LICENSE.md` file to specify the terms under which this software is shared.

For example, if you choose the MIT License, you could state:
`This project is licensed under the MIT License - see the LICENSE.md file for details.`