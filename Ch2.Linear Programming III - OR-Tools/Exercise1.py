from ortools.linear_solver import pywraplp

def Exercise1():
    # Create linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    
    # Create Decision variables
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')
    x3 = solver.NumVar(0, solver.infinity(), 'x3')
    x4 = solver.NumVar(0, solver.infinity(), 'x4')
    x5 = solver.NumVar(0, solver.infinity(), 'x5')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint.
    solver.Add(x1 + x2 + x3 + x4 + x5 <= 12)
    solver.Add(x4 + x5 >= 0.4*(x1 + x2 + x3 + x4 + x5))
    solver.Add(x3 >= 0.5*(x1 + x2 + x3))
    solver.Add(0.1*x1 + 0.07*x2 + 0.03*x3 + 0.05*x4 + 0.02*x5 <= 0.4*(x1 + x2 + x3 + x4 + x5))

    print('Number of constraints =', solver.NumConstraints())

    # Create Objective function
    solver.Maximize(0.026*x1 + 0.0509*x2 + 0.0864*x3 + 0.06875*x4 + 0.078*x5)

    # Solve the system
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:') 
        print('Objective value =', solver.Objective().Value()) 
        print('x1 =', x1.solution_value()) 
        print('x2 =', x2.solution_value())
        print('x3 =', x3.solution_value())
        print('x4 =', x4.solution_value())
        print('x5 =', x5.solution_value())
    else:
        print("The problem does not have an optimal solution.")    

# 함수 호출
Exercise1()