def quadratic_equation(a,b,c): # ax^2 + bx + c = 0
    delta=(b**2)-4*a*c   # use the formula for quadratic equation to calculate root
    root1=(-b+(delta**0.5))/2*a
    root2=(-b-(delta**0.5))/2*a
    return root1,root2
print(quadratic_equation(2,-4,-6))