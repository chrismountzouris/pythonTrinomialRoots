import matplotlib.pyplot as plt

import numpy as np

# A function that checks for valid numeric inputs

def check_for_numeric_values(x):

    if x.isnumeric() == True:

        return True

    else:

        return False

while True:

  a = input ("Insert the equation's factor 'a' value: ")

  if check_for_numeric_values (a) == True:

    break

  else:

    print ("Unacceptable value. Please try again.")

while True:

  b = input ("Insert the equation's factor 'b' value: ")

  if check_for_numeric_values (b) == True:

    break

  else:

    print ("Unacceptable value. Please try again.")

while True:

  c = input ("Insert the equation's factor 'c' value: ")

  if check_for_numeric_values (c) == True:

    break

  else:

    print ("Unacceptable value. Please try again.")

# Returns evenly spaced numbers over a specified interval [start,stop,num]

x = np.linspace(-2, 2, 100)

# Create the second order equation / trinomial

y = float(a) * (x ** 2) + float(b) * x + float(c)

# Width, height of the plot in inches

plt.figure(figsize = (10, 5))

# Create the plot

plt.plot(x, y)

# Show the plot

plt.show()
