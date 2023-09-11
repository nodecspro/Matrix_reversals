# Matrix_reversals

## English

The code is a Python implementation of a matrix calculator that computes an inverse matrix using the Gaussian elimination method. The program includes a graphical user interface (GUI) built with the tkinter library. The GUI features a combobox that enables users to select the matrix dimension they want to invert. After selecting the dimension, users can click the "Create matrix" button to open a new window for inputting matrix values. The matrix input window consists of a two-level window with a grid of entry widgets for entering matrix values. Once the values are entered, users can click the "Calculate inverse matrix" button to compute the inverse of the matrix. In case of a singular matrix, the program displays an error message indicating that the inverse matrix does not exist.

The main logic of the program is implemented in the `MatrixCalculator` class. The `__init__` method initializes the GUI by creating the main frame and the necessary widgets. The `gauss_elimination` method implements the Gauss elimination algorithm for calculating the inverse of the matrix. The `is_valid_number` method is a helper function that checks if a given string is a valid number. The `create_matrix_window` method creates the matrix input window, and the `calculate_inverse` method computes the inverse of the matrix. Finally, the `show_inverse_matrix` method displays the inverse matrix in a new window.

The program utilizes the numpy library to represent matrices as arrays and the ttk library to create GUI widgets. Exception handling is employed to catch errors and display error messages to users. Lambda functions are used to validate input values in the matrix input window.

To enhance code readability, more descriptive variable and method names could be employed. Additionally, additional comments could be added to explain the purpose of each method and variable. For improved program performance, a more efficient algorithm could be used for matrix inversion, and multithreading could be implemented to enhance GUI responsiveness.

## Russian

Код представляет собой реализацию матричного калькулятора на языке Python, который вычисляет обратную матрицу методом исключения Гаусса. Программа включает графический интерфейс пользователя (GUI), построенный с использованием библиотеки tkinter. В GUI присутствует комбобокс, который позволяет пользователям выбирать размерность матрицы, которую они хотят инвертировать. После выбора размерности пользователи могут нажать кнопку "Создать матрицу", чтобы открыть новое окно для ввода значений матрицы. Окно ввода матрицы состоит из двухуровневого окна с сеткой виджетов ввода для ввода значений матрицы. После ввода значений пользователи могут нажать кнопку "Вычислить обратную матрицу", чтобы вычислить обратную матрицу. В случае сингулярной матрицы программа отображает сообщение об ошибке, указывающее, что обратная матрица не существует.

Основная логика программы реализована в классе `MatrixCalculator`. Метод `__init__` инициализирует GUI, создав основной фрейм и необходимые виджеты. Метод `gauss_elimination` реализует алгоритм исключения Гаусса для вычисления обратной матрицы. Метод `is_valid_number` является вспомогательной функцией, которая проверяет, является ли заданная строка действительным числом. Метод `create_matrix_window` создает окно ввода матрицы, а метод `calculate_inverse` вычисляет обратную матрицу. Наконец, метод `show_inverse_matrix` отображает обратную матрицу в новом окне.

Программа использует библиотеку numpy для представления матриц в виде массивов и библиотеку ttk для создания виджетов GUI. Обработка исключений используется для обработки ошибок и отображения сообщений об ошибках пользователям. Лямбда-функции используются для проверки вводимых значений в окне ввода матрицы.

Для повышения читаемости кода можно использовать более описательные имена переменных и методов. Кроме того, можно добавить дополнительные комментарии для объяснения назначения каждого метода и переменной. Для улучшения производительности программы можно использовать более эффективный алгоритм для вычисления обратной матрицы и реализовать многопоточность для улучшения отзывчивости GUI.
