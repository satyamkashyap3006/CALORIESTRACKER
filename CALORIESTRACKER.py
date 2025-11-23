import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class HealthTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker - Calorie & Water Intake")
        self.root.geometry("850x800")
        self.root.configure(bg='#1a1a2e')
        
        # Data storage
        self.data_file = "health_data.json"
        self.load_data()
        
        # Food database with calories per 100g or per serving
        self.food_database = {
            "Fruits": {
                "Apple (1 medium)": 95,
                "Banana (1 medium)": 105,
                "Orange (1 medium)": 62,
                "Grapes (1 cup)": 104,
                "Mango (1 cup)": 99,
                "Watermelon (1 cup)": 46,
                "Strawberries (1 cup)": 49,
                "Pineapple (1 cup)": 82,
            },
            "Vegetables": {
                "Broccoli (1 cup)": 55,
                "Carrot (1 medium)": 25,
                "Tomato (1 medium)": 22,
                "Potato (1 medium)": 164,
                "Spinach (1 cup)": 7,
                "Cucumber (1 cup)": 16,
                "Bell Pepper (1 medium)": 37,
                "Onion (1 medium)": 44,
            },
            "Grains & Bread": {
                "White Rice (1 cup cooked)": 206,
                "Brown Rice (1 cup cooked)": 216,
                "Whole Wheat Bread (1 slice)": 81,
                "White Bread (1 slice)": 79,
                "Pasta (1 cup cooked)": 221,
                "Oatmeal (1 cup cooked)": 154,
                "Quinoa (1 cup cooked)": 222,
                "Roti/Chapati (1 medium)": 71,
            },
            "Proteins": {
                "Chicken Breast (100g)": 165,
                "Salmon (100g)": 208,
                "Tuna (100g)": 144,
                "Egg (1 large)": 72,
                "Tofu (100g)": 76,
                "Lentils (1 cup cooked)": 230,
                "Chickpeas (1 cup cooked)": 269,
                "Greek Yogurt (1 cup)": 100,
            },
            "Dairy": {
                "Milk (1 cup)": 149,
                "Cheese (1 slice)": 113,
                "Butter (1 tbsp)": 102,
                "Paneer (100g)": 265,
                "Curd/Yogurt (1 cup)": 154,
                "Ice Cream (1 cup)": 267,
            },
            "Snacks": {
                "Chips (1 oz)": 152,
                "Cookies (2 medium)": 140,
                "Chocolate Bar (1 bar)": 235,
                "Popcorn (1 cup)": 31,
                "Nuts (1 oz)": 161,
                "Pizza (1 slice)": 285,
                "Burger (1 medium)": 354,
                "Fries (medium)": 365,
            },
            "Beverages": {
                "Coffee (1 cup black)": 2,
                "Tea (1 cup)": 2,
                "Soda (12 oz)": 140,
                "Orange Juice (1 cup)": 112,
                "Beer (12 oz)": 153,
                "Wine (5 oz)": 123,
                "Energy Drink (8 oz)": 110,
                "Smoothie (1 cup)": 145,
            },
            "Indian Food": {
                "Dal (1 cup)": 198,
                "Biryani (1 cup)": 290,
                "Samosa (1 piece)": 262,
                "Dosa (1 medium)": 168,
                "Idli (1 piece)": 39,
                "Paratha (1 medium)": 126,
                "Curry (1 cup)": 180,
                "Raita (1 cup)": 80,
            }
        }
        
        # User profile
        self.age = tk.IntVar(value=25)
        self.weight = tk.DoubleVar(value=70.0)
        self.height = tk.DoubleVar(value=170.0)
        self.gender = tk.StringVar(value="male")
        self.activity_level = tk.StringVar(value="moderate")
        
        self.create_widgets()
        self.update_recommendations()
        
    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                'daily_logs': {},
                'profile': {}
            }
    
    def save_data(self):
        """Save data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def create_widgets(self):
        # Title with gradient-like effect
        title_frame = tk.Frame(self.root, bg='#16213e', height=80)
        title_frame.pack(fill='x', pady=0)
        
        title_label = tk.Label(title_frame, text="🏃 HEALTH TRACKER", 
                               font=('Arial', 32, 'bold'), bg='#16213e', fg='#00ff88')
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(title_frame, text="Track Your Wellness Journey", 
                                 font=('Arial', 13), bg='#16213e', fg='#ffd700')
        subtitle_label.pack(pady=(0, 10))
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=15)
        
        # Left frame - Profile & Input
        left_frame = tk.LabelFrame(main_frame, text="👤 Profile & Daily Input", 
                                   font=('Arial', 14, 'bold'), bg='#0f3460', fg='#00ff88',
                                   padx=15, pady=15, relief='raised', bd=3)
        left_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        
        # Profile section
        tk.Label(left_frame, text="Age:", bg='#0f3460', fg='#ff6b9d', 
                font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        age_spin = tk.Spinbox(left_frame, from_=10, to=100, textvariable=self.age, 
                             width=15, bg='#16213e', fg='#00ff88', insertbackground='#00ff88',
                             buttonbackground='#16213e', relief='flat', font=('Arial', 11))
        age_spin.grid(row=0, column=1, pady=5)
        
        tk.Label(left_frame, text="Weight (kg):", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        weight_spin = tk.Spinbox(left_frame, from_=30, to=200, textvariable=self.weight, 
                                width=15, increment=0.5, bg='#16213e', fg='#00ff88',
                                insertbackground='#00ff88', buttonbackground='#16213e', 
                                relief='flat', font=('Arial', 11))
        weight_spin.grid(row=1, column=1, pady=5)
        
        tk.Label(left_frame, text="Height (cm):", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        height_spin = tk.Spinbox(left_frame, from_=100, to=250, textvariable=self.height, 
                                width=15, bg='#16213e', fg='#00ff88', insertbackground='#00ff88',
                                buttonbackground='#16213e', relief='flat', font=('Arial', 11))
        height_spin.grid(row=2, column=1, pady=5)
        
        tk.Label(left_frame, text="Gender:", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky='w', pady=5)
        gender_frame = tk.Frame(left_frame, bg='#0f3460')
        gender_frame.grid(row=3, column=1, pady=5, sticky='w')
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender, value="male", 
                      bg='#0f3460', fg='#ffd700', selectcolor='#16213e',
                      activebackground='#0f3460', activeforeground='#00ff88',
                      font=('Arial', 11)).pack(side='left')
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender, value="female", 
                      bg='#0f3460', fg='#ffd700', selectcolor='#16213e',
                      activebackground='#0f3460', activeforeground='#00ff88',
                      font=('Arial', 11)).pack(side='left')
        
        tk.Label(left_frame, text="Activity Level:", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=4, column=0, sticky='w', pady=5)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox', 
                       fieldbackground='#16213e',
                       background='#16213e',
                       foreground='#00ff88',
                       arrowcolor='#00ff88',
                       bordercolor='#00ff88')
        
        activity_combo = ttk.Combobox(left_frame, textvariable=self.activity_level, 
                                     width=13, state='readonly', style='Custom.TCombobox',
                                     font=('Arial', 11))
        activity_combo['values'] = ('sedentary', 'light', 'moderate', 'active', 'very active')
        activity_combo.grid(row=4, column=1, pady=5)
        
        tk.Button(left_frame, text="⚡ Update Profile", command=self.update_recommendations, 
                  bg='#00ff88', fg='#0f3460', font=('Arial', 13, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#00cc70', activeforeground='#0f3460').grid(row=5, column=0, columnspan=2, pady=15, ipadx=10)
        
        # Separator
        sep_frame = tk.Frame(left_frame, bg='#ff6b9d', height=3)
        sep_frame.grid(row=6, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Daily intake section - Food Selection
        intake_label = tk.Label(left_frame, text="🍽️ Add Food Items", bg='#0f3460', 
                               fg='#00ff88', font=('Arial', 14, 'bold'))
        intake_label.grid(row=7, column=0, columnspan=2, pady=10)
        
        tk.Label(left_frame, text="Category:", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=8, column=0, sticky='w', pady=5)
        
        self.food_category = tk.StringVar(value="Fruits")
        category_combo = ttk.Combobox(left_frame, textvariable=self.food_category, 
                                     width=13, state='readonly', style='Custom.TCombobox',
                                     font=('Arial', 11))
        category_combo['values'] = list(self.food_database.keys())
        category_combo.grid(row=8, column=1, pady=5)
        category_combo.bind('<<ComboboxSelected>>', self.update_food_items)
        
        tk.Label(left_frame, text="Food Item:", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=9, column=0, sticky='w', pady=5)
        
        self.food_item = tk.StringVar()
        self.food_combo = ttk.Combobox(left_frame, textvariable=self.food_item, 
                                      width=13, state='readonly', style='Custom.TCombobox',
                                      font=('Arial', 11))
        self.food_combo.grid(row=9, column=1, pady=5)
        self.update_food_items()
        
        tk.Label(left_frame, text="Servings:", bg='#0f3460', fg='#ff6b9d',
                font=('Arial', 12, 'bold')).grid(row=10, column=0, sticky='w', pady=5)
        self.servings = tk.DoubleVar(value=1.0)
        servings_spin = tk.Spinbox(left_frame, from_=0.5, to=10, textvariable=self.servings, 
                                  width=15, increment=0.5, bg='#16213e', fg='#00ff88',
                                  insertbackground='#00ff88', buttonbackground='#16213e', 
                                  relief='flat', font=('Arial', 11))
        servings_spin.grid(row=10, column=1, pady=5)
        
        tk.Button(left_frame, text="➕ Add Food", command=self.add_food_item, 
                  bg='#ffd700', fg='#0f3460', font=('Arial', 13, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#ffb700', activeforeground='#0f3460').grid(row=11, column=0, columnspan=2, pady=10, ipadx=10)
        
        # Separator
        sep_frame2 = tk.Frame(left_frame, bg='#e94560', height=2)
        sep_frame2.grid(row=12, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Water entry section
        water_label = tk.Label(left_frame, text="💧 Add Water Intake", bg='#0f3460', 
                               fg='#00d4ff', font=('Arial', 13, 'bold'))
        water_label.grid(row=13, column=0, columnspan=2, pady=10)
        
        tk.Label(left_frame, text="Water (ml):", bg='#0f3460', fg='#e94560',
                font=('Arial', 11, 'bold')).grid(row=14, column=0, sticky='w', pady=5)
        self.water_entry = tk.Entry(left_frame, width=15, bg='#16213e', fg='#00d4ff',
                                    insertbackground='#00d4ff', relief='flat', bd=2,
                                    font=('Arial', 11))
        self.water_entry.grid(row=14, column=1, pady=5)
        
        tk.Button(left_frame, text="💦 Add Water", command=self.add_water, 
                  bg='#00bcd4', fg='#0f3460', font=('Arial', 12, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#0097a7', activeforeground='#0f3460').grid(row=15, column=0, columnspan=2, pady=10, ipadx=10)
        
        # Clear button
        tk.Button(left_frame, text="🗑️ Clear Today's Log", command=self.clear_today, 
                  bg='#f44336', fg='white', font=('Arial', 12, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#d32f2f', activeforeground='white').grid(row=16, column=0, columnspan=2, pady=15, ipadx=10)
        
        # Right frame - Recommendations & Progress
        right_frame = tk.LabelFrame(main_frame, text="💡 Recommendations & Progress", 
                                    font=('Arial', 14, 'bold'), bg='#0f3460', fg='#00ff88',
                                    padx=15, pady=15, relief='raised', bd=3)
        right_frame.grid(row=0, column=1, sticky='nsew')
        
        # Recommendations
        self.rec_text = tk.Text(right_frame, height=15, width=45, wrap='word', 
                                font=('Arial', 11), bg='#16213e', fg='#ffd700', 
                                relief='flat', insertbackground='#00ff88', bd=0)
        self.rec_text.pack(pady=10, padx=5)
        
        # Today's progress
        progress_frame = tk.LabelFrame(right_frame, text="📊 Today's Progress", 
                                       font=('Arial', 13, 'bold'), bg='#0f3460', fg='#ff6b9d',
                                       padx=10, pady=10, relief='raised', bd=2)
        progress_frame.pack(fill='x', pady=10)
        
        self.progress_label = tk.Label(progress_frame, text="", bg='#0f3460', fg='#ffd700',
                                       font=('Arial', 11), justify='left')
        self.progress_label.pack()
        
        # Food log display
        food_log_frame = tk.LabelFrame(right_frame, text="🍴 Today's Food Log", 
                                       font=('Arial', 13, 'bold'), bg='#0f3460', fg='#ff6b9d',
                                       padx=10, pady=10, relief='raised', bd=2)
        food_log_frame.pack(fill='both', expand=True, pady=10)
        
        # Scrollable food log
        food_scroll_frame = tk.Frame(food_log_frame, bg='#0f3460')
        food_scroll_frame.pack(fill='both', expand=True)
        
        food_scrollbar = tk.Scrollbar(food_scroll_frame, bg='#16213e')
        food_scrollbar.pack(side='right', fill='y')
        
        self.food_log_text = tk.Text(food_scroll_frame, height=6, wrap='word', 
                                     font=('Arial', 10), bg='#16213e', fg='#ffd700',
                                     relief='flat', yscrollcommand=food_scrollbar.set)
        self.food_log_text.pack(side='left', fill='both', expand=True)
        food_scrollbar.config(command=self.food_log_text.yview)
        
        # Control buttons frame
        control_frame = tk.Frame(right_frame, bg='#0f3460')
        control_frame.pack(fill='x', pady=10)
        
        tk.Button(control_frame, text="🗑️ Clear Food Log", command=self.clear_food_log, 
                  bg='#ff5722', fg='white', font=('Arial', 11, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#e64a19', activeforeground='white').pack(side='left', padx=5, ipadx=10)
        
        tk.Button(control_frame, text="🔄 Reset Progress", command=self.reset_progress, 
                  bg='#9c27b0', fg='white', font=('Arial', 11, 'bold'), 
                  cursor='hand2', relief='raised', bd=3,
                  activebackground='#7b1fa2', activeforeground='white').pack(side='left', padx=5, ipadx=10)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        self.update_progress_display()
    
    def update_food_items(self, event=None):
        """Update food items based on selected category"""
        category = self.food_category.get()
        food_items = list(self.food_database[category].keys())
        self.food_combo['values'] = food_items
        if food_items:
            self.food_combo.current(0)
    
    def add_food_item(self):
        """Add food item to daily intake"""
        try:
            category = self.food_category.get()
            food = self.food_item.get()
            servings = self.servings.get()
            
            if not food:
                messagebox.showerror("Error", "Please select a food item!")
                return
            
            calories = self.food_database[category][food] * servings
            
            today = datetime.now().strftime("%Y-%m-%d")
            
            if today not in self.data['daily_logs']:
                self.data['daily_logs'][today] = {'calories': 0, 'water': 0, 'foods': []}
            
            self.data['daily_logs'][today]['calories'] += calories
            
            # Track food items
            if 'foods' not in self.data['daily_logs'][today]:
                self.data['daily_logs'][today]['foods'] = []
            
            self.data['daily_logs'][today]['foods'].append({
                'name': food,
                'servings': servings,
                'calories': calories
            })
            
            self.save_data()
            self.update_progress_display()
            
            messagebox.showinfo("Success", f"Added: {food}\n{servings} serving(s) = {calories:.0f} calories!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add food item: {str(e)}")
    
    def add_water(self):
        """Add water intake only"""
        try:
            water = float(self.water_entry.get())
            
            today = datetime.now().strftime("%Y-%m-%d")
            
            if today not in self.data['daily_logs']:
                self.data['daily_logs'][today] = {'calories': 0, 'water': 0, 'foods': []}
            
            self.data['daily_logs'][today]['water'] += water
            
            self.save_data()
            self.update_progress_display()
            
            self.water_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Added {water}ml water!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for water!")
    
    def clear_today(self):
        """Clear today's log"""
        result = messagebox.askyesno("Clear All Data", 
                                     "Are you sure you want to clear ALL of today's data?\n(Food + Water + Progress)\n\nThis cannot be undone!")
        if result:
            today = datetime.now().strftime("%Y-%m-%d")
            if today in self.data['daily_logs']:
                del self.data['daily_logs'][today]
                self.save_data()
                self.update_progress_display()
                messagebox.showinfo("Success", "Today's complete log has been cleared!")
    
    def clear_food_log(self):
        """Clear only food log, keep water"""
        result = messagebox.askyesno("Clear Food Log", 
                                     "Are you sure you want to clear today's food log?\n(Water intake will be kept)\n\nThis cannot be undone!")
        if result:
            today = datetime.now().strftime("%Y-%m-%d")
            if today in self.data['daily_logs']:
                self.data['daily_logs'][today]['foods'] = []
                self.data['daily_logs'][today]['calories'] = 0
                self.save_data()
                self.update_progress_display()
                messagebox.showinfo("Success", "Food log cleared! Water intake preserved.")
    
    def reset_progress(self):
        """Reset calories and water but keep food log for reference"""
        result = messagebox.askyesno("Reset Progress", 
                                     "Reset today's calorie and water counts to zero?\n(Food log will be kept for reference)\n\nThis cannot be undone!")
        if result:
            today = datetime.now().strftime("%Y-%m-%d")
            if today in self.data['daily_logs']:
                self.data['daily_logs'][today]['calories'] = 0
                self.data['daily_logs'][today]['water'] = 0
                self.save_data()
                self.update_progress_display()
                messagebox.showinfo("Success", "Progress reset! Check food log to re-add items if needed.")
    
    def calculate_bmr(self):
        """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
        weight = self.weight.get()
        height = self.height.get()
        age = self.age.get()
        
        if self.gender.get() == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        return bmr
    
    def calculate_tdee(self, bmr):
        """Calculate Total Daily Energy Expenditure"""
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very active': 1.9
        }
        
        multiplier = activity_multipliers.get(self.activity_level.get(), 1.55)
        return bmr * multiplier
    
    def calculate_water_intake(self):
        """Calculate recommended water intake in ml"""
        weight = self.weight.get()
        # Basic formula: 30-35ml per kg of body weight
        return weight * 35
    
    def update_recommendations(self):
        """Update recommendations based on profile"""
        bmr = self.calculate_bmr()
        tdee = self.calculate_tdee(bmr)
        water = self.calculate_water_intake()
        
        # Calculate BMI
        height_m = self.height.get() / 100
        bmi = self.weight.get() / (height_m ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            bmi_category = "Underweight"
            bmi_advice = "Consider increasing calorie intake with nutrient-dense foods."
        elif 18.5 <= bmi < 25:
            bmi_category = "Normal weight"
            bmi_advice = "Maintain your current healthy habits!"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
            bmi_advice = "Consider reducing calorie intake by 300-500 calories/day for gradual weight loss."
        else:
            bmi_category = "Obese"
            bmi_advice = "Consult a healthcare professional for a personalized plan."
        
        # Generate recommendations
        recommendations = f"""
📊 YOUR HEALTH METRICS

BMI: {bmi:.1f} ({bmi_category})
BMR: {bmr:.0f} calories/day
TDEE: {tdee:.0f} calories/day

💧 WATER INTAKE
Recommended: {water:.0f} ml/day ({water/250:.0f} glasses)

🍽️ CALORIE RECOMMENDATIONS
• Maintenance: {tdee:.0f} cal/day
• Weight Loss: {tdee - 500:.0f} cal/day
• Weight Gain: {tdee + 300:.0f} cal/day

✨ PERSONALIZED ADVICE
{bmi_advice}

🥗 NUTRITION TIPS
• Eat 5-6 small meals throughout the day
• Include protein in every meal
• Eat fruits & vegetables (5+ servings/day)
• Choose whole grains over refined grains
• Limit processed foods and added sugars
• Stay hydrated throughout the day

🏃 ACTIVITY TIPS
• Aim for 150 min of moderate exercise/week
• Include strength training 2-3 times/week
• Take regular breaks if sedentary
• Walk 10,000 steps daily if possible
"""
        
        self.rec_text.delete(1.0, tk.END)
        self.rec_text.insert(1.0, recommendations)
        
    def add_intake(self):
        """Add today's intake - DEPRECATED, kept for compatibility"""
        try:
            if self.water_entry.get():
                self.add_water()
        except:
            pass
    
    def update_progress_display(self):
        """Update today's progress display"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        if today in self.data['daily_logs']:
            calories = self.data['daily_logs'][today]['calories']
            water = self.data['daily_logs'][today]['water']
            foods = self.data['daily_logs'][today].get('foods', [])
        else:
            calories = 0
            water = 0
            foods = []
        
        tdee = self.calculate_tdee(self.calculate_bmr())
        recommended_water = self.calculate_water_intake()
        
        calorie_percent = (calories / tdee) * 100
        water_percent = (water / recommended_water) * 100
        
        progress_text = f"""
🔥 Calories: {calories:.0f} / {tdee:.0f} ({calorie_percent:.0f}%)
💧 Water: {water:.0f}ml / {recommended_water:.0f}ml ({water_percent:.0f}%)

Status:
"""
        
        if calorie_percent < 80:
            progress_text += "⚠️ You may need more calories today\n"
        elif calorie_percent > 120:
            progress_text += "⚠️ You're exceeding your calorie goal\n"
        else:
            progress_text += "✅ You're on track with calories!\n"
        
        if water_percent < 50:
            progress_text += "⚠️ Drink more water!"
        elif water_percent < 100:
            progress_text += "👍 Keep drinking water!"
        else:
            progress_text += "✅ Great hydration!"
        
        self.progress_label.config(text=progress_text)
        
        # Update food log
        self.food_log_text.delete(1.0, tk.END)
        if foods:
            for i, food in enumerate(foods, 1):
                log_entry = f"{i}. {food['name']}\n   {food['servings']} serving(s) - {food['calories']:.0f} cal\n\n"
                self.food_log_text.insert(tk.END, log_entry)
        else:
            self.food_log_text.insert(tk.END, "No food items logged yet today.\nStart adding foods to track your intake!")

def main():
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()