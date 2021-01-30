# A function that gets trinomial factors as input and returns discriminant value

def discriminant(a,b,c):

    discriminant = int(b) ** 2 - 4 * int(a) * int(c)

    return discriminant

# A function that checks for valid numeric inputs

def check_for_numeric_values(x):

    if x.isnumeric() == True:

        return True

    else:

        return False

# A function that rounds root to 2 decimal digits

def round_value(x):

    if isinstance(x, complex) == True:

        return round(x.real, 2) + round(x.imag, 2) * 1j

    else :

        return round(float(x), 2)

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

equation_disc = discriminant(a,b,c)

x1 = round_value( ( - int(b) + equation_disc ** 0.5 ) / ( 2 * int(a) ) )

x2 = round_value( ( - int(b) - equation_disc ** 0.5 ) / ( 2 * int(a) ) )

if ( x1 == x2 ) :

    if isinstance(x1, complex) == True:

        print ("Double Imaginary Root", x1)

    else :

        print ("Double Real Root", x1)

else :

    if isinstance(x1, complex) == True:

        print ("Imaginary Root x1 =", x1)

    else :

        print ("Real Root x1 =", x1)

    if isinstance(x2, complex) == True:

        print ("Imaginary Root x2 =", x2)

    else :

        print ("Real Root x2 =", x2)
