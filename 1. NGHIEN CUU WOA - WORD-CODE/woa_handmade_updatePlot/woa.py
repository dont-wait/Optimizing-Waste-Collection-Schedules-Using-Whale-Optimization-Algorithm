import numpy as np
import random as rd
from plot import plot_solutions_init, plot_solutions_update
from initialize import initialize_solutions
from objective_func import get_info

def calculate_fitness(solutions, fitness_func):
    return np.array([fitness_func(solution) for solution in solutions])

def reset_constant(solutions, lb, ub):
    for i in range(len(solutions)):
        for j in range(len(solutions[i])):
            if solutions[i][j] < ub: solutions[i][j] = ub
            if solutions[i][j] > lb: solutions[i][j] = lb
            
def get_best_solution(solutions, fitness):
    best_index = np.argmin(fitness)
    return solutions[best_index], fitness[best_index]

def calculate_A(a, dim):
    rand = np.random.uniform(0, 1, dim)
    return 2*np.multiply(rand, a) - a

def calculate_C(dim):
    rand = np.random.uniform(0, 1, dim)
    return 2*rand

def Encircling(best_sol, sol, A, dim):
    C = calculate_C(dim)
    D = np.abs(np.multiply(C, best_sol) - sol)
    return best_sol - np.multiply(A, D)

def rand_solution(solutions, population_size):
    return solutions[rd.randint(0, population_size - 1)]

def Searching(rand_sol, sol, A, dim):
    C = calculate_C(dim)
    D = np.abs(np.multiply(C, rand_sol) - sol)
    return rand_sol - np.multiply(A, D)

def Attacking(best_sol, sol, a2):
    b = np.random.uniform(-1, 1)
    l = (a2 - 1)*np.random.uniform(0, 1) + 1
    D = np.linalg.norm(best_sol - sol)
    return D*np.exp(b*l)*np.cos(2*np.pi*l) + best_sol

# handle
def woa_handle(function_name, population_size, max_iterater):
    # lay cac fitness, ub, lb, dim
    fitness_func, ub, lb, dim = get_info(function_name)
    # khoi tao quan the ban dau
    solutions = initialize_solutions(population_size, dim, lb, ub)
    # quan the ban dau
    print(f"""Quan the ban dau: 
          {solutions}""")
    
    #Biểu đồ quần thể ban đầu
    plot_solutions_init(solutions, calculate_fitness(solutions, fitness_func))
    
    iter = 0
    fitness = np.inf
    while iter < max_iterater:
        # tinh fitness cho tung ca the
        fitness_list = calculate_fitness(solutions, fitness_func)
        best_sol_t, fitness_sol_t = get_best_solution(solutions, fitness_list)

        # neu co gia tri tot hon thi cap nhat lai
        if fitness_sol_t < fitness:
            fitness = fitness_sol_t
            best_sol = best_sol_t
        # cap nhat gia tri cho moi ca the
        a1 = 2*(1 - iter / max_iterater)
        a2 = 1/2 * a1 - 2
        for i in range(len(solutions)):
            p = np.random.uniform(0, 1)
            if p < 0.5:
                A = calculate_A(a1, dim)
                if np.linalg.norm(A) < 1:
                    solutions[i] = Encircling(best_sol, solutions[i], A, dim)
                else:
                    rand_sol = rand_solution(solutions, population_size)
                    solutions[i] = Searching(rand_sol, solutions[i], A, dim)
            else:
                solutions[i] = Attacking(best_sol, solutions[i], a2)
        # neu co ca the vuot khoi khong gian tim kiem thi dat lai gia tri
        reset_constant(solutions, lb, ub)
        plot_solutions_update(solutions, best_sol_t, iter)
        iter += 1
        print(fitness)
    return best_sol, fitness
    