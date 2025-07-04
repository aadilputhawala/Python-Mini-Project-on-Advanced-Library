import numpy as np

def input_matrix(n):
    print(f"Enter elements for matrix {n} (row by row, space-separated):")
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print("Enter the matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def display_menu():
    print("\nChoose an operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Inverse of Matrix A")
    print("6. Exit")

A = input_matrix("A")
B = input_matrix("B")

while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        if A.shape == B.shape:
            print("Result:\n", A + B)
        else:
            print("Matrices must be of same shape for addition.")
    elif choice == "2":
        if A.shape == B.shape:
            print("Result:\n", A - B)
        else:
            print("Matrices must be of same shape for subtraction.")
    elif choice == "3":
        if A.shape[1] == B.shape[0]:
            print("Result:\n", np.dot(A, B))
        else:
            print("Columns of A must match rows of B for multiplication.")
    elif choice == "4":
        print("Transpose of A:\n", A.T)
    elif choice == "5":
        if A.shape[0] == A.shape[1]:
            try:
                print("Inverse of A:\n", np.linalg.inv(A))
            except np.linalg.LinAlgError:
                print("Matrix A is not invertible.")
        else:
            print("Matrix A must be square to find inverse.")
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
