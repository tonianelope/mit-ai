# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x ** 3

def factorial(x):
    if (x < 0):
        raise ValueError('factorial: input {} cannot be negative'.format(n))
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def count_pattern(pattern, lst):
    match = True
    matches = 0
    for e in range(len(lst)):
        i = e
        for p in pattern:
           # print(lst[i], p, lst[e])
            if(i < len(lst) and lst[i] == p):
                match = match and True
                i += 1
            else:
                match = False
        if(match):
            matches += 1
        match = True
    return matches


# Problem 2.2: Expression depth

def depth(expr):
    d = [0] * len(expr)
    #if(isinstance(expr, (list, tuple))):
    #   d += 1
    for i in range(len(d)):
        #print(e)
        if(isinstance(expr[i], (list, tuple))):
            d[i] = depth(expr[i])
    return max(d) + (1 if isinstance(expr, (list, tuple)) else 0)


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    if(len(index) > 1):
        return tree_ref(tree[index[0]], index[1:])
    else:
        return tree[index[0]]



# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
