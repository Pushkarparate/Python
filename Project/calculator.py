import numpy as np
import statistics

def matrix_module():
    try:
        print("\n--- Matrix Algebra Module ---")

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("Enter elements for Matrix A:")
        A = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            A.append(row)
        A = np.array(A)

        print("Enter elements for Matrix B:")
        B = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            B.append(row)
        B = np.array(B)

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Determinant (Matrix A)")
        print("5. Inverse (Matrix A)")

        choice = int(input("Choose operation: "))

        if choice == 1:
            print("Result:\n", A + B)

        elif choice == 2:
            print("Result:\n", A - B)

        elif choice == 3:
            print("Result:\n", np.dot(A, B))

        elif choice == 4:
            if rows == cols:
                print("Determinant:", np.linalg.det(A))
            else:
                print("Determinant requires square matrix.")

        elif choice == 5:
            if rows == cols:
                print("Inverse:\n", np.linalg.inv(A))
            else:
                print("Inverse requires square matrix.")

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
    except Exception as e:
        print("Error:", e)


def statistics_module():
    try:
        print("\n--- Statistical Analysis Module ---")
        data = list(map(float, input("Enter numbers separated by space: ").split()))

        print("Mean:", statistics.mean(data))
        print("Median:", statistics.median(data))
        print("Standard Deviation:", statistics.stdev(data))

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except statistics.StatisticsError as e:
        print("Statistics error:", e)


def unit_conversion():
    try:
        print("\n--- Unit Conversion Module ---")
        print("1. Length (Meters ↔ Kilometers)")
        print("2. Temperature (Celsius ↔ Fahrenheit)")
        print("3. Weight (Kg ↔ Pounds)")

        choice = int(input("Choose conversion type: "))

        if choice == 1:
            print("1. Meters → Kilometers")
            print("2. Kilometers → Meters")
            sub = int(input("Choose: "))
            val = float(input("Enter value: "))

            if sub == 1:
                print("Result:", val / 1000, "km")
            elif sub == 2:
                print("Result:", val * 1000, "m")

        elif choice == 2:
            print("1. Celsius → Fahrenheit")
            print("2. Fahrenheit → Celsius")
            sub = int(input("Choose: "))
            val = float(input("Enter temperature: "))

            if sub == 1:
                print("Result:", (val * 9/5) + 32, "°F")
            elif sub == 2:
                print("Result:", (val - 32) * 5/9, "°C")

        elif choice == 3:
            print("1. Kg → Pounds")
            print("2. Pounds → Kg")
            sub = int(input("Choose: "))
            val = float(input("Enter value: "))

            if sub == 1:
                print("Result:", val * 2.20462, "lbs")
            elif sub == 2:
                print("Result:", val / 2.20462, "kg")

        else:
            print("Invalid option")

    except ValueError:
        print("Invalid input! Please enter numbers.")
    except ZeroDivisionError:
        print("Division by zero error.")


def main():
    while True:
        print("\n====== Engi-Calc ======")
        print("1. Matrix Algebra")
        print("2. Statistical Analysis")
        print("3. Unit Conversion")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                matrix_module()

            elif choice == 2:
                statistics_module()

            elif choice == 3:
                unit_conversion()

            elif choice == 4:
                print("Exiting Engi-Calc...")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Please enter a valid number!")



main()