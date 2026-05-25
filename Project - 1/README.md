# Project - 1
This is my Python project.
# 📋 Personal Data Collector
Welcome to the Personal Data Collector! 🎉 This is a clean, interactive, terminal-based Python application designed to safely gather user inputs, process them instantly, and reveal exactly how Python handles data behind the scenes.

It is a fantastic educational tool for seeing how a computer reads your text, calculates numbers, converts data formats, and even tracks memory storage in real time! It is super lightweight, fast, and easy to run. 🚀

# ✨ Features
📥 Interactive Inputs: Seamlessly collects your name, age, height, and favorite number right from the console.

🧠 Smart Calculations: Automatically estimates your birth year by performing math on the age you provide.

🔍 Behind-the-Scenes Peek: Displays the exact data type and unique system memory tracking ID for every single input.

🔢 Smart Rounding: Safely converts decimal heights into whole numbers to show data conversion and truncation in action.

# 🔍 Detailed Data & Code Breakdown
The program collects four specific pieces of information from you. Here is exactly what the code does with each data point step-by-step:

👤 The Name Input (name)
When you enter your name, the program stores it as a text string (str). Because it is a string, Python treats it as literal text characters rather than a value to do math with. The program reads your name, remembers it, and assigns it a unique memory location ID in your system's RAM.

🎂 The Age Input & Birth Year (age)
When you type your age, the program immediately uses int() to convert the text into a whole number (an integer). This is a crucial step because it allows the program to perform math! It takes the base year (2023 in the code) and subtracts your age to estimate your approximate birth year, proving how raw user input can be turned into fresh, calculated data.

📏 The Height Input & Rounding (height)
Your height is captured using float(), which allows the program to accept decimal numbers (like 1.68 meters). To demonstrate data manipulation, the code later forces this decimal into a whole integer using int(height). This process chops off the decimal points entirely (turning 1.68 into 1), showing how programming languages truncate numbers when changing data formats.

⭐ The Favorite Number (fav_num)
Just like your age, your favorite number is saved as a whole integer (int). By printing out the data type and memory ID for this number alongside your age, the program beautifully demonstrates how Python allocates different spaces in your computer's memory for different numbers, even if they are entered right after one another.

🧠 Memory Tracking (id())
Every time the program prints out a long string of numbers at the end, it is showing you the id(). This is the literal, unique digital address of where that specific piece of information is being held inside your computer's RAM while the script runs!

# 🚀 How to Run the Code
Getting this program up and running on your computer is incredibly simple! Just follow these quick steps:

🖥️ Step 1: Open Your Terminal
Start by opening your computer's terminal (or Command Prompt / PowerShell on Windows). Use the cd command to navigate into the specific folder where you have saved this project file.

📥 Step 2: Check Your Python Setup
Make sure you have Python installed on your machine. You can quickly double-check this by typing python --version into your terminal and hitting enter.

🏃‍♂️ Step 3: Launch the Script
Once you are in the correct folder, simply type python main.py (or use the exact name of your script file, like python data_collector.py) and press enter. The application will instantly boot up right inside your terminal, welcoming you to the data collector and guiding you through the prompts step-by-step!
# Code
<img width="1012" height="432" alt="Screenshot 2026-05-25 190453" src="https://github.com/user-attachments/assets/7356b2f8-97ae-43da-855f-e230c13e6dd9" />

<img width="757" h<img width="757" height="291" alt="Screenshot 2026-05-23 132901" src="https://github.com/user-attachments/assets/5a1702eb01f4" />
eight="291" alt="Screenshot 2026-05-23 132901" src="https://github.com/user-attachments/assets/f04343ec-4c4d-4ff5-ba43-87b835da2f77" />
