# Code from https://getfem-examples.readthedocs.io/en/latest/cantilever.html

import getfem as gf
import numpy as np
import pandas as pd
import pyvista as pv
from IPython.display import Markdown

from pyvirtualdisplay import Display

display = Display(visible=True, size=(1280, 1024))
display.start()

cases = [
    "case11",
    "case12",
    "case13",
    "case14",
    "case21",
    "case22",
    "case23",
    "case24",
    "case31",
    "case32",
    "case33",
    "case34",
    "case41",
    "case42",
    "case43",
    "case44",
]
xs = [4, 4, 4, 16, 4, 4, 4, 16, 4, 4, 4, 16, 4, 4, 4, 16, ]
ys = [1, 2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8, 1, 2, 4, 8, ]
fem_names = [
    "FEM_PK(1, 2)",
    "FEM_PK(1, 2)",
    "FEM_PK(1, 2)",
    "FEM_PK(1, 2)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK(1, 1)",
    "FEM_PK_WITH_CUBIC_BUBBLE(1, 1)",
    "FEM_PK_WITH_CUBIC_BUBBLE(1, 1)",
    "FEM_PK_WITH_CUBIC_BUBBLE(1, 1)",
    "FEM_PK_WITH_CUBIC_BUBBLE(1, 1)",
]
methods = [
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(2)",
    "IM_GAUSS1D(2)",
    "IM_GAUSS1D(2)",
    "IM_GAUSS1D(2)",
    "IM_GAUSS1D(0)",
    "IM_GAUSS1D(0)",
    "IM_GAUSS1D(0)",
    "IM_GAUSS1D(0)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
    "IM_GAUSS1D(4)",
]

pd.options.display.float_format = "{:.2f}".format
data = []
columns = ["Case Name", "Mesh", "Finite Element Method", "Integration Method"]
for case, x, y, fem_name, method in zip(cases, xs, ys, fem_names, methods):
    data.append([case, str(x) + "x" + str(y), fem_name, method])
df = pd.DataFrame(data=data, columns=columns)
Markdown(df.to_markdown())

p = pv.Plotter(shape=(4, 4))

# Mesh

# Size of the model L = 10 mm in length, h = 1 mm in height, and b = 1 mm in depth
L = 10.0
b = 1.0
h = 1.0
meshs = []
for case, x, y in zip(cases, xs, ys):
    X = np.arange(x + 1) * L / x
    Y = np.arange(y + 1) * h / y
    mesh = gf.Mesh("cartesian", X, Y)
    meshs.append(mesh)
    mesh.export_to_vtk("mesh_" + case + ".vtk", "ascii")

# Outputs an image of each mesh
for i in range(4):
    for j in range(4):
        p.subplot(i, j)
        mesh = pv.read("mesh_" + cases[i * 4 + j] + ".vtk")
        p.add_text(cases[i * 4 + j], font_size=10)
        p.add_mesh(mesh, color="tan", show_edges=True)

p.show(cpos="xy")

# Region
# Sets the area on the left side of the mesh where the Dirichlet condition is set. The right side sets the area for setting the Neumann condition.
TOP_BOUND = 1
RIGHT_BOUND = 2
LEFT_BOUND = 3
BOTTOM_BOUND = 4

for mesh in meshs:
    fb1 = mesh.outer_faces_with_direction([0.0, 1.0], 0.01)
    fb2 = mesh.outer_faces_with_direction([1.0, 0.0], 0.01)
    fb3 = mesh.outer_faces_with_direction([-1.0, 0.0], 0.01)
    fb4 = mesh.outer_faces_with_direction([0.0, -1.0], 0.01)
    mesh.set_region(TOP_BOUND, fb1)
    mesh.set_region(RIGHT_BOUND, fb2)
    mesh.set_region(LEFT_BOUND, fb3)
    mesh.set_region(BOTTOM_BOUND, fb4)

# FEM
# Create a MeshFem object and associate the mesh with the finite element method.
fems = []
for fem_name in fem_names:
    fems.append(gf.Fem("FEM_PRODUCT(" + fem_name + "," + fem_name + ")"))

mfus = []
for mesh, fem in zip(meshs, fems):
    mfu = gf.MeshFem(mesh, 2)
    mfu.set_fem(fem)
    mfus.append(mfu)

# Integral method
# Associate the integration method with the mesh
ims = []
for method in methods:
    ims.append(gf.Integ("IM_PRODUCT(" + method + ", " + method + ")"))

mims = []
for mesh, im in zip(meshs, ims):
    mim = gf.MeshIm(mesh, im)
    mims.append(mim)

# Variable
# Define the model object and set the variable “u”.
mds = []
for mfu in mfus:
    md = gf.Model("real")
    md.add_fem_variable("u", mfu)
    mds.append(md)

# Properties
# Define properties as constants for the model object. The Young’s modulus of steel is E=205000×106N/m2. Also set Poisson’s ratio ν=0.0 to ignore the Poisson effect.

E = 10000  # N/mm2
Nu = 0.0

for md in mds:
    md.add_initialized_data("E", E)
    md.add_initialized_data("Nu", Nu)

# Plane Strain Element
# Defines the plane strain element for variable ‘u’.
for md, mim in zip(mds, mims):
    md.add_isotropic_linearized_elasticity_brick_pstrain(mim, "u", "E", "Nu")

# Boundary Conditions
# Set the Dirichlet condition for the region on the left side.
for (md, mim, mfu, fem) in zip(mds, mims, mfus, fems):
    if fem.is_lagrange():
        md.add_Dirichlet_condition_with_simplification("u", LEFT_BOUND)
    else:
        md.add_Dirichlet_condition_with_multipliers(mim, "u", mfu, LEFT_BOUND)

# Set the Neumann boundary condition on the right side
F = 1.0  # N/mm2
for (md, mfu, mim) in zip(mds, mfus, mims):
    md.add_initialized_data("F", [0, F / (b * h)])
    md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)

# Solving
# Solve the simultaneous equations of the model object to find the value of the variable ‘u’.
for md in mds:
    md.solve()
# The constraint on the left end has a displacement of 0.0.
for md, mfu, case in zip(mds, mfus, cases):
    u = md.variable("u")
    dof = mfu.basic_dof_on_region(LEFT_BOUND)
    np.assert_almost_equal(abs(np.max(u[dof])), 0.0)

# Review results
# Output and visualize the results of each case to vtk files
for md, mfu, case in zip(mds, mfus, cases):
    u = md.variable("u")
    mfu.export_to_vtk("u_" + case + ".vtk", "ascii", mfu, u, "u")

# deformation diagram of case11
p = pv.Plotter(shape=(4, 4))

for i in range(4):
    for j in range(4):
        p.subplot(i, j)
        mesh = pv.read("u_" + cases[i * 4 + j] + ".vtk")
        p.add_text(cases[i * 4 + j], font_size=10)
        p.add_mesh(mesh.warp_by_vector("u"), color="tan", show_edges=True)

p.show(cpos="xy")



