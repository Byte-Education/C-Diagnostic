# C Diagnostic

This is a simple diagnostic in C. This is intended to provide some base understanding of what the student understands to better cater tutoring to teach at the students' level.

## Prerequisites

1. `gcc` and `make` both must be installed in order to run the code.
2. In order to do this diagnostic, an understanding of how to use the terminal and call `make` is required. If the user doesn't know how to do so, a basic lesson may be required before beginning this diagnostic.
3. In order to run the tester, `python3` must be installed.

## Instructions to Run

In your terminal, navigate to the folder and run `make`. This will compile the code. In order to test the code, run `make test`. This will compile the code into a binary and run that code. For the most part, this will simply allow you to see if it's correct or not.

While running `make` at the base level will compile all of the code, it may be more useful to compile it at each question. To do so, navigate to the question folder and run `make` there.

## Instructions to Test

Run `python3 test.py <question number>` where the question number is added. For example, in order to test question 3, running `python3 test.py 3` would run the test script for question 3.

In order to test all questions at once, run `python3 test.py all`. This will run all of the tests and see what problems require more attention.

### Important Notes

Questions 1 and 2 need to be manually checked as there is a high degree of variance with the question itself.
