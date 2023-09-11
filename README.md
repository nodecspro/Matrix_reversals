# Matrix Calculator with Gaussian Elimination

This Python program provides a matrix calculator that computes the inverse of a matrix using the Gaussian elimination method. It includes a graphical user interface (GUI) built with the tkinter library for easy interaction.

## Features

- Choose matrix dimensions via a combobox.
- Input matrix values using a user-friendly interface.
- Calculate the inverse of the matrix.
- Handles singular matrices and displays appropriate error messages.
- Utilizes the numpy library for matrix operations.
- Enhances GUI with ttk library for widgets.
- Exception handling for error management.
- Lambda functions for input validation.

## Usage

1. Select the desired matrix dimension from the combobox.
2. Click the "Create matrix" button to input matrix values.
3. Enter matrix values in the grid of entry widgets.
4. Click the "Calculate inverse matrix" button.
5. The inverse matrix is displayed in a new window.

## Main Logic

The core functionality of the program is encapsulated in the `MatrixCalculator` class:

- `__init__`: Initializes the GUI and widgets.
- `gauss_elimination`: Implements Gaussian elimination for matrix inversion.
- `is_valid_number`: Helper function to validate numbers.
- `create_matrix_window`: Creates the matrix input window.
- `calculate_inverse`: Computes the inverse of the matrix.
- `show_inverse_matrix`: Displays the inverse matrix.
