Scenario1 = (input("You just got home fom school and suddenly the lights all go out. A loud noise is heard coming from the basement. On your way to investigate " \
"you stumble upon a FLASHLIGHT and a GLOWSTICK. Which one do you take with you? : "))
Scenario1 = Scenario1.upper()

print(Scenario1)

flashlight = "FLASHLIGHT"
glowstick = "GLOWSTICK"
choice1 = ""

if Scenario1 == flashlight:
    choice1 = "The flashlight does not have any batteries, you must head to the garage to get some."

elif Scenario1 == glowstick:
    choice1 = "You shake the glowstick and a very low green light emits making it very hard to see."

else:
    choice1 = "Try again"

print(choice1)