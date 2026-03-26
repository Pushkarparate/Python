from collections import Counter
import os


def read_file():
    # write your code here...
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print("File not found")


def write_names():
    # write your code here...
    filename = input("Enter the filename: ")
    names = input("Enter comma-separated names: ").split(',')
    with open(filename, "w") as file:
        for name in names:
            file.write(name.strip())
    print("Names written to file")
