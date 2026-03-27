PROJECT REPORT: Health Tracker – Calorie & Water Intake Monitor 

Course: B.Tech CSE (AI/ML) 

Developer: Satyam Kashyap 

Institution: VIT Bhopal University 

 

1. Introduction 

The Health Tracker is a Python-based desktop application designed to bridge the gap between nutritional awareness and daily habits. In an era where lifestyle diseases are prevalent, this tool provides a centralized, offline platform for users to monitor their caloric intake, hydration levels, and essential body metrics like BMI and TDEE. 

2. Problem Statement 

Many existing health apps require constant internet connectivity or paid subscriptions. There is a need for a lightweight, privacy-focused desktop tool that allows students and professionals to track their health metrics locally without complex setups. 

3. Proposed Solution 

A GUI-based application developed using Python’s tkinter library. It features: 

Dynamic Calculations: Real-time updates for BMI (Body Mass Index) and BMR (Basal Metabolic Rate). 

Localized Storage: Using JSON for data persistence so no data leaves the user's machine. 

User-Centric Design: A modern dark-themed UI to reduce eye strain during evening logging. 

4. System Requirements 

4.1 Hardware Requirements 

Processor: 1.6 GHz or faster 

RAM: 4 GB minimum 

Storage: 50 MB (includes Python environment) 

4.2 Software Requirements 

Operating System: Windows/macOS/Linux 

Language: Python 3.6+ 

Libraries: tkinter (GUI), json (Data), datetime (Time tracking) 

5. System Design & Architecture 

The project follows a modular structure: 

UI Layer: Built with tkinter and ttk for a responsive, modern aesthetic (Neon/Gold accents). 

Logic Layer: Python functions to handle the mathematical formulas for TDEE and BMR based on the Mifflin-St Jeor Equation. 

Data Layer: A health_data.json file that stores user profiles and daily logs. 

6. Implementation Details 

6.1 Key Algorithms 

BMI Formula: Weight(kg) / Height(m)^2 

TDEE Calculation: Calculated by multiplying BMR by an activity factor (1.2 to 1.9). 

Food Database: A dictionary-based structure containing over 60 items across 8 categories (Fruits, Vegetables, Proteins, etc.). 

7. Results and Discussion 

The application successfully allows a user to: 

Set up a profile with age, height, and weight. 

Log a meal (e.g., "2 Bananas") and see an immediate update of +210 calories. 

Track water intake in milliliters. 

View a real-time progress bar of "Actual vs. Target" calories. 

8. Conclusion & Future Scope 

The Health Tracker demonstrates the effective use of Python for building utility-based software. Future Enhancements: 

Integration with a Web API (like Edamam) for a larger food database. 

Adding a graphical "Weight Trend" chart using Matplotlib. 

Developing a mobile-responsive version using Kivy. 

 
