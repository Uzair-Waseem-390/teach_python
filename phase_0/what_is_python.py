# What is Python?

"""
Python is a high-level, general-purpose, interpreted programming language
created by Guido van Rossum, first released in 1991.

It was designed with a strong focus on CODE READABILITY - meaning Python
code often looks close to plain English, and uses indentation (not curly
braces {}) to define blocks of code.

Fun fact: Python is NOT named after the snake - it's named after the British
comedy show "Monty Python's Flying Circus," which Guido van Rossum was a fan of.
"""


# Key characteristics of Python
"""
1. High-level        -> you don't manage memory or hardware details yourself
2. Interpreted        -> code runs line-by-line through an interpreter
                          (more detail in translators.py)
3. Dynamically typed   -> you don't have to declare a variable's data type,
                          Python figures it out automatically at runtime
4. Beginner-friendly    -> clean, readable syntax, close to plain English
5. General-purpose      -> not limited to one domain, used almost everywhere
                          (web, data science, AI, automation, games, etc.)
6. Huge ecosystem        -> massive collection of libraries/frameworks for
                          almost any task (covered more in scope_of_python.py)
"""


# Why are WE learning Python (as a first language)?
"""
1. Easiest syntax to start with - close to how you'd describe steps in English
2. Huge community - if you get stuck, chances are someone already asked
   your exact question online
3. Extremely versatile - the same language you're learning now can build
   websites, automate tasks, analyze data, or build AI models
4. In high demand in the job market across many different fields
5. A great language for building strong PROBLEM-SOLVING skills, which matters
   more than syntax - once you understand programming logic here, learning a
   second language (like JavaScript or Java) later becomes much easier
"""


# A tiny taste of Python's readability (just to see it, not to fully understand it yet)
if True:
    print("Notice how this reads almost like a plain English sentence")

# Compare that same idea's basic shape in a language like C or Java, which needs
# extra symbols like semicolons ; and curly braces { } to define the same block.
# Python intentionally removes that visual clutter.


# History of Python - How It Came to Be
"""
Python wasn't built by a company or a committee - it started as one person's
side project.

Late 1980s (Origins):
    Guido van Rossum, a Dutch programmer working at CWI (a research institute
    in the Netherlands), was working with a language called ABC. ABC was
    designed to be easy to learn, but it had limitations and never took off.
    Guido liked ABC's readability but wanted something more practical and
    extensible.

    Over Christmas in 1989, looking for a hobby project to keep himself busy
    during the holidays, Guido started designing a new language that combined
    ABC's readability with better support for real programming tasks like
    handling errors and working with different systems.

1991 (First Release):
    Python 0.9.0 was released publicly. It already had many features Python
    is known for today: functions, exception handling, and core data types
    like list, str, and dict.

1994 (Python 1.0):
    The first fully-featured version. Added functional programming tools
    like lambda, map, filter, and reduce.

2000 (Python 2.0):
    Introduced list comprehensions and a cycle-detecting garbage collector.
    This is the version that saw Python's community and adoption grow rapidly.

2008 (Python 3.0):
    A intentionally backward-incompatible redesign to fix long-standing
    design flaws in the language (e.g. how text/strings were handled).
    This caused a long, sometimes painful transition period, since Python 2
    and Python 3 code weren't always compatible with each other.

2020 (Python 2 Retired):
    Python 2 officially reached its "end of life" - no more updates or
    security fixes. The entire ecosystem fully shifted to Python 3, which
    is what you are learning today.
"""


# How and why Python became a mature BACKEND programming language
"""
Python wasn't originally built with "web backend development" as its main
goal - but a combination of its design and community growth made it a
natural fit for server-side development over time:

1. Readable syntax lowered the barrier to entry
   Because Python code is easy to read and write, more developers picked it
   up quickly, which grew the community and the number of tools built for it.

2. "Batteries included" philosophy
   Python ships with a large STANDARD LIBRARY out of the box (for handling
   files, networking, dates, JSON, etc.), so developers didn't have to build
   everything from scratch to get a server running.

3. Web frameworks matured the ecosystem
   - Django (2005) arrived as a full "batteries-included" web framework,
     handling databases, authentication, security, and more, letting
     companies build production-grade websites fast and safely.
   - Flask (2010) offered a lightweight, flexible alternative for smaller
     apps and APIs.
   - FastAPI (2018) brought modern, high-performance API development with
     built-in data validation, becoming extremely popular for backend APIs.

4. Strong integration with databases and other systems
   Python has mature libraries for connecting to almost every database and
   external service, making it practical for real-world backend systems
   that need to talk to many other pieces of infrastructure.

5. Adoption by major companies proved it could scale
   Companies like Instagram, Spotify, Dropbox, YouTube, and Pinterest built
   large parts of their backend systems using Python, proving it could
   handle serious, large-scale, production traffic - not just scripts and
   small projects. This real-world validation is a big part of why Python
   is trusted as a "mature" backend choice today, not just a beginner language.

6. The rise of APIs and microservices
   As the industry moved toward REST APIs and microservices architecture,
   Python's frameworks (especially FastAPI and Flask) fit perfectly into
   this style of building backend systems - lightweight, fast to develop,
   and easy to connect to other services.

In short: Python matured as a backend language not because it was DESIGNED
for that purpose from day one, but because its readability attracted a huge
developer community, that community built powerful frameworks and libraries
around it over 20+ years, and major companies proved at scale that it could
handle real production workloads.
"""


# Who created Python and is it still actively maintained?
"""
Python was created by Guido van Rossum and first released in February 1991.
It is FREE and OPEN SOURCE, meaning anyone can use it, and it's maintained by
the Python Software Foundation along with a massive open-source community.
It continues to receive regular updates - Python 3 is the current actively
developed version (Python 2 was officially retired/end-of-life in 2020).
"""