# Translators (Compiler, Interpreter, Assembler)

# A computer's processor only understands machine code (binary: 0s and 1s).
# Since we write code in high-level languages like Python, we need a
# TRANSLATOR PROGRAM to convert our human-readable code into machine code
# the computer can actually execute.


# 1. Compiler
"""
A compiler translates the ENTIRE source code into machine code (or another
lower-level form) all at ONCE, BEFORE the program runs. This produces a
separate output file (an executable) that can be run directly, any number
of times, without needing the compiler again.

Process:  Source Code  --[Compiler]-->  Executable File  -->  Run

Characteristics:
    - If there's an error, the compiler reports it before anything runs at all
    - Once compiled, the program generally runs FAST since translation is
      already done
    - You must RE-COMPILE every time you change the code

Examples of compiled languages: C, C++, Rust, Go
"""


# 2. Interpreter
"""
An interpreter translates and EXECUTES source code line-by-line, on the fly,
each time you run the program. There's no separate standalone executable
produced - you always need the interpreter present to run the code.

Process:  Source Code  --[Interpreter reads + runs line by line]-->  Output

Characteristics:
    - Errors are only found WHEN that specific line is reached during execution
    - Easier and faster to test small changes (no separate compile step)
    - Generally somewhat SLOWER than compiled code, since translation happens
      every time the program runs

Examples of interpreted languages: Python, JavaScript, Ruby, PHP
"""


# 3. Assembler
"""
An assembler is a specialized translator that converts Assembly Language
(human-readable mnemonics like MOV, ADD, JMP) directly into machine code.
It's a much simpler, more direct translation than a compiler, since assembly
language is already very close to machine code, just written in short words
instead of pure binary.

Process:  Assembly Code  --[Assembler]-->  Machine Code
"""


# So... is Python compiled or interpreted?
"""
Technically, Python does BOTH:
    1. Your .py source code is first compiled into an intermediate form
       called BYTECODE (this happens automatically, you don't do it manually)
    2. That bytecode is then run by the Python Interpreter (called CPython
       in the most common implementation), which executes it line by line

This is why Python is usually called an "interpreted language" - the bytecode
compilation step is invisible to you as a beginner, and the interpreter is
what actually runs your code, giving you that immediate "run and see results"
experience typical of interpreted languages.
"""


# Compiler vs Interpreter - quick comparison
"""
Aspect              Compiler                       Interpreter
Translation         All at once, before running     Line-by-line, while running
Output               Separate executable file          No separate file produced
Error detection      Before the program runs at all     Only when that line executes
Speed                Faster to RUN (already translated)  Slower to run (translates each time)
Examples             C, C++, Rust                        Python, JavaScript, Ruby
"""