# 📊 PATTERN GENERATOR AND NUMBER ANALYZER

Welcome to the **Pattern Generator and Number Analyzer**! This is a simple, beginner-friendly Python command-line tool that lets you create visual star patterns and analyze ranges of numbers.

---

## 🎯 PROJECT FEATURES (What it Does)

This application provides three straightforward options in an interactive menu:

* **1️⃣ Generate a Pattern:** Creates a right-angled triangle made of stars (*) based on how many rows you request.
* **2️⃣ Analyze Numbers:** Looks at a range of numbers you choose, tells you if each number is Odd or Even, and calculates their total sum.
* **3️⃣ Exit:** Safely closes the program.

---

## 🔍 STEP-BY-STEP CODE EXPLANATION

Here is exactly how each part of the project works behind the scenes:

### 🔄 The Main Menu Loop (while True)

* **What it does:** It keeps the program running in a continuous loop so you don't have to restart it after every task.
* **How it works:** It displays the menu choices over and over until you explicitly type 3 to exit.

### ✨ OPTION 1: PATTERN GENERATOR LOGIC

* **Input Check:** The code uses a built-in check (.isdigit) to make sure you typed a real positive number. If you type letters or symbols, it shows an error message instead of crashing.
* **The Loops:** It uses a while loop combined with a for loop. The outer loop moves down line-by-line, while the inner loop prints the correct number of stars (*) on that specific line.

### 🧮 OPTION 2: NUMBER ANALYZER LOGIC

* **Safe Reading (try-except):** It uses a safety block to read your start and end numbers. This allows the program to accept negative numbers safely without breaking.
* **Range Validation:** It checks if your "end" number is actually bigger than or equal to your "start" number.
* **Odd/Even Check (% 2):** It divides each number in your range by 2. If the remainder is 0, it labels it Even. Otherwise, it labels it Odd.
* **Total Counter:** It keeps adding every number in the loop into a variable called total_sum to give you the grand total at the very end.

### 🚪 OPTION 3 & FALLBACK LOGIC

* **The Exit:** Typing 3 triggers a break command, which stops the infinite loop and closes the program nicely.
* **The Mistake Catcher (else):** If you type anything else (like 5 or hello), the program politely tells you it's an invalid choice and brings you right back to the main menu.

---

## 💻 SAMPLE OUTPUT
### 🔹 Pattern Generator (If you input 4)
* 
* * 
* * * 
* * * *
* * * * *

### 🔹 Number Analyzer (If range is 1 to 3)

Number 1 is Odd
Number 2 is Even
Number 3 is Odd

## 🚀 HOW TO RUN PROJECT

Follow these quick steps to get the program running on your computer:

### 📋 PREREQUISITES

Make sure you have Python installed on your system. You can download it from the official python website.

### 🛠️ EXECUTION STEPS

1. **Save the Code:** Copy your Python code and save it in a file named main.py.
2. **Open Terminal:** Open your Command Prompt (Windows) or Terminal (Mac/Linux).
3. **Navigate to Folder:** Go to the folder where you saved your file using the cd command (e.g., cd Documents/PythonProjects).
4. **Run the Script:** Type the command **python main.py** and press Enter.

# CODE
<img width="835" height="352" alt="Screenshot 2026-05-25 195444" src="https://github.com/user-attachments/assets/069e4c17-4953-4131-b8bf-352ea768a2f4" />
<img width="724" height="897" alt="Screenshot 2026-05-25 195425" src="https://github.com/user-attachments/assets/9d1a7f35-71af-49b0-8fb1-9dcc4f189785" />
