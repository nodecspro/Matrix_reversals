import tkinter as tk
from tkinter import messagebox, ttk

import customtkinter as ctk
import numpy as np
from customtkinter import CTkToplevel


class MatrixCalculator:
    """
    Класс для вычисления обратной матрицы методом исключения Гаусса.

    Атрибуты:
        - root: корневой объект Tk
        - main_frame: основной фрейм графического интерфейса
        - dimension_label: метка для выбора размерности матрицы
        - dimension_var: строковый переменный для хранения выбранной размерности
        - dimension_combobox: Комбобокс для выбора размерности матрицы
        - create_matrix_button: кнопка для создания окна ввода матрицы
        - matrix_window: Двухуровневое окно для ввода матрицы
    """

    def __init__(self, root):
        """
        Инициализирует объект MatrixCalculator.

        Параметры:
            - root: корневой объект Tk
        """
        self.root = root
        self.root.title("Обратная матрица")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.dimension_label = ctk.CTkLabel(
            self.main_frame, text="Выберите размерность матрицы:"
        )
        self.dimension_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.dimension_var = ctk.StringVar()
        self.dimension_combobox = ctk.CTkComboBox(
            self.main_frame,
            variable=self.dimension_var,
            values=[str(i) for i in range(2, 11)],
            state="readonly",
        )

        self.dimension_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.dimension_combobox.set("2")

        self.create_matrix_button = ctk.CTkButton(
            self.main_frame, text="Создать матрицу", command=self.create_matrix_window
        )
        self.create_matrix_button.grid(row=0, column=2, padx=5, pady=5)

        root.eval("tk::PlaceWindow . center")

        self.matrix_window = None

    def gauss_elimination(self, matrix):
        """
        Вычисляет обратную матрицу, используя гауссово исключение.

        Параметры:
            - matrix: массив numpy, представляющий матрицу для инвертирования

        Возвращает:
            - inverse_matrix: массив numpy, представляющий инвертированную матрицу, или None, если матрица сингулярна.
        """
        n = len(matrix)
        augmented_matrix = np.hstack((matrix, np.identity(n)))

        for col in range(n):
            pivot_row = col

            for i in range(col + 1, n):
                if abs(augmented_matrix[i][col]) > abs(
                    augmented_matrix[pivot_row][col]
                ):
                    pivot_row = i

            if abs(augmented_matrix[pivot_row][col]) < 1e-10:
                messagebox.showerror(
                    "Ошибка", "Матрица вырождена. Обратной матрицы не существует."
                )
                return None

            augmented_matrix[[col, pivot_row]] = augmented_matrix[[pivot_row, col]]

            for i in range(col + 1, n):
                factor = augmented_matrix[i][col] / augmented_matrix[col][col]
                augmented_matrix[i, col:] -= factor * augmented_matrix[col, col:]

        for col in range(n - 1, -1, -1):
            augmented_matrix[col] /= augmented_matrix[col, col]
            for i in range(col - 1, -1, -1):
                augmented_matrix[i] -= augmented_matrix[i, col] * augmented_matrix[col]

        inverse_matrix = augmented_matrix[:, n:]
        return inverse_matrix

    def is_valid_number(self, value):
        """
        Проверяет, является ли строка действительным числом.

        Параметры:
            - value: строка, представляющая проверяемое значение

        Возвращает:
            - True, если значение является действительным числом, False в противном случае
        """
        if value == "":
            return True
        try:
            float(value)
            if value.startswith("+") or " " in value:
                return False
            if value.count("0") > 1 and value[0] == "0" and value[1] != ".":
                return False
            return True
        except ValueError:
            if value == "-" and len(value) == 1:
                return True
            return False

    def create_matrix_window(self):
        """
        Создает окно Toplevel для ввода матрицы.
        """
        if self.matrix_window is not None:
            self.matrix_window.deiconify()
            self.matrix_window.lift()
            return

        try:
            dimension = int(self.dimension_var.get())
            if dimension < 2 or dimension > 10:
                raise ValueError("Размерность матрицы должна быть от 2 до 10.")

            self.matrix_window = CTkToplevel(self.root)
            self.matrix_window.title("Ввод матрицы")
            self.matrix_window.grab_set()

            matrix_entries = []
            for i in range(dimension):
                row_entries = []
                for j in range(dimension):
                    entry = ctk.CTkEntry(self.matrix_window, width=48, justify="center")
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    entry.insert(0, "")
                    vcmd = (entry.register(lambda P: self.is_valid_number(P)), "%P")
                    entry.configure(validate="key", validatecommand=vcmd)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)

            calculate_button = ctk.CTkButton(
                self.matrix_window,
                text="Посчитать обратную матрицу",
                command=lambda: self.calculate_inverse(matrix_entries, dimension),
            )
            calculate_button.grid(row=dimension, columnspan=dimension, padx=5, pady=10)

            self.root.eval(f"tk::PlaceWindow {str(self.matrix_window)} center")

            self.matrix_window.protocol("WM_DELETE_WINDOW", self.hide_matrix_window)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def hide_matrix_window(self):
        """
        Скрывает окно ввода матрицы.
        """
        if self.matrix_window is not None:
            self.matrix_window.withdraw()
            self.matrix_window = None

    def calculate_inverse(self, matrix_entries, dimension):
        """
        Вычисляет обратную величину матрицы, введенной в окно ввода матрицы.

        Параметры:
            - matrix_entries: список списков объектов ttk.Entry, представляющих матрицу
            - dimension: целое число, представляющее размерность матрицы
        """
        try:
            matrix = []
            for i in range(dimension):
                row = []
                for j in range(dimension):
                    entry_value = matrix_entries[i][j].get()
                    if entry_value == "":
                        messagebox.showerror("Ошибка", "Необходимо заполнить все поля.")
                        return
                    row.append(float(entry_value))
                matrix.append(row)

            inverse_matrix = self.gauss_elimination(np.array(matrix))

            if inverse_matrix is not None:
                self.show_inverse_matrix(inverse_matrix)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    def show_inverse_matrix(self, inverse_matrix):
        """
        Отображает инвертированную матрицу в новом окне Toplevel.

        Параметры:
            - inverse_matrix: массив numpy, представляющий инвертированную матрицу
        """
        self.result_window = CTkToplevel(self.root)
        self.result_window.title("Результат")
        self.result_window.grab_set()

        dimension = len(inverse_matrix)
        for i in range(dimension):
            for j in range(dimension):
                entry = ctk.CTkEntry(self.result_window, width=48, justify="center")
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.insert(0, f"{inverse_matrix[i][j]:.2f}")
                entry.configure(state="readonly")

        self.root.eval(f"tk::PlaceWindow {str(self.result_window)} center")


if __name__ == "__main__":
    app = ctk.CTk()
    MatrixCalculator(app)
    app.mainloop()
