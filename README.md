# PyFileX

**PyFileX** is a file manager developed in Python.

The project starts as a command-line application and progressively evolves into a graphical file manager using Tkinter.

The main purpose of the project is both **practical and educational**: learning how Python interacts with the operating system and mastering file and directory manipulation through `pathlib` and `os`.

---

## 🚀 Project objectives

PyFileX aims to provide a progressively complete file-management system capable of:

* navigating through directories;
* creating files and directories;
* renaming files and directories;
* copying and moving files;
* deleting files and directories;
* searching for files;
* automatically organizing files;
* creating backups;
* monitoring directories;
* analyzing disk usage;
* providing a complete CLI;
* eventually providing a Tkinter graphical interface.

---

## 🛠️ Technologies

### Core

* Python 3
* pathlib
* os

### Standard Python libraries introduced progressively

* shutil
* datetime
* time
* json
* logging

### Future

* Tkinter

No external dependency is required for the core file-management functionality.

---

## 📈 Development roadmap

### Level 1 — Basic file management

Introduction to:

* files;
* directories;
* paths;
* creation;
* deletion;
* renaming;
* existence checks.

### Level 2 — File-system navigation

Implementation of:

```text
pwd
ls
cd
back
tree
```

### Level 3 — Automatic organization

Files are automatically classified according to their extensions.

Example:

```text
.jpg  → Images/
.pdf  → Documents/
.mp3  → Music/
.py   → Code/
.mp4  → Videos/
```

### Level 4 — Backup system

Creation of dated backups of selected directories.

### Level 5 — Directory monitoring

Detection and processing of new files appearing inside a monitored directory.

### Level 6 — Storage analysis

Analysis of:

* file sizes;
* directory sizes;
* largest files;
* total storage usage.

### Level 7 — Complete CLI

Integration of all previous features into a coherent command-line file manager.

### Level 8 — Tkinter GUI

A graphical interface will be developed after the CLI version has been completed.

---

## 📁 Planned architecture

The architecture will evolve throughout development.

Initial version:

```text
pyfilex/
└── main.py
```

Target architecture:

```text
pyfilex/
│
├── main.py
├── fileManager.py
├── Navigation.py
├── Search.py
├── Organizer.py
├── Backup.py
├── Analyzer.py
├── Monitor.py
├── commands.py
├── utils.py
│
├── logs/
│
├── tests/
│
└── README.md
```

The final architecture may change as the project grows.

---

## 🎯 Learning goals

This project is also a practical Python learning path.

During development, the following concepts will be studied:

* variables;
* conditions;
* loops;
* functions;
* modules;
* exceptions;
* file handling;
* paths;
* recursion;
* object-oriented programming;
* classes;
* encapsulation;
* static methods;
* class methods;
* decorators;
* command-line interfaces;
* graphical interfaces.

---

## 🔎 pathlib

PyFileX gives particular importance to `pathlib`.

Examples of methods explored during the project:

```python
Path.cwd()
Path.home()
Path.exists()
Path.is_file()
Path.is_dir()
Path.iterdir()
Path.glob()
Path.rglob()
Path.mkdir()
Path.touch()
Path.rename()
Path.unlink()
Path.stat()
```

---

## 🖥️ os

The project will also explore the `os` module in order to understand how Python interacts with the operating system.

Examples:

```python
os.getcwd()
os.chdir()
os.listdir()
os.mkdir()
os.makedirs()
os.rename()
os.remove()
os.rmdir()
os.walk()
```

The project will compare equivalent operations between `pathlib` and `os`.

---

## ⚠️ Safety

PyFileX manipulates real files and directories.

For this reason, development and testing should initially be performed inside a dedicated test directory.

Example:

```text
PyFileX_Test/
├── Documents/
├── Images/
├── Music/
└── Videos/
```

Avoid testing deletion features directly on important personal directories.

---

## 📌 Project status

Current stage:

```text
[ ] Level 1 — Basic file management
[ ] Level 2 — Navigation
[ ] Level 3 — Automatic organization
[ ] Level 4 — Backup
[ ] Level 5 — Monitoring
[ ] Level 6 — Storage analysis
[ ] Level 7 — Complete CLI
[ ] Level 8 — Tkinter GUI
```

---

## 👨‍💻 Author

**Rom**

Student in Computer Science.

This project is developed as a progressive Python learning and software-engineering project.

---

## 📄 License

This project will receive a license as the repository matures.
