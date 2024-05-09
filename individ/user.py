from calories import BMR_Calculator, BMI_Calculator

class User():
    height = 183
    weight = 108
    sex = 'male'
    age = 40
    activity = 'sedentary'
    meals_a_day = 5
    BMI = 32.2
    category = 'obese'
    BMR = 2417
    cal_needed = 2901
    calories_left = 2901
    meals_left = 5
    PIN = '1234'
    
#     def __init__(self, bmi: BMI_Calculator, bmr: BMR_Calculator,
#                  height, weight, sex, age, activity, meals):
#         self.bmi = bmi
#         self.bmr = bmr
#         self.height = height
#         self.weight = weight
#         self.sex = sex
#         self.age = age
#         self.activity = activity
#         self.meals_a_day = meals
#         self.BMI = self.bmi.getBMI(self.height, self.weight)
#         self.category = self.bmi.getBMI_category(self.bmi)
#         self.BMR = self.bmr.getBMR(self.height, self.weight, self.age, self.sex)
#         self.cal_needed = self.bmr.calories_needed(self.BMR, self.activity)
        
    def new_day(self):
        self.meals_left = self.meals_a_day
        self.calories_left = self.cal_needed
        
    def meal_eaten(self, calories):
        self.calories_left -= calories
        self.meals_left -= 1
        
    def average_meal(self):
        return self.calories_left / self.meals_left
        
    
    
    
    