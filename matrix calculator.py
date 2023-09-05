import numpy as np

def print_menu():
    print("\nMatrix Calculator Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrix by Scalar")
    print("4. Multiply Matrices")
    print("5. Transpose Matrix")
    print("6. Quit")

def add_matrices():
    matrix1 = np.array(eval(input("Enter the first matrix (as a list of lists): ")))
    matrix2 = np.array(eval(input("Enter the second matrix (as a list of lists): ")))
    
    if matrix1.shape != matrix2.shape:
        print("Matrices must have the same dimensions for addition.")
        return
    
    result = np.add(matrix1, matrix2)
    print("Result:")
    print(result)

def subtract_matrices():
    matrix1 = np.array(eval(input("Enter the first matrix (as a list of lists): ")))
    matrix2 = np.array(eval(input("Enter the second matrix (as a list of lists): ")))
    
    if matrix1.shape != matrix2.shape:
        print("Matrices must have the same dimensions for subtraction.")
        return
    
    result = np.subtract(matrix1, matrix2)
    print("Result:")
    print(result)

def multiply_scalar():
    matrix = np.array(eval(input("Enter the matrix (as a list of lists): ")))
    scalar = float(input("Enter the scalar: "))
    
    result = np.multiply(matrix, scalar)
    print("Result:")
    print(result)

def multiply_matrices():
    matrix1 = np.array(eval(input("Enter the first matrix (as a list of lists): ")))
    matrix2 = np.array(eval(input("Enter the second matrix (as a list of lists): ")))
    
    if matrix1.shape[1] != matrix2.shape[0]:
        print("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        return
    
    result = np.dot(matrix1, matrix2)
    print("Result:")
    print(result)

def transpose_matrix():
    matrix = np.array(eval(input("Enter the matrix (as a list of lists): ")))
    
    result = np.transpose(matrix)
    print("Result:")
    print(result)

while True:
    print_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_matrices()
    elif choice == "2":
        subtract_matrices()
    elif choice == "3":
        multiply_scalar()
    elif choice == "4":
        multiply_matrices()
    elif choice == "5":
        transpose_matrix()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
