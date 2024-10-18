from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def plot_solutions_init(solutions, best_solution):
    dim = solutions.shape[1] # lấy ra số cột
    
    if dim == 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(solutions[:, 0], solutions[:, 1], c='Blue', label='Quần thể ban đầu')
        plt.scatter(best_solution[0], best_solution[1], c='Red', label='Giải pháp tốt nhất', s=100)
        plt.title('Khởi tạo quần thể ban đầu (2D)', fontweight="bold")
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.show()
        
    elif dim == 3:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(solutions[:, 0], solutions[:, 1], solutions[:, 2], c='Blue', label='Quần thể ban đầu')
        ax.scatter(best_solution[0], best_solution[1], best_solution[2], c='Red', label='Giải pháp tốt nhất', s=100)
        ax.set_title('Khởi tạo quần thể ban đầu (3D)', fontweight="bold")
        ax.set_xlabel('X1')
        ax.set_ylabel('X2')
        ax.set_zlabel('X3')
        ax.legend()
        plt.show()
        
    else:
        # Giảm chiều xuống 2D bằng PCA
        pca = PCA(n_components=2)
        reduced_solutions = pca.fit_transform(solutions)
        reduced_best_solution = pca.transform(best_solution.reshape(1, -1))

        plt.figure(figsize=(8, 6))
        plt.scatter(reduced_solutions[:, 0], reduced_solutions[:, 1], c='Blue', label='Quần thể ban đầu (PCA)')
        plt.scatter(reduced_best_solution[0, 0], reduced_best_solution[0, 1], c='Red', label='Giải pháp tốt nhất', s=100)
        plt.title('Khởi tạo quần thể ban đầu (Giảm chiều)', fontweight="bold")
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.show()
    

def plot_solutions_update(solutions, best_solution, i):
    dim = solutions.shape[1] # lấy ra số cột
    
    if dim == 2:
        plt.figure(figsize=(8, 6))
        plt.scatter(solutions[:, 0], solutions[:, 1], c='Blue', label=f'Quần thể vòng lặp thứ {i}')
        plt.scatter(best_solution[0], best_solution[1], c='Red', label='Giải pháp tốt nhất', s=100)
        plt.title(f'Quần thể vòng lặp thứ {i} (2D)', fontweight="bold")
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.draw()
        plt.pause(3)   
        plt.close()
             
    elif dim == 3:
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(solutions[:, 0], solutions[:, 1], solutions[:, 2], c='Blue', label=f'Quần thể vòng lặp thứ {i}')
        ax.scatter(best_solution[0], best_solution[1], best_solution[2], c='Red', label='Giải pháp tốt nhất', s=100)
        plt.title(f'Quần thể vòng lặp thứ {i} (3D)', fontweight="bold")
        ax.set_xlabel('X1')
        ax.set_ylabel('X2')
        ax.set_zlabel('X3')
        ax.legend()
        plt.draw()
        plt.pause(3)  
        plt.close()
        
    else:
        # Giảm chiều xuống 2D bằng PCA
        pca = PCA(n_components=2)
        reduced_solutions = pca.fit_transform(solutions)
        reduced_best_solution = pca.transform(best_solution.reshape(1, -1))

        plt.figure(figsize=(8, 6))
        plt.scatter(reduced_solutions[:, 0], reduced_solutions[:, 1], c='Blue', label=f'Quần thể vòng lặp thứ {i} (PCA)')
        plt.scatter(reduced_best_solution[0, 0], reduced_best_solution[0, 1], c='Red', label='Giải pháp tốt nhất', s=100)
        plt.title(f'Quần thể vòng lặp thứ {i} (Giảm chiều)', fontweight="bold")
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.draw()
        plt.pause(3)  
        plt.close()