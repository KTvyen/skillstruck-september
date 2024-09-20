


chemisty_relationship_PTVN =  { "P:1/V" : "The inverse of volume is directly proportional to pressure, so as volume lowers < pressure increases.", "P:N" : "Pressure is proportional to partical amount. As pressure increases so does particle amount (n).", "P:T(K)" : "Pressure is directly proportional to temperature in the kelvin scale, as temperature increases form absoulte temperature to beyond pressure also increases." , "V:T(K)" : "Volume and temperature are proportional to one another, as volume increases so does temperature in the kelvin scale." }

chemisty_KMT = {"Tenet 1" : "The amount of particles is negligable, however the amount of space between is not." , "Tenet 2" : "Gas particles do not have force of attraction unlike solids and liquids, so they move freely." , "Tenet 3" : "The movement of gas particles are that of straight lines, they do not move in wiggly lines, they don't change course unless they bump into something (gas particles or wall)" , "Tenet 4" : "When gas particles collide they do not make sounds becuase of their elasity. So typically when particles collide there is a sound because force is exchnaged but gas particles don't do that. When they collide they don't gain or lose energy" , "Tenet 5" : "Gas particles have the average kinetic energy that is proportional to abosolute temperature." }

chemisty_standard_pressure = { "mmHg" : "760." , "kPa" : "101.3", "atm" : "1.00", "psi" : "14.7"}

chemisty_question_straw = input("How do straws work? ")

check_straw = ["push", "pressure", "gas particles", "space", "water"]


if all(word in chemisty_question_straw for word in check_straw):
    print("Great job you mentioned all key concepts")
else:
    print("Failed to mention all key concepts")
