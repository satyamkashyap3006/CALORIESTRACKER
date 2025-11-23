# Health Tracker - Calorie & Water Intake Monitor

## Overview

Health Tracker is a Python-based desktop application that helps users monitor daily calorie and water intake while providing personalized health recommendations. Built with tkinter, it features a modern dark theme with vibrant colors for an engaging user experience. The app calculates BMI, BMR, and TDEE based on user profiles and includes 60+ pre-loaded food items across 8 categories for effortless meal logging.

## Features

- Profile Management: Track age, weight, height, gender, and activity level
- Food Database: 8 categories including Fruits, Vegetables, Proteins, Dairy, Indian Food, and more
- Automatic Calorie Tracking: Select foods and servings for instant calorie calculation
- Water Intake Monitoring: Track hydration with personalized recommendations
- Health Metrics: Automatic BMI, BMR, and TDEE calculations
- Progress Tracking: Real-time visual indicators showing intake vs. recommendations
- Data Persistence: JSON-based local storage for long-term tracking
- Multiple Clear Options: Clear food log, reset progress, or clear all data
- Modern UI: Dark theme with neon green, hot pink, and gold accents

## Technologies Used

- Python 3.6+ (tkinter, json, datetime, os)
- GUI Framework: tkinter with ttk for themed widgets
- Storage: JSON file format

## Installation & Running

1. Ensure Python 3.6+ is installed
2. Verify tkinter: `python -m tkinter`
3. Download `CALORIESTRACKER.py`
4. Run: `python CALORIESTRACKER.py`

The app creates `health_data.json` automatically on first launch.

## Testing

Test key features by:
- Updating profile and verifying BMI/TDEE calculations
- Adding foods (e.g., 2 bananas = 210 calories)
- Logging water intake (e.g., 500ml)
- Testing clear functions (food log, reset progress, clear all)
- Verifying data persistence across sessions
- Checking progress indicators at different intake levels

<img width="1470" height="956" alt="Screenshot 2025-11-23 at 12 56 16 PM" src="https://github.com/user-attachments/assets/7d119d82-14fd-45ce-86ae-dedfe47e5cb8" />
<img width="1470" height="956" alt="Screenshot 2025-11-23 at 12 57 57 PM" src="https://github.com/user-attachments/assets/dbe6e9a0-b2aa-4bb7-8514-4e5ae27750d0" />

