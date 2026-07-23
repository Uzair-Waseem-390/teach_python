# What is Programming?

# A computer is a machine. Machines don't "think" - they only follow instructions.
# Programming is the process of giving a computer a set of clear, step-by-step
# instructions to perform a task.
#
# Example (in plain English, not code):
#   1. Ask the user for two numbers
#   2. Add the two numbers together
#   3. Show the result to the user
#
# A "program" is simply this list of instructions, written in a language the
# computer can understand and follow.


# What is a Programming Language?
"""
A programming language is a formal set of rules (syntax + grammar) that lets
humans write instructions for a computer to execute.

Just like English or Urdu is a language for humans to communicate with each
other, a programming language is a language for a HUMAN to communicate with
a COMPUTER.

Examples of programming languages: Python, Java, C, C++, JavaScript, Go, Rust.

Every programming language has:
    1. Syntax    -> the exact rules of how to write valid code (grammar)
    2. Semantics -> what that code actually MEANS / does when it runs
    3. Keywords  -> reserved words with special meaning (if, for, while, etc.)
"""


# Why can't we just talk to computers in plain English?
"""
Human language (English, Urdu, etc.) is full of AMBIGUITY.
Example: "I saw the man with the telescope."
    - Did I use a telescope to see the man?
    - Or did the man have a telescope?

A human can usually figure out the intended meaning using context. A computer
CANNOT. Computers need PRECISE, UNAMBIGUOUS instructions - this is exactly
what programming languages are designed to provide.
"""


# What does a computer actually understand?
"""
At the lowest level, a computer's processor only understands BINARY:
sequences of 0s and 1s (called machine code / machine language).

Example of machine code (meaningless to a human):
    01001000 01100101 01101100 01101100 01101111

Writing everything in binary would be extremely slow and error-prone for
humans. That's exactly why programming languages like Python exist - they
let us write instructions in a form that's readable to humans, which then
gets converted (translated) into machine code the computer can execute.
This translation process is covered later in translators.py.
"""


# Programming vs Coding vs Software Development (common confusion)
"""
Coding       -> the ACT of writing lines of code / instructions
Programming  -> a broader process that includes coding, PLUS designing the
                logic, planning the steps, and solving the problem
Software
Development  -> the full lifecycle: planning, designing, coding, testing,
                debugging, deploying, and maintaining a complete application

In short: coding is a subset of programming, and programming is a subset of
software development.
"""