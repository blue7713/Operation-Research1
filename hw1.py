from ortools.linear_solver import pywraplp


def hw1():
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Create Decision variables
    x11 = solver.NumVar(0, solver.infinity(), 'x11')
    x12 = solver.NumVar(0, solver.infinity(), 'x12')
    x13 = solver.NumVar(0, solver.infinity(), 'x13')
    x21 = solver.NumVar(0, solver.infinity(), 'x21')
    x22 = solver.NumVar(0, solver.infinity(), 'x22')
    x23 = solver.NumVar(0, solver.infinity(), 'x23')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint.
    solver.Add(x11 + x12 + x13 <= 100)
    solver.Add(x21 + x22 + x23 <= 200)
    solver.Add(x11 + x21 <= 150)
    solver.Add(x12 + x22 <= 200)
    solver.Add(x13 + x23 <= 350)

    print('Number of constraints =', solver.NumConstraints())

    # Create Objective function
    solver.Maximize(4*x11 + 4*x12 + 3*x13 + 5*x21 + 5*x22 + 4*x23)

    # Solve the system
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x11 =', x11.solution_value())
        print('x12 =', x12.solution_value())
        print('x13 =', x13.solution_value())
        print('x21 =', x21.solution_value())
        print('x22 =', x22.solution_value())
        print('x23 =', x23.solution_value())
    else:
        print("The problem does not have an optimal solution.")


# 함수 호출
hw1()
