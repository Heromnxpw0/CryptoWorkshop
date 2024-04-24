# talk to the server n stuff

pplusq = n - phi + 1
a = 1 
b = pplusq 
c = n

x = symbols('x')
eq = Eq(a*x**2 + b*x + c,0)
sol = solve(eq, x)
p1= -sol[0]
q1 = n // p1
