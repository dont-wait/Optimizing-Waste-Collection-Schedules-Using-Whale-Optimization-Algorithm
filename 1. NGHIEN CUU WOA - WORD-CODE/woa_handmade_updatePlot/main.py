from initialize import initialize_solutions
from woa import woa_handle

def main():
    pop_size = 50
    function_name = 'F2'
    max_iterater = 100
    best_sol, fitness_sol = woa_handle(function_name, pop_size, max_iterater)
    print("Giải pháp tốt nhất:", best_sol, fitness_sol)
    # plot_solutions(solutions, best_solution)

main()