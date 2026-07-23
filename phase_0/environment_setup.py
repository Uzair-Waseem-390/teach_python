# Environment Setup - Getting Python Ready on Your Computer

# Before you can run a single line of Python, you need two things:
#   1. Python itself installed on your computer (the interpreter)
#   2. A place to actually WRITE your code (a text editor / IDE)
# This file walks through both, plus how to confirm everything works.


# 1. Installing Python
"""
Download Python from the OFFICIAL source only: https://www.python.org/downloads/
Avoid random third-party download sites.

Windows:
    - Download the installer from python.org
    - IMPORTANT: On the first screen of the installer, check the box that
      says "Add Python to PATH" before clicking Install. Skipping this is
      the #1 reason beginners get a "python is not recognized" error later.

macOS:
    - macOS often comes with an old, outdated Python version pre-installed.
      Download and install the latest version from python.org instead.
    - Alternatively, many developers use Homebrew: brew install python

Linux:
    - Most distributions already come with Python 3 installed.
    - You can install/update it via your package manager, e.g.:
      sudo apt install python3     (Debian/Ubuntu)
"""


# 2. Verifying the installation
"""
Open your terminal (Command Prompt / PowerShell on Windows, Terminal on
macOS/Linux) and run:

    python --version
    (or on some systems: python3 --version)

You should see something like:  Python 3.12.x

If you get an error like "command not found" or "not recognized", Python
either isn't installed correctly, or wasn't added to your system's PATH
(see the Windows note above).
"""


# 3. What is pip?
"""
pip is Python's built-in PACKAGE MANAGER - it lets you install extra
libraries/tools that don't come with Python by default (for example, later
you'll use it to install libraries like requests, pandas, or Django).

Check that pip is installed and working:
    pip --version

Installing a package looks like this (just an example, don't run it yet):
    pip install requests
"""


# 4. Choosing where to write your code (Text Editor vs IDE)
"""
Text Editor:
    A lightweight tool for writing code. Fast to open, minimal extra features
    out of the box, but can be extended with plugins.
    Example: VS Code (with the right extensions, it behaves like a full IDE)

IDE (Integrated Development Environment):
    A full-featured application built specifically for writing, running, and
    debugging code, usually with more built-in tools (debugger, project
    management, code suggestions) right out of the box.
    Example: PyCharm

For beginners, the two most common recommendations are:
    - VS Code (free, lightweight, install the official "Python" extension
      from Microsoft for syntax highlighting, running code, and debugging)
    - PyCharm Community Edition (free, more built-in features specifically
      for Python, slightly heavier to run)

Either is a completely fine choice - what matters most right now is picking
ONE and getting comfortable with it, not which one is "better."
"""


# 5. Running your first Python file
"""
Once Python and an editor are installed:
    1. Create a new file and save it with a .py extension, e.g. hello.py
    2. Write one line of code inside it:
           print("Hello, World!")
    3. Run it from the terminal by navigating to the file's folder and typing:
           python hello.py
       (or python3 hello.py on macOS/Linux)
    4. You should see the text: Hello, World!  printed in your terminal

Most editors (like VS Code) also have a built-in "Run" button that does the
same thing without needing to type the command manually - useful once you're
comfortable, but knowing the terminal command matters too, since not every
environment will have a convenient Run button (e.g. running code on a server).
"""


print("Hello, World!")


# 6. What is a virtual environment (a quick heads-up, covered in more depth later)
"""
A virtual environment is an ISOLATED workspace for a Python project, with
its own separate set of installed packages, so different projects don't
interfere with each other's dependencies.

You don't need to fully understand or use this yet as a complete beginner,
but the command to be aware of for later is:
    python -m venv venv_name

This will come up again once you start working on larger, multi-file projects.
"""