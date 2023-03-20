from ortools.linear_solver import pywraplp

def Exercise3():
    # Create linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    
    # Create Decision variables
    num_vars = 6
    num_consts = 6
    A = [ [1, 0, 0, 0, 0, 1],
          [1, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 1, 1]
          ]
    b = [4, 8, 10, 7, 12, 4]

    x = {}
    for i in range(1, num_vars + 1):
        x[i] = solver.NumVar(0, solver.infinity(), 'x[%i]' %i)

    print('Number of variables =', solver.NumVariables())   
    

    # Create constraint
    for i in range(num_consts):
        constraint = solver.RowConstraint(b[i], solver.infinity(), '') # 4부터 무한대까지의 값
        for j in range(num_vars):
            constraint.SetCoefficient(x[j + 1], A[i][j])

    print('Number of constraints =', solver.NumConstraints()) 

    # Create Objective function
    objective = solver.Objective()

    for i in range(1, num_vars + 1):
        objective.SetCoefficient(x[i], 1)

    objective.SetMinimization()

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
    
    else:
        print("The problem does not have an optimal solution.")                   
        
Exercise3()        