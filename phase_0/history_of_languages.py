# History of Programming Languages

# Understanding how programming languages evolved helps you understand WHY
# modern languages like Python look and behave the way they do.


# Generation 1: Machine Language (1940s)
"""
The very first "programs" were written directly in BINARY (0s and 1s) -
the only language the hardware understood directly.

Example: 10110000 01100001

Problems:
    - Extremely hard to write and read
    - Different for every type of machine (not portable)
    - One tiny mistake could break the entire program, and it was hard to find
"""


# Generation 2: Assembly Language (1950s)
"""
Assembly language replaced raw binary with short human-readable MNEMONICS
(abbreviated words) that map directly to machine instructions.

Example: MOV A, 5   (move the value 5 into register A)

This was easier for humans than pure binary, but it needed a special program
called an ASSEMBLER to translate it into machine code (covered in translators.py).
Still very low-level and hardware-specific.
"""


# Generation 3: High-Level Languages (1950s - 1970s)
"""
This is where languages started looking more like ENGLISH / MATH.

Key milestones:
    - FORTRAN (1957)  -> designed for scientific/mathematical calculations
    - COBOL (1959)    -> designed for business applications
    - C (1972)         -> extremely influential, still used today, gave rise
                          to C++, Java, C#, and heavily influenced Python's syntax

High-level languages need a COMPILER or INTERPRETER to convert the code into
machine language, but they made programming dramatically more accessible -
you no longer needed to think in terms of hardware registers.
"""


# Generation 4 and beyond: Modern High-Level & Scripting Languages (1980s - present)
"""
Languages got even more human-friendly, abstracted away more hardware detail,
and focused on developer productivity:

    - Python (1991)       -> created by Guido van Rossum, focus on readability
    - Java (1995)          -> "write once, run anywhere" philosophy
    - JavaScript (1995)     -> the language of the web browser
    - Go (2009), Rust (2010), Kotlin (2011), Swift (2014) -> modern languages
      solving modern problems (performance + safety + simplicity)
"""


# The general trend across history
"""
Binary  ->  Assembly  ->  High-Level Languages (C, Fortran)  ->  Modern
Languages (Python, JavaScript, Go...)

Each step moved AWAY from "how the hardware works" and TOWARD "how humans
think." Python sits very far on the human-friendly end of this timeline -
which is exactly why it's a great first language to learn.
"""


# A quick timeline summary
"""
Year    Language        Milestone
1957    FORTRAN         First widely-used high-level language
1959    COBOL           Business-oriented language
1972    C                Hugely influential systems language
1983    C++              Added Object-Oriented Programming to C
1991    Python           Focus on readability and simplicity
1995    Java             "Write once, run anywhere"
1995    JavaScript       Brought programming to the web browser
2009    Go               Simplicity + performance for modern servers
"""