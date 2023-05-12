
# Banker's Algorithm

This repository contains a Python implementation of the Banker's algorithm, a resource allocation and deadlock avoidance algorithm used in operating systems. The algorithm ensures that the system does not enter an unsafe state, where a deadlock can occur, by carefully allocating resources to processes.

## Requirements
- Python 3.x
- PyQt5
- NumPy

## Usage
1. Run the main Python script:
python bankers_algorithm.py

2. A graphical user interface (GUI) window will appear.
3. Enter the number of processes and the number of resources in the respective input fields.
4. Click the "Next" button.
5. In the subsequent windows, enter the maximum needed resources for each process, the current resource allocation, and the total available resources.
6. Click the "Enter" button after entering the values in each window.
7. The program will determine if the system is in a safe state and display the results in a new window.
8. Close the windows to exit the program.

## Explanation of the Code
The provided Python code implements the Banker's algorithm using the PyQt5 library for creating the GUI. Here's a breakdown of the major components and classes in the code:

- The `Ui_DataInput1` class represents the GUI for inputting the number of processes and resources. It initializes the GUI elements and handles button click events.
- The `Banker` class implements the Banker's algorithm logic. It initializes the necessary data structures and performs the safety check to determine if the system is in a safe state.
- The `Ui_MaxInput`, `Ui_AllocInput`, and `Ui_TotalInput` classes represent the GUI windows for inputting the maximum needed resources, current resource allocation, and total available resources, respectively. These classes handle the GUI initialization and data entry.
- The `Ui_Update` class is responsible for the GUI window to update the resource allocation. It captures the process number, resource number, and amount to be allocated.
- The `Ui_Result` class displays the result of the Banker's algorithm. It determines whether the system is in a safe state and shows the sequence of processes if it is safe.
- The main execution flow starts with creating an instance of `Ui_DataInput1` and displaying the input window. The user enters the number of processes and resources, and subsequent windows appear to collect the required input.
- Finally, the program determines if the system is in a safe state and displays the result in the `Ui_Result` window.

