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
    print(f'Total length: {crane.get_length() / 1000} m')
    print(f'Total volume: {crane.get_length() / 1000 * A} m^3')
    print(
        f'Total mass: {crane.get_length() / 1000 * A * DENSITY} kg with a cost of {crane.get_length() / 1000 * A * DENSITY / 1000 * 1000} euros')
    # crane.create_counter_jib()

    # Override Python arrays with Numpy arrays, nodes are of type float64
    nodes, bars = crane.get_counter_jib()

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
