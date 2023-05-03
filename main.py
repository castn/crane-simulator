"""
Main Script
"""

import numpy as np
import crane
import plotter
import analysis

# Youngs Module
E = 210e9  # 210GPa
# Cross section of each beam
A = 0.01  # 0.01m^2
DENSITY = 7850


if __name__ == '__main__':
    # Create crane
    tower_height = 4000
    # while tower_height < 5000 or tower_height > 10000:
    #     tower_height = float(input('Enter the height of the tower in mm: '))
    tower_seg_height = 2000
    # while tower_seg_height < 500 or tower_seg_height > 2000:
    #     tower_seg_height = float(input('Enter the height of each segment of the tower in mm: '))
    tower_width = 2000
    # while width < 500 or width > 2000:
    #     width = float(input('Enter the width of the crane in mm: '))
    if np.sqrt(tower_seg_height ** 2 + tower_width ** 2) > 2000:
        print(f'Error! The diagonal elements will have a length of {np.sqrt(tower_seg_height ** 2 + tower_width ** 2):.3f}mm which is greater than the 2000mm allowed!')
    
    crane.create_crane(tower_height, tower_seg_height, tower_width)
    total_length = crane.get_length()
    print(f'Total length: {(total_length / 1000):.5f} m')
    print(f'Total volume: {(total_length / 1000 * A):.5f} m^3')
    print(f'Total mass: {(total_length / 1000 * A * DENSITY):.5f} kg')
    print(f'Total cost: {(total_length / 1000 * A * DENSITY / 1000 * 1000):.2f} euros')

    # Override Python arrays with Numpy arrays, nodes are of type float64
    nodes, beams = crane.get_crane()
    
    # Condition of DOF (0 = fixed, 1 = free)
    dof_condition = np.ones_like(nodes).astype(int)
    dof_condition[0, :] = 0
    dof_condition[1, :] = 0
    dof_condition[2, :] = 0
    dof_condition[3, :] = 0
    
    # Applied forces
    p = np.zeros_like(nodes)
    p[16, 2] = -500
    p[17, 2] = -500
    p[20, 2] = -100
    p[21, 2] = -100

    # Run analysis
    # N, R, U = analysis.analyze(nodes, beams, dof_condition, p, E, A)
    # print('Axial Forces (positive = tension, negative = compression)')
    # print(N[np.newaxis].T)
    # print('Reaction Forces (positive = upward, negative = downward)')
    # print(R)
    # print('Deformation at nodes')
    # print(U)
    plotter.plot(nodes, beams, 'gray', '--', 'Undeformed')
    # scale = 1 #increase to make more evident in plot
    # Dnodes = U * scale + nodes
    # plotter.plot(Dnodes, 'red', '-', 'Deformed')
    plotter.display()
