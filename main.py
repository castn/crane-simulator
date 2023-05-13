"""
Main Script
"""

from craneSimulator.truss import crane
from craneSimulator.gui.plotting import plotter
from craneSimulator.simulation import analysis

# Youngs Module
E = 210e9  # 210GPa
# Cross section of each beam
A = 0.01  # 0.01m^2
DENSITY = 7850


if __name__ == '__main__':
    # Create crane
    crane.create_crane()

    total_length = crane.get_length()
    print(f'Total length: {(total_length / 1000):.5f} m')
    print(f'Total volume: {(total_length / 1000 * A):.5f} m^3')
    print(f'Total mass: {(total_length / 1000 * A * DENSITY):.5f} kg')
    print(
        f'Total cost: {(total_length / 1000 * A * DENSITY / 1000 * 1000):.2f} euros')

    # Override Python arrays with Numpy arrays, nodes are of type float64
    nodes, beams = crane.get_crane()

    # Run analysis
    analysis.generate_conditions(nodes)
    N, R, U = analysis.analyze(nodes, beams, E, A)
    # print('Axial Forces (positive = tension, negative = compression)')
    # print(N[np.newaxis].T)
    # print('Reaction Forces (positive = upward, negative = downward)')
    # print(R)
    print('Deformation at nodes')
    print(U)
    plotter.plot(nodes, beams, 'gray', '--', 'Undeformed')
    scale = 10 # increase to make more evident in plot
    deformed_nodes = U * scale + nodes
    plotter.plot(deformed_nodes, beams, 'red', '-', 'Deformed')
    plotter.display()
