import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define inputs and outputs
road_condition = ctrl.Antecedent(np.arange(0, 11, 1), 'road_condition')
weather_condition = ctrl.Antecedent(np.arange(0, 11, 1), 'weather_condition')
car_speed = ctrl.Consequent(np.arange(0, 101, 1), 'car_speed')

# Define membership functions
road_condition['poor'] = fuzz.trimf(road_condition.universe, [0, 0, 5])
road_condition['good'] = fuzz.trimf(road_condition.universe, [0, 5, 10])

weather_condition['bad'] = fuzz.trimf(weather_condition.universe, [0, 0, 5])
weather_condition['fair'] = fuzz.trimf(weather_condition.universe, [0, 5, 10])
weather_condition['good'] = fuzz.trimf(weather_condition.universe, [5, 10, 10])

car_speed['slow'] = fuzz.trimf(car_speed.universe, [0, 0, 50])
car_speed['fast'] = fuzz.trimf(car_speed.universe, [0, 50, 100])

# Define rules
rule1 = ctrl.Rule(road_condition['poor'] & weather_condition['bad'], car_speed['slow'])
rule2 = ctrl.Rule(road_condition['poor'] & weather_condition['fair'], car_speed['slow'])
rule3 = ctrl.Rule(road_condition['poor'] & weather_condition['good'], car_speed['slow'])
rule4 = ctrl.Rule(road_condition['good'] & weather_condition['bad'], car_speed['slow'])
rule5 = ctrl.Rule(road_condition['good'] & weather_condition['fair'], car_speed['fast'])
rule6 = ctrl.Rule(road_condition['good'] & weather_condition['good'], car_speed['fast'])

# Create control system
car_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])

# Create simulation
car_sim = ctrl.ControlSystemSimulation(car_ctrl)

# Get input values from user
rc = int(input("Enter road condition (0-10): "))
wc = int(input("Enter weather condition (0-10): "))

# Set input values
car_sim.input['road_condition'] = rc
car_sim.input['weather_condition'] = wc

# Compute output
car_sim.compute()

# Print output
print("Recommended car speed: {:.2f}".format(car_sim.output['car_speed']))
