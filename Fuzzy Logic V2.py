import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Investigative = ctrl.Antecedent(np.arange(0, 11, 1), 'Investigative')
Social = ctrl.Antecedent(np.arange(0, 11, 1), 'Social')
Artistic = ctrl.Antecedent(np.arange(0, 11, 1), 'Artistic')
Realistic = ctrl.Antecedent(np.arange(0, 11, 1), 'Realistic')
Enterprising = ctrl.Antecedent(np.arange(0, 11, 1), 'Enterprising')
Interest = ctrl.Consequent(np.arange(0, 51, 1), 'Interest')

Investigative.automf(3)
Social.automf(3)
Artistic.automf(3)
Realistic.automf(3)
Enterprising.automf(3)

Interest['low'] = fuzz.trimf(Interest.universe, [0, 0, 25])
Interest['medium'] = fuzz.trimf(Interest.universe, [0, 25, 50])
Interest['high'] = fuzz.trimf(Interest.universe, [25, 50, 50])

Investigative.view()
Social.view()
Artistic.view()
Realistic.view()
Enterprising.view()

rule1 = ctrl.Rule(Investigative['poor']    | Social['poor']    | Artistic['poor']    | Realistic['poor']    | Enterprising['poor'],    Interest['low'])
rule2 = ctrl.Rule(Investigative['average'] | Social['average'] | Artistic['average'] | Realistic['average'] | Enterprising['average'], Interest['medium'])
rule3 = ctrl.Rule(Investigative['good']    | Social['good']    | Artistic['good']    | Realistic['good']    | Enterprising['good'],    Interest['high'])
rule4 = ctrl.Rule(Investigative['poor']    | Social['average'] | Artistic['poor']    | Realistic['poor']    | Enterprising['poor'], Interest['low'])
rule5 = ctrl.Rule(Investigative['average'] | Social['good']    | Artistic['poor']    | Realistic['good']    | Enterprising['average'], Interest['medium'])
rule6 = ctrl.Rule(Investigative['good'] | Social['good']    | Artistic['poor']    | Realistic['poor']    | Enterprising['average'], Interest['medium'])
rule7 = ctrl.Rule(Investigative['poor'] | Social['good']    | Artistic['poor']    | Realistic['good']    | Enterprising['good'], Interest['medium'])
rule8 = ctrl.Rule(Investigative['good'] | Social['good']    | Artistic['good']    | Realistic['good']    | Enterprising['average'], Interest['high'])
rule9 = ctrl.Rule(Investigative['average'] | Social['good']    | Artistic['poor']    | Realistic['good']    | Enterprising['average'], Interest['high'])
rule10 = ctrl.Rule(Investigative['average'] | Social['poor']    | Artistic['poor']    | Realistic['good']    | Enterprising['good'], Interest['high']) 

rule1.view()

inter_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10
                                 ])

inter = ctrl.ControlSystemSimulation(inter_ctrl)

print("\n Value 1-3 = Low , 4-7 = Medium , 8-10 = High\n")
print("Enter the value for each skill for suggestion.")

inter.input['Investigative'] = int(input("Enter the value for Investigative : "))
inter.input['Social'] = int(input("Enter the value for Social : "))
inter.input['Artistic'] = int(input("Enter the value for Artistic : "))
inter.input['Realistic'] = int(input("Enter the value for Realistic : "))
inter.input['Enterprising'] = int(input("Enter the value for Enterprising : "))
inter.compute()

print("\nOutput - ")
print(inter.output['Interest'])
Interest.view(sim=inter)