from ortools.linear_solver import pywraplp # LP모형을 풀기위한 라이브러리
from ortools.init import pywrapinit

def main():
# Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP') # LP모형 정의, 'GLOP'라는 solver 사용(LP모형 solver)
    if not solver:
        return

    # Create the variables x and y.
    x = solver.NumVar(0, 1, 'x') # 0~1 사이의 변수 x 
    y = solver.NumVar(0, 2, 'y') # 0~2 사이의 변수 y

    print('Number of variables =', solver.NumVariables()) # 변수의 개수 출력

    # Create a linear constraint, 0 <= x + y <= 2.
    ct = solver.Constraint(0, 2, 'ct') # 기본적인 틀 생성, ct는 0~2사이의 범위, 변수끼리 + 로 연결되어짐
    ct.SetCoefficient(x, 1) # ct에 1x 대입
    ct.SetCoefficient(y, 1) # ct에 1y 대입

    print('Number of constraints =', solver.NumConstraints()) # 제약식의 개수 출력

    # Create the objective function, 3 * x + y.
    objective = solver.Objective() 
    objective.SetCoefficient(x, 3) 
    objective.SetCoefficient(y, 1)
    objective.SetMaximization() # 최대화문제로 세팅

    solver.Solve() # 최적해 찾기

    print('Solution:') # 결과값 출력
    print('Objective value =', objective.Value()) # 목적식 값
    print('x =', x.solution_value()) # 변수의 값
    print('y =', y.solution_value())

if __name__ == '__main__':
    pywrapinit.CppBridge.InitLogging('basic_example.py')
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)
    
    main()