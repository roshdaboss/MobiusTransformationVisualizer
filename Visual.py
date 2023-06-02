#%%
import numpy as np
import matplotlib.pyplot as plt

def plot_complex_plane():
    """Plots the complex plane"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    return ax

def mobius_transformation(a, b, c, d, z):
    """Applies the Möbius transformation to the complex number z"""
    numerator = a * z + b
    denominator = c * z + d
    return numerator / denominator

def visualize_mobius_transformation(a, b, c, d):
    """Visualizes the effect of a Möbius transformation on the complex plane"""
    ax = plot_complex_plane()
    grid_size = 0.1
    x = np.arange(-10, 10, grid_size)
    y = np.arange(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    transformed_Z = mobius_transformation(a, b, c, d, Z)

    colors_before = np.zeros((len(y), len(x), 4))
    colors_after = np.zeros((len(y), len(x), 4))

    # Assign colors based on quadrants
    mask_top_right = np.logical_and(np.real(Z) > 0, np.imag(Z) > 0)
    colors_before[mask_top_right] = [1, 0, 0, 1]  # Top-right quadrant (red)
    colors_after[mask_top_right] = [0, 1, 0, 1]  # Top-right quadrant (green)

    mask_top_left = np.logical_and(np.real(Z) <= 0, np.imag(Z) > 0)
    colors_before[mask_top_left] = [0, 0, 1, 1]  # Top-left quadrant (blue)
    colors_after[mask_top_left] = [1, 1, 0, 1]  # Top-left quadrant (yellow)

    mask_bottom_left = np.logical_and(np.real(Z) <= 0, np.imag(Z) <= 0)
    colors_before[mask_bottom_left] = [0.5, 0, 0.5, 1]  # Bottom-left quadrant (purple)
    colors_after[mask_bottom_left] = [0, 0, 0, 1]  # Bottom-left quadrant (black)

    mask_bottom_right = np.logical_and(np.real(Z) > 0, np.imag(Z) <= 0)
    colors_before[mask_bottom_right] = [1, 0.5, 0, 1]  # Bottom-right quadrant (orange)
    colors_after[mask_bottom_right] = [1, 1, 1, 1]  # Bottom-right quadrant (white)

    ax.scatter(np.real(Z), np.imag(Z), c=colors_before.reshape(-1, 4), alpha=0.5)
    ax.scatter(np.real(transformed_Z), np.imag(transformed_Z), c=colors_after.reshape(-1, 4), alpha=0.5)

    # Display color assignments in the top-left corner
    ax.text(-9, 9, 'Color Assignments:', color='white', fontsize=8, ha='left', va='top')
    ax.text(-9, 8.5, 'Top-right quadrant:  Red (before) / Green (after)', color='white', fontsize=8, ha='left', va='top')
    ax.text(-9, 8, 'Top-left quadrant:  Blue (before) / Yellow (after)', color='white', fontsize=8, ha='left', va='top')
    ax.text(-9, 7.5, 'Bottom-left quadrant:  Purple (before) / Black (after)', color='white', fontsize=8, ha='left', va='top')
    ax.text(-9, 7, 'Bottom-right quadrant:  Orange (before) / White (after)', color='white', fontsize=8, ha='left', va='top')

    # Compute and display eigenvalues, algebraic multiplicities, and geometric multiplicities
    count = 7
    eigenvalues, _ = np.linalg.eig([[a, b], [c, d]])
    eigenvalues = np.round(eigenvalues, decimals=2)
    eigenvalues_unique = np.unique(eigenvalues)
    for eig_val in eigenvalues_unique:
        count -=0.5
        alg_mult = np.sum(eigenvalues == eig_val)
        geo_mult = np.sum(np.isclose(eigenvalues, eig_val))
        eig_val_text = f'Eigenvalue: {eig_val}'
        alg_mult_text = f'Alg. Mult.: {alg_mult}'
        geo_mult_text = f'Geo. Mult.: {geo_mult}'
        ax.text(-9, count, eig_val_text, color='white', fontsize=8, ha='left', va='top')
        ax.text(-9, count-0.5, alg_mult_text, color='white', fontsize=8, ha='left', va='top')
        ax.text(-9, count-1, geo_mult_text, color='white', fontsize=8, ha='left', va='top')
        count-=1

    ax.set_title('Möbius Transformation')
    plt.show()

# Example usage
visualize_mobius_transformation(0,1j,1,1j)
# %%
