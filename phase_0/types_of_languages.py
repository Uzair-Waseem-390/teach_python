# Types of Programming Languages

# Programming languages can be classified in several different ways.
# We'll look at the most important classifications a beginner should know.


# 1. Classification by Level of Abstraction
"""
Low-Level Languages:
    - Closer to the hardware / machine
    - Examples: Machine Language, Assembly Language
    - Hard for humans to read, but very fast and gives full hardware control

High-Level Languages:
    - Closer to human language, abstracted away from hardware details
    - Examples: Python, Java, C++, JavaScript
    - Easier for humans to read/write, more portable across different machines
    - Python is a HIGH-LEVEL language
"""


# 2. Classification by Execution Method
"""
Compiled Languages:
    - Entire source code is translated into machine code BEFORE running,
      producing a separate executable file
    - Examples: C, C++, Rust
    - Generally faster to run, but you must recompile after every change

Interpreted Languages:
    - Code is translated and executed line-by-line, at the time you run it,
      without producing a separate standalone executable first
    - Examples: Python, JavaScript, Ruby
    - Easier to test and debug quickly, generally a bit slower than compiled code
    - Python is an INTERPRETED language (technically Python compiles to an
      intermediate "bytecode" first, then an interpreter runs that bytecode -
      more detail on this in translators.py)
"""


# 3. Classification by Programming Paradigm
"""
Procedural Languages:
    - Code is organized as a sequence of instructions / procedures (functions)
    - Examples: C, early Python-style scripts

Object-Oriented Languages:
    - Code is organized around "objects" that bundle data and behavior together
    - Examples: Java, C++, Python (Python supports this - covered in Phase 6)

Functional Languages:
    - Code is organized around pure functions and avoiding changing state
    - Examples: Haskell, Lisp (Python supports SOME functional-style features
      too, like lambda, map(), filter())

Python is a MULTI-PARADIGM language - it supports procedural, object-oriented,
AND functional programming styles, which is part of why it's so flexible.
"""


# 4. Classification by Typing
"""
Statically Typed:
    - Variable types are fixed and checked BEFORE the program runs
    - Examples: Java, C, C++
    - Example: int age = 20;   (type must be declared)

Dynamically Typed:
    - Variable types are determined automatically WHILE the program runs
    - Examples: Python, JavaScript
    - Example: age = 20        (no type declaration needed, Python infers it)

Python is DYNAMICALLY typed.
"""


# Quick summary table
"""
Classification            Python is...
Level of Abstraction       High-Level
Execution Method            Interpreted (with compiled bytecode step)
Programming Paradigm         Multi-paradigm (Procedural + OOP + Functional)
Typing                        Dynamically Typed
"""