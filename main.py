"""
Main Script
"""

import crane
import plotter

# Youngs Module
E = 210e6  # 210GPa
# Cross section of each beam
A = 0.01  # 0.01m^2
DENSITY = 7850


if __name__ == '__main__':
    # Create crane
    crane.create_crane()
    total_length = crane.get_length()
    print(f'Total length: {total_length / 1000:.5f} m')
    print(f'Total volume: {total_length / 1000 * A:.5f} m^3')
    density = 7850
    print(f'Total mass: {total_length / 1000 * A * density:.5f} kg')
    print(f'Total cost: {(total_length / 1000 * A * density / 1000 * 1000):.2f} euros')

    # Override Python arrays with Numpy arrays, nodes are of type float64
    nodes, bars = crane.get_crane()

    # Run test with known data
    # N, R, U = TrussAnalysis()
    # print('Axial Forces (positive = tension, negative = compression)')
    # print(N[np.newaxis].T)
    # print('Reaction Forces (positive = upward, negative = downward)')
    # print(R)
    # print('Deformation at nodes')
    # print(U)
    plotter.plot(nodes, bars, 'gray', '--', 'Undeformed')
    # scale = 1 #increase to make more evident in plot
    # Dnodes = U * scale + nodes
    # plot(nodes, 'red', '-', 'Deformed')
    plotter.display()
