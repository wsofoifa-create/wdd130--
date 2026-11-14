import math

print("Welcome to the velocity calculator. Please enter the following: ")

#ask user for units
#m
mass = float(input("Mass (in kg): "))

# g
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

#t
time = float(input("(Time (in seconds)"))

#p
density = (float(input("n kg/m^3, 1.3 for air, 1000 for water):")))

#A
sectional = float(input("Cross sectional area (in m^2):"))

#c
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder):"))


drag_constant = (1/2) * density * sectional * drag
print(f"The inner value of c is: {drag_constant:.3f}")

#compute velocity

#v
velocity = math.sqrt(mass * gravity / drag_constant) * (1 - math.exp ((-math.sqrt(mass*gravity*drag_constant) / mass * time)))

print(f"The velocity after 10.0 seconds is: {velocity:.3f} m/s")