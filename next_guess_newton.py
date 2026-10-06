x = float(input("What x to find the square root of? "))
g = float(input("What guess to start with? "))

print("Current estimate:", g)

# Newton-Raphson formülü: next_guess = guess - f(guess)/f'(guess)
# f(g) = g^2 - x  ve  f'(g) = 2*g
next_guess = g - (g**2 - x) / (2 * g)

print("Next guess:", next_guess)