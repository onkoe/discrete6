import numpy as np
import os
import pandas as pd
import sys

# Tell the script where to find the base autograder
sys.path.append("..")
sys.path.append(os.path.join("..", ".."))
from autograder_base import Base_Autograder

# Colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
O = '\033[33m'  # orange
Y = '\033[93m'  # yellow
G = '\033[32m'  # green


"""
Combinations Code Autograder

Autogrades a single students code
"""
class Autograder_Permutations(Base_Autograder):

    """
    Initializes variables
    """
    def __init__(self, in_student_name="student", in_this_dir=".", in_test_files=["..", "test_data"]):
        super().__init__()

        # Student information
        self.student_name = in_student_name
        self.is_grad = True
        self.DEBUG = True

        # Directory information
        self.this_dir =         in_this_dir
        self.student_files =    "Solution_Files"
        self.test_files =       ""

        for i in range(len(in_test_files)):
            self.test_files = os.path.join(self.test_files, in_test_files[i])
    
        self.test_files = os.path.join(self.test_files, "Permutations")

        # Test information
        self.test_names = [
            "test_1"
        ]


    """
    Check if the student's answer is within a reasonable bound of the actual answer
    Error Bound:
        - Check that student's answer is within 1% of actual answer

    Parameters:
        - expected  (ndarray):  The actual answer read from test_data/
        - result    (ndarray):  The student's answer
    """
    def is_error_within_bound(self, expected, result):

        try:
            # Make sure the shapes of the 
            if expected.shape != result.shape:
                raise Exception("Shapes of expected output and student output do not match")
            
            # Remove all quotation marks and commas
            symbols = "[]\','\"()"

            expected_test = np.char.strip(expected, symbols)
            expected_test = np.sort(expected_test)

            result_test = np.char.strip(result, symbols)
            result_test = np.sort(result_test)

            # Compare the two arrays
            return np.array_equal(expected_test, result_test)
        
        except Exception as err:
            print(f"{R}Error reading output file:{W}")
            print(f"{R}\t{err}{W}")

        return


    """
    Autogrades Combinations Problem
    Overrides Base_Autograder.autograde()

    Constructs a test by retrieving data about paths and data locations, then calls Base_Autograder.grade_problem()
    to test and grade the problem
    """
    def autograde(self):
        this_dir =  os.path.abspath(self.this_dir)
        test_dir =  os.path.abspath(self.test_files)

        # Print the test dir and project dir
        if self.DEBUG:
            print(f"{G} --> Test dir: {test_dir}{W}")
            print(f"{G} --> Project dir: {this_dir}{W}")

        columns = []
        for p in self.test_names:
            columns.append(f"{p}")

        # student grades
        grade = pd.DataFrame(
            np.nan,
            index=[self.student_name],
            columns=columns
        )

        # student timing
        time = pd.DataFrame(
            np.nan,
            index=[self.student_name],
            columns=columns
        )

        # Input files
        t_in = [
            os.path.join(test_dir, "input-1.csv")
        ]

        # Expected output files
        t_out = [
            os.path.join(test_dir, "output-1.csv")
        ]

        # Actual output from the student
        t_dir = os.path.join(this_dir, self.student_files)
        t_get = []

        for out in range(len(t_out)):
            t_get.append(os.path.join(t_dir, f"test{out}_output.csv"))

        # Generate commands for the program
        # Command structure:
        #   python3 combination.py
        # test_data = [ ]
        c_p2 = []

        for file in range(len(self.test_names)):
            c_p2.append([
                "make run"
            ])

        # Add in command "references" that will tell which argument is which (mainly for result csv and time csv)
        # Dictionary format:
        #       key = flag (i.e. "t" = time argument), value = index of argument in command structure
        # TODO: This can be expanded upon later for every argument so no arguments have to be guessed
        c_ref = {"r": 1, "t": -1}

        # Autograde with test parameters
        test_params = []

        for file in range(len(self.test_names)):
            test_params.append(
                [t_dir, t_out[file], t_get[file], c_p2[file], False, self.is_error_within_bound]
            )

        test_results = [None] * len(columns)
        
        # Test every problem
        grade_index = 0
        for file in range(len(self.test_names)):
            params = test_params[file]
            result = self.grade_problem(
                params[0],                      # student directory
                [params[1]],                    # test output
                [params[2]],                    # test results
                [params[3]],                    # commands
                c_ref,                          # command references
                params[4],                      # exact
                params[5]                       # error function to be passed
            )

            test_results[grade_index] = result[0]

            # Add results to dataframes
            grade.loc[self.student_name, columns[grade_index]] = test_results[grade_index][0]
            grade_index += 1

        return [grade, time]
    

"""
Start of Program Logic
"""
def main():
    print(f"{G}Autograding for Permutation Assignment:\n{W}")
    
    autograder = Autograder_Permutations()
    res = autograder.autograde()

    total   = len(res[0].columns)
    correct = int(res[0].sum(axis=1)[0])

    print(f"{Y}\nFinal Grades:{W}")
    res[0].to_csv("grades.csv")
    print(res[0])

    print(f"\n --> {correct}/{total} problems correct\n")


if __name__ == "__main__":
    main()