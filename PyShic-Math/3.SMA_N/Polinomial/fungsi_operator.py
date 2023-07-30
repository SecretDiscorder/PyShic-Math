import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

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

def plot_spldv(m, b, label):
    x = np.linspace(-10, 10, 1000)  # Menghasilkan 1000 titik antara -10 hingga 10
    y = m * x + b

    plt.plot(x, y, label=label)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

def main():
    x = sp.Symbol('x')
    f_x = sp.Function('f')(x)  # Menggunakan f(x) sebagai fungsi
    g_x = sp.Function('g')(x)  # Menggunakan g(x) sebagai fungsi

    print("Masukkan persamaan fungsi f(x) dan g(x) serta operator matematika.")
    print("Contoh: 'f(x) = x**2 + 3*x - 4', 'g(x) = 2*x + 1', dan operator '+', '-', '*', '/'.")

    f_equation_str = input("Masukkan persamaan fungsi f(x): ")
    g_equation_str = input("Masukkan persamaan fungsi g(x): ")
    operator = input("Masukkan operator matematika (+, -, *, /): ")

    # Hitung persamaan f(x) dan g(x)
    f_x_expr = sp.sympify(f_equation_str.replace(' ', ''))
    g_x_expr = sp.sympify(g_equation_str.replace(' ', ''))

    # Perhitungan operasi antara f(x) dan g(x)
    result_expr = None
    if operator == '+':
        result_expr = f_x_expr + g_x_expr
    elif operator == '-':
        result_expr = f_x_expr - g_x_expr
    elif operator == '*':
        result_expr = f_x_expr * g_x_expr
    elif operator == '/':

        result_expr, _ = sp.div(f_x_expr, g_x_expr)  # Gunakan sp.div() untuk pembagian polinomial
    elif operator == '%':
        quotient, remainder = sp.div(f_x_expr, g_x_expr)  # Gunakan sp.div() untuk pembagian polinomial
        result_expr = remainder
    else:
        print("Operator matematika tidak valid. Silakan gunakan '+', '-', '*', atau '/'.")
        return

    # Tampilkan perhitungan persamaan fungsi dan operator matematika
    print("\nHasil Operasi:")
    print(f"f(x) = {f_x_expr}")
    print(f"g(x) = {g_x_expr}")
    print(f"Hasil (f(x) {operator} g(x)) = {result_expr}\n")

    # Persiapkan persamaan f(x) dan hasilnya untuk digambar dalam grafik SPLDV
    m_f_x = f_x_expr.as_coefficients_dict(x)[x]
    b_f_x = f_x_expr.subs(x, 0)
    m_result = result_expr.as_coefficients_dict(x)[x]
    b_result = result_expr.subs(x, 0)

    # Gambar grafik SPLDV f(x) dan hasil operasi
    plt.figure(figsize=(8, 6))
    plot_spldv(m_f_x, b_f_x, 'f(x)')
    plot_spldv(m_result, b_result, f'f(x) {operator} g(x)')
    plt.legend()
    plt.title(f'Grafik SPLDV (f(x) dan f(x) {operator} g(x))')
    plt.show()

if __name__ == "__main__":
    main()
