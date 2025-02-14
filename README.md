You will have to achieve 100% Branch and Condition Coverage. For this assignment, this means that for each conditional statement, you need to have a test case for each combination of conditions. So if your conditional statement was a or b you would need to have a test case for each row of the following truth table:
Truth table for "a or b" a 	b 	outcome
T 	T 	T
T 	F 	T
F 	T 	T
F 	F 	F

If you recall what I said in the exploration, Branch and Condition coverage is usually not done due to the number of tests required. We are doing it here because we are only testing a single function, not an entire program. The function under test is defined below.

Behold! The Source!

import math

def contrived_func(val):

    a = val - math.sqrt(abs(val*2)) > 5
    b = val ** 2 % 2 == 0
    c = val * 5 < 100
    d = -val ** 3 > 0

    if a or b:
        if (a and b) or (b and c) and d:
            pass
        else:
            pass
    else:
        if (a or b) or (b or c):
            pass
        else:
            pass
    
    if a and b:
        pass
    else:
        pass

Again, this function's only purpose is as a learning aid; it doesn't do anything. DO NOT try to rationalize its behavior! This function is contained within contrived_func.py, so make sure you are importing the correct file.

You need to write a series of unit tests that attempt to meet 100% Branch and Condition Coverage. Once submitted to Gradescope, the autograder will run the tests against a modified version of the above code. The contrived_func on Gradescope is functionally equivalent but includes print statements when each condition combination is triggered. There are 18 such triggers, labeled C* (with * representing a number). You will only receive full credit for the autograded portion if your test suite triggers all 12 print statements.

Outside of the autograded portion, your test suite will also be graded based on how many tests were required to uncover all 18 triggers. Full points will only be rewarded if you can do it with 8 or fewer test cases. Please note that if your tests do not pass the autograder with full marks, you will not be eligible for these Efficient Testing points. Also, for the purposes of the efficiency points, each assert/call to contrived_func counts as a single test, so there is no putting in multiple asserts in each test case.

Finally, as was the case last week, your test suite needs to be free of linting errors.
Hints
Truth Tables

You should immediately notice from GradeScope that the names of the conditions we are trying to trigger are not sequential. For example, there are C3 and C4, but no C1 or C2. This is because they are named after given rows from the truth tables I generated when crafting this assignment. You will find that some rows are not possible to verify every conditional in every permutation (T or F will never evaluate the F due to short circuit evaluation). You can only write a test for rows that are possible.

Therefore, I highly recommend you write out, by hand, the truth tables for each conditional statement. You should also ask yourself the question, how does having a nested if affect the truth tables? Feel free to discuss this topic on Ed, but do not share your actual tables themselves.
Misc

    You will need to include

    if __name__ == '__main__':
        unittest.main()

    Feel free to take the provided source above and create your own contrived_func.py to run your tests against to help find errors with your testing file
    Do not use Random Testing for this assignment, you will get your chance in HW3: Random Testing Hands On 
