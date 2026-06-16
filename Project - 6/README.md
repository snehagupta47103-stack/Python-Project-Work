<div align="center">

# 📔 Personal Journal Manager

### *Interactive File-Based Journal Management System using Python & OOP*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-FF6F00?style=for-the-badge)
![File Handling](https://img.shields.io/badge/File%20Handling-Read%20Write%20Search-4CAF50?style=for-the-badge)
![CLI](https://img.shields.io/badge/Console-Interactive%20CLI-9C27B0?style=for-the-badge)

<br/>

> *"Every thought deserves a place to be remembered."*

</div>

---

# 📋 Table of Contents

* 📌 Overview
* 🎯 Problem Statement
* ✨ Key Features
* 🏗️ Project Structure
* 🔄 Project Workflow
* 📔 Journal Entry Management
* 🔍 Search Functionality
* 🗑️ Delete Functionality
* 🛠️ Tech Stack
* 📈 Results & Insights
* 🏆 Advantages
* 📄 License
* 🙏 Acknowledgements

---

# 📌 Overview

**Personal Journal Manager** is a menu-driven Python application that allows users to maintain a personal digital journal using file handling techniques and Object-Oriented Programming (OOP).

The application enables users to:

* Add journal entries with timestamps
* View all saved entries
* Search entries using keywords or dates
* Delete all entries after confirmation
* Store data permanently using text files

This project demonstrates practical implementation of:

* File Handling
* Object-Oriented Programming
* Exception Handling
* User Input Validation
* Menu-Driven Program Design

---

# 🎯 Problem Statement

### Objective

Develop a console-based journal management system that allows users to create, store, search, view, and delete journal entries while ensuring data persistence through file handling.

The application should:

| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| Add Entry          | Save journal notes with timestamps   |
| View Entries       | Display all stored journal entries   |
| Search Entry       | Find entries using keywords or dates |
| Delete Entries     | Remove all journal records           |
| Persistent Storage | Store data in a text file            |

The goal is to provide a simple yet efficient personal journaling solution while demonstrating fundamental Python programming concepts.

---

# ✨ Key Features

| Feature                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| 📝 Timestamped Entries     | Automatically records date and time           |
| 📂 File-Based Storage      | Stores entries permanently in a text file     |
| 🔍 Smart Search            | Search by keyword or date                     |
| 👀 View All Entries        | Displays complete journal history             |
| 🗑️ Delete Journal         | Removes all entries after confirmation        |
| 🧩 OOP Design              | Organized using a JournalManager class        |
| ⚠️ Exception Handling      | Handles file and permission errors            |
| 🔄 Menu-Driven Interface   | Easy-to-use command-line interface            |
| 📅 Automatic Time Tracking | Uses current system date and time             |
| 💾 Persistent Data Storage | Data remains available after program restarts |

---

# 🏗️ Project Structure

📦 Project-6/

│
├── 📄 Project-6.py          ← Main Python Script
│
└── 📄 README.md             ← Project Documentation

---

# 🔄 Project Workflow

```text
Program Start
      │
      ▼
┌─────────────────────────────┐
│ Display Main Menu           │
└─────────────┬───────────────┘
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Add Entry  View     Search
              │         │
              ▼         ▼
        Read Journal  Find Match
              │
              ▼
        Display Result
              │
              ▼
      Delete Entries?
              │
         Yes / No
              │
              ▼
      Return to Menu
              │
              ▼
            Exit
```

---

# 📔 Journal Entry Management

## 📝 Add New Entry

Users can add personal journal entries through the console.

Each entry is automatically stored with:

* Current Date
* Current Time
* User's Journal Text

### Example Format

```text
[2026-06-16 13:01:44]
I am a Data Analyst.
```

### Concepts Used

* append mode (`a`)
* datetime module
* file creation
* user input handling

---

## 👀 View All Entries

Displays all stored journal records from the journal file.

### Example Output

```text
Your Journal Entries:
------------------------------

[2026-06-16 12:29:38]
I am sneha gupta student of data analyst.

[2026-06-16 13:01:44]
I am a Data Analyst.
```

### Concepts Used

* read mode (`r`)
* file existence checking
* content display

---

# 🔍 Search Functionality

Users can search journal entries using:

* Keywords
* Dates
* Partial Text

### Search Example

```text
Enter a keyword or date to search:
Data Analyst
```

### Matching Output

```text
Matching Entries:
------------------------------

[2026-06-16 12:29:38]
I am sneha gupta student of data analyst.

[2026-06-16 13:01:44]
I am a Data Analyst.
```

### Logic Used

```python
if keyword.lower() in entry.lower():
```

This allows case-insensitive searching throughout all journal entries.

---

# 🗑️ Delete Functionality

Users can remove all journal records after confirmation.

### Confirmation Prompt

```text
Are you sure you want to delete all entries? (yes/no)
```

### Successful Output

```text
All journal entries have been deleted.
```

### Concepts Used

* os.remove()
* confirmation validation
* file deletion handling

---

# ⚠️ Exception Handling

The application handles common runtime errors gracefully.

| Exception         | Purpose                     |
| ----------------- | --------------------------- |
| FileNotFoundError | Journal file does not exist |
| PermissionError   | Access denied to file       |
| Exception         | Handles unexpected errors   |

### Benefits

* Prevents application crashes
* Improves reliability
* Enhances user experience

---

# 🧠 Object-Oriented Programming (OOP)

The project follows an Object-Oriented approach.

### Class Used

```python
class JournalManager:
```

### Methods

```python
add_entry()
view_all_entries()
search_entry()
delete_all_entries()
```

### OOP Advantages

* Better code organization
* Easy maintenance
* Reusability
* Scalability

---

<img width="1206" height="802" alt="Screenshot 2026-06-16 123158" src="https://github.com/user-attachments/assets/599311cd-121f-4afc-99ef-302ba448deaf" />
<img width="1112" height="869" alt="Screenshot 2026-06-16 123250" src="https://github.com/user-attachments/assets/863da3e9-cb36-4047-b524-b95d01c6488b" />
<img width="1289" height="887" alt="Screenshot 2026-06-16 123324" src="https://github.com/user-attachments/assets/bbcd6be7-48a7-4894-882a-10d0e2478ef7" />
<img width="1202" height="796" alt="Screenshot 2026-06-16 123353" src="https://github.com/user-attachments/assets/6c3bf02a-e1f9-47fa-92eb-940381945658" />
<img width="1006" height="908" alt="Screenshot 2026-06-16 123419" src="https://github.com/user-attachments/assets/b1faff08-67da-40e2-9e4f-4a0b5acacd1c" />
<img width="1280" height="729" alt="Screenshot 2026-06-16 123447" src="https://github.com/user-attachments/assets/fe51a3e7-4be8-4a1a-8d2a-a9d33057b68b" />

---

# 🛠️ Tech Stack

| Tool               | Purpose               |
| ------------------ | --------------------- |
| 🐍 Python 3.8+     | Programming Language  |
| 📂 File Handling   | Data Storage          |
| 🧩 OOP             | Application Structure |
| 📅 datetime Module | Timestamp Generation  |
| 🗑️ os Module      | File Operations       |
| 🖥️ CLI Interface  | User Interaction      |

---

# 📈 Results & Insights

After successful execution, the application provides:

✅ Journal entries saved permanently

✅ Automatic timestamp generation

✅ Fast keyword-based search

✅ Complete journal viewing capability

✅ Safe journal deletion with confirmation

✅ Error handling for missing files

✅ User-friendly menu navigation

✅ Persistent storage across program runs

---

# 🏆 Advantages

| Advantage             | Detail                                |
| --------------------- | ------------------------------------- |
| 🎓 Beginner Friendly  | Easy to understand and implement      |
| 📂 Real File Handling | Practical use of file operations      |
| 🧩 OOP Based          | Demonstrates class-based design       |
| 🔍 Efficient Search   | Quick keyword matching                |
| 💾 Persistent Storage | Data remains after execution          |
| ⚡ Lightweight         | No external libraries required        |
| 🔄 Extensible         | Easy to add update/edit functionality |
| 🛡️ Reliable          | Includes exception handling           |

---

# 🚀 Future Enhancements

Possible future improvements include:

* ✏️ Edit Existing Entries
* 🏷️ Category-Based Journals
* 📅 Search by Date Range
* 🔐 Password Protection
* 📊 Journal Statistics
* 🖼️ Graphical User Interface (GUI)
* ☁️ Cloud Backup Support

---

# 📄 License

This project is licensed under the MIT License.

```text
MIT License

Free to use, modify, and distribute with attribution.
```

---

# 🙏 Acknowledgements

Special thanks to the following learning resources:

* Python Official Documentation
* Real Python
* GeeksForGeeks
* W3Schools
* Stack Overflow Community
* Python Developer Community

---

<div align="center">

## 👤 Author

### Project Developer

> *"Every journal entry captures a moment, every line of code preserves it."*

**🎓 Role:** Python Developer | Programming Learner  
**🛠️ Skills:** Python · OOP · File Handling · Exception Handling · CLI Applications

</div>

<div align="center">

### 📔 Personal Journal Manager

*"Write today. Remember tomorrow."*

Made with ❤️ using Python

</div>
