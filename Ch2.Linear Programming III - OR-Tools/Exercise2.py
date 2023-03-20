from ortools.linear_solver import pywraplp

def Exercise2():
    # Create linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    
    # Create Decision variables
    num_vars = 6
    x = {}
    I = {}
    for i in range(1, num_vars + 1):
        x[i] = solver.NumVar(0, solver.infinity(), 'x[%i]' %i)
        I[i] = solver.NumVar(0, solver.infinity(), 'I[%i]' %i)

    print('Number of variables =', solver.NumVariables())
    

    # Create a linear constraint
    solver.Add(x[1] - I[1] == 100)

    d = [100, 250, 190, 140, 220, 110]
    for i in range(2, 6):
        solver.Add(x[i] - I[i] + I[i - 1] == d[i - 1])

    solver.Add(I[5] + x[6] == 110)

    print('Number of constraints =', solver.NumConstraints())

    # Create Objective function
    objective = solver.Objective()

    x_coeffs = [50, 45, 55, 48, 52, 50]
    I_coeffs = [8, 8, 8, 8, 8, 8] 

    for i in range(1, num_vars + 1):
        objective.SetCoefficient(x[i], x_coeffs[i - 1])   
        objective.SetCoefficient(I[i], I_coeffs[i - 1])  

    objective.SetMinimization()    

    # Solve the system
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:') 
        print('Objective value =', solver.Objective().Value()) 
        print('x1 =', x[1].solution_value()) 
        print('x2 =', x[2].solution_value())
        print('x3 =', x[3].solution_value())
        print('x4 =', x[4].solution_value())
        print('x5 =', x[5].solution_value())
        print('x6 =', x[6].solution_value())
        print('I1 =', I[1].solution_value())
        print('I2 =', I[2].solution_value())
        print('I3 =', I[3].solution_value())
        print('I4 =', I[4].solution_value())
        print('I5 =', I[5].solution_value())
        print('I6 =', I[6].solution_value())
    else:
        print("The problem does not have an optimal solution.")    

Exercise2()    