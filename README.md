**0x00. AirBnB clone - The console**
---
- This is the first step towards building first full web application: the AirBnB clone

he AirBnB Clone project is replicate simplified version of the well known vacation rental plantform. It aims at providing the basic implementatio of the AirBnB concept, permiting users to create, manage and interact with various objects such as users, states and cities

This project consists of a command line based application which serves as the simplified front-end interface for managing AirBnB series of projects. It includes a custom command interpreter that permits users to perform actions like creating, updating and viewing different objects.

Command Interpreter

This is the main component of the AirBNB Clone project. it provides a text-based interface for interacting with the application and its objects. It supports both interactive and non-interactive modes.

How to start the Command Interpreter:

1. Clone the repository from Github into your local machine
2. Open a terminal and navigate to the project directory
3. Execute the main file (console.py) scrip as follows:

# ./console.py

How to use it:

One the intepreter is running you will see the prompt (hbnb), then you can interact with it by entering various commands. The syntax is as follows:

(hbnb) (command) (options)

Example commands:

* 'create': creates a new instance of an object
* 'show': displays details of an object
* 'update': update attributes of an object
* 'all': display all instances of a specific class
* 'quit': exits the command interpreter

Examples

* Create a new User:
(hbnb) create User

* Show User details:
(hbnb) show User 3456

* Update the name of a User:
(hbnb) update User 3456 first_name "Musa"

* Display all instances of a class:
(hbnb) all User

* Quit command interpreter:
(hbnb) quit

The command line has both interactive and non-interactive modes:

Interactive Mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

Non-Interactive Mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
