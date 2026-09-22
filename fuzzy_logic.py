import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def calculate_care_score(soil_moisture, temperature, light):
    # Input variables
    soil = ctrl.Antecedent(np.arange(0, 101, 1), "soil")
    temp = ctrl.Antecedent(np.arange(0, 41, 1), "temperature")
    sunlight = ctrl.Antecedent(np.arange(0, 101, 1), "light")

    # Output variable
    care = ctrl.Consequent(np.arange(0, 101, 1), "care")

    # Membership functions for soil moisture
    soil["dry"] = fuzz.trimf(soil.universe, [0, 0, 40])
    soil["medium"] = fuzz.trimf(soil.universe, [20, 50, 80])
    soil["wet"] = fuzz.trimf(soil.universe, [60, 100, 100])

    # Membership functions for temperature
    temp["low"] = fuzz.trimf(temp.universe, [0, 0, 18])
    temp["moderate"] = fuzz.trimf(temp.universe, [15, 24, 32])
    temp["high"] = fuzz.trimf(temp.universe, [28, 40, 40])

    # Membership functions for sunlight
    sunlight["low"] = fuzz.trimf(sunlight.universe, [0, 0, 40])
    sunlight["medium"] = fuzz.trimf(sunlight.universe, [20, 50, 80])
    sunlight["high"] = fuzz.trimf(sunlight.universe, [60, 100, 100])

    # Membership functions for care level
    care["low"] = fuzz.trimf(care.universe, [0, 0, 40])
    care["medium"] = fuzz.trimf(care.universe, [20, 50, 80])
    care["high"] = fuzz.trimf(care.universe, [60, 100, 100])

    # Fuzzy rules
    rule1 = ctrl.Rule(
        soil["dry"] & temp["high"],
        care["high"]
    )

    rule2 = ctrl.Rule(
        soil["dry"] & sunlight["high"],
        care["high"]
    )

    rule3 = ctrl.Rule(
        soil["medium"] & temp["moderate"],
        care["medium"]
    )

    rule4 = ctrl.Rule(
        soil["wet"] & temp["low"],
        care["low"]
    )

    rule5 = ctrl.Rule(
        soil["wet"] & sunlight["low"],
        care["low"]
    )

    rule6 = ctrl.Rule(
        soil["medium"] & sunlight["medium"],
        care["medium"]
    )

    # Create fuzzy control system
    care_control = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6
    ])

    # Create simulation
    simulation = ctrl.ControlSystemSimulation(care_control)

    # Give inputs to fuzzy system
    simulation.input["soil"] = soil_moisture
    simulation.input["temperature"] = temperature
    simulation.input["light"] = light

    # Perform fuzzy inference and defuzzification
    simulation.compute()

    return round(simulation.output["care"], 2)