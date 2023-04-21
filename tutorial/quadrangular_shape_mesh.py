# Code from https://getfem-examples.readthedocs.io/en/latest/demo_unit_disk.html#Quadrangular-shape-case

import getfem as gf
import numpy as np
import pyvista as pv

from pyvirtualdisplay import Display

# Mesh generation
mo = gf.MesherObject("rectangle", [-1.0, -1.0], [1.0, 1.0])
h = 0.1
K = 2
mesh = gf.Mesh("generate", mo, h, K)

# Boundary selection
outer_faces = mesh.outer_faces()
OUTER_BOUND = 1
mesh.set_region(OUTER_BOUND, outer_faces)
sl = gf.Slice(("none",), mesh, 1)
sl.export_to_vtk("sl.vtk", "ascii")

# Mesh draw
display = Display(visible=True, size=(1280, 1024))
display.start()
p = pv.Plotter()
m = pv.read("sl.vtk")
p.add_mesh(m, show_edges=True)
pts = m.points
p.show(window_size=[512, 384], cpos="xy")
display.stop()

# Definition of finite element methods and integration method
mfu = gf.MeshFem(mesh, 1)
elements_degree = 2
mfu.set_classical_fem(elements_degree)
mim = gf.MeshIm(mesh, pow(elements_degree, 2))

# Model definition
md = gf.Model("real")
md.add_fem_variable("u", mfu)

# Poisson’s equation
md.add_Laplacian_brick(mim, "u")
F = 1.0
md.add_fem_data("F", mfu)
md.set_variable("F", np.repeat(F, mfu.nbdof()))
md.add_source_term_brick(mim, "u", "F")
md.add_Dirichlet_condition_with_multipliers(mim, "u", elements_degree - 1, OUTER_BOUND)

# Model solve
md.solve()

# Export/visualization of the solution
U = md.variable("u")
sl.export_to_vtk("u.vtk", "ascii", mfu, U, "U")

display = Display(visible=0, size=(1280, 1024))
display.start()
p = pv.Plotter()
m = pv.read("u.vtk")
contours = m.contour()
p.add_mesh(m, show_edges=False)
p.add_mesh(contours, color="black", line_width=1)
p.add_mesh(m.contour(8).extract_largest(), opacity=0.1)
pts = m.points
p.show(window_size=[384, 384], cpos="xy")
display.stop()
