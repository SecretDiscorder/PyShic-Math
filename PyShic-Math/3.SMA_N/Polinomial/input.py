import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_equation(equation_str):
    x = sp.Symbol('x')
    f_x = sp.Function('f')(x)  # Menggunakan f(x) sebagai fungsi

    lhs, rhs = equation_str.split('=')
    lhs_expr = sp.sympify(lhs.replace(' ', ''))
    rhs_expr = sp.sympify(rhs.replace(' ', ''))

    if 'f(x)' in str(lhs_expr) or 'f(x)' in str(rhs_expr):
        f_x_expr = sp.solve(lhs_expr - rhs_expr, f_x)[0]
        m = f_x_expr.as_coefficients_dict(x)[x]
        b = f_x_expr.subs(x, 0)

        # Tampilkan perhitungan persamaan fungsi
        print("Persamaan Fungsi:")
        print(f"{lhs} = {rhs}")
        print(f"{lhs_expr} = {rhs_expr}")
        print(f"f(x) = {f_x_expr}")
        print(f"Koefisien m = {m}")
        print(f"Koefisien b = {b}\n")

        # Gambar grafik SPLDV
        plot_spldv(m, b)

    elif equation_str.count('x') == 1 and equation_str.count('y') == 1:
        lhs_expr = sp.sympify(add_implicit_multiplication(lhs.replace(' ', '')))
        rhs_expr = sp.sympify(add_implicit_multiplication(rhs.replace(' ', '')))

        equation = sp.Eq(lhs_expr, rhs_expr)

        if equation.has(x) and equation.has(f_x):
            y_expr = sp.solve(equation, f_x)[0]
            m = y_expr.as_coefficients_dict(x)[x]
            b = y_expr.subs(x, 0)

            # Tampilkan perhitungan persamaan fungsi
            print("Persamaan Fungsi:")
            print(f"{lhs} = {rhs}")
            print(f"{lhs_expr} = {rhs_expr}")
            print(f"f(x) = {y_expr}")
            print(f"Koefisien m = {m}")
            print(f"Koefisien b = {b}\n")

            # Gambar grafik SPLDV
            plot_spldv(m, b)
        else:
            print("Masukkan persamaan aljabar yang valid (misalnya: 'x + y = 2').")
    else:
        print("Format persamaan tidak didukung. Masukkan persamaan fungsi (f(x)) atau persamaan aljabar (x + y = 1).")

def add_implicit_multiplication(expression):
    # Tambahkan operator '*' eksplisit sebelum variabel tanpa operator di antara mereka
    # Misalnya, ubah '3x+5y' menjadi '3*x+5*y'
    operators = {'x', 'y'}
    new_expr = ""
    for i, char in enumerate(expression):
        new_expr += char
        if char.isalpha() and i < len(expression) - 1 and expression[i+1] not in operators:
            new_expr += '*'
    return new_expr

def plot_spldv(m, b):
    x = np.linspace(-10, 10, 1000)  # Menghasilkan 1000 titik antara -10 hingga 10
    y = m * x + b

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik SPLDV (f(x) = mx + b)')
    plt.grid(True)
    plt.show()

# Menerima input persamaan dari pengguna
equation_str = input("Masukkan persamaan (misalnya: 'f(x) = x**2 + 3*x - 4' atau 'x + y = 1'): ")
plot_equation(equation_str)
