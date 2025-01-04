# PyQt Boilerplate Application

This is a simple PyQt5 boilerplate application demonstrating the **Model-View pattern**. It provides a basic interface to save text content to a file and shows error messages for invalid operations like missing file names or overwriting existing files.

## Features

- **Model-View Design Pattern**:
  - `Model`: Handles file saving logic and emits error signals.
  - `View`: Provides the user interface and emits signals to submit data.
  - `MainWindow`: Connects the `View` and `Model`.

- **File Saving**:
  - Accepts a file name and content from the user.
  - Displays error messages for invalid file operations.

![boilerplate](https://github.com/user-attachments/assets/47171373-b05f-4699-b9a7-0527a3052cd5)

## File Structure

- **`Model`**: 
  - Handles the business logic (e.g., file operations).
  - Emits error signals for issues like:
    - Empty filename.
    - Attempt to overwrite an existing file.
    - File write errors.

- **`View`**:
  - Defines the user interface with:
    - A text input field for the filename.
    - A text editor for file content.
    - A button to trigger the save operation.
  - Emits a `submitted` signal with the file name and content.

- **`MainWindow`**:
  - Integrates the `View` and `Model`.
  - Connects:
    - `View.submitted` to `Model.save`.
    - `Model.error` to `View.show_error`.

## Usage

1. Clone this repository
2. Install the required package:
   ```
   pip install PyQt5
   ```
3. Run the application:
   ```
   python template.py
   ```
4. Enter a filename (with filetype ending) and text content
5. Click the **Save** button to save the file
