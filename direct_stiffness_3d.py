import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as axes

#truss structure data
E = 1e4
A = 0.111

nodes = []
bars = []

#test data
levels = 5
block_width = 2000
block_height = 2000
# nodes.append([0, 0, 0])               #node 0
# nodes.append([block_width, 0, 0])           #node 1
# nodes.append([block_width, block_width, 0])       #node 2
# nodes.append([0, block_width, 0])           #node 3
# nodes.append([0, 0, block_height])          #node 4
# nodes.append([block_width, 0, block_height])      #node 5
# nodes.append([block_width, block_width, block_height])  #node 6
# nodes.append([0, block_width, block_height])      #node 7
for i in range(levels + 1):
  nodes.append([0, 0, block_height * i])
  nodes.append([block_width, 0, block_height * i])
  nodes.append([block_width, block_width, block_height * i])
  nodes.append([0, block_width, block_height * i])

# #base beams
# bars.append([0, 1])
# bars.append([1, 2])
# bars.append([2, 3])
# bars.append([3, 0])
# #vertical beams
# bars.append([0, 4])
# bars.append([1, 5])
# bars.append([2, 6])
# bars.append([3, 7])
# #diagonal beams
# bars.append([0, 5])
# bars.append([5, 2])
# bars.append([2, 7])
# bars.append([7, 0])
# #top beams
# bars.append([4, 5])
# bars.append([5, 6])
# bars.append([6, 7])
# bars.append([7, 4])
# #base and top diagonals
# bars.append([0, 2])
# bars.append([4, 6])
for i in range(levels + 1):
  print(i)
  #base beams
  bars.append([0 + 4 * i, 1 + 4 * i])
  bars.append([1 + 4 * i, 2 + 4 * i])
  bars.append([2 + 4 * i, 3 + 4 * i])
  bars.append([3 + 4 * i, 0 + 4 * i])
  #base diag
  bars.append([0 + 4 * i, 2 + 4 * i])
  if (i < levels):
    #vertical beams
    bars.append([0 + 4 * i, 4 + 4 * i])
    bars.append([1 + 4 * i, 5 + 4 * i])
    bars.append([2 + 4 * i, 6 + 4 * i])
    bars.append([3 + 4 * i, 7 + 4 * i])
    #diagonal beams
    bars.append([0 + 4 * i, 5 + 4 * i])
    bars.append([5 + 4 * i, 2 + 4 * i])
    bars.append([2 + 4 * i, 7 + 4 * i])
    bars.append([7 + 4 * i, 0 + 4 * i])

nodes = np.array(nodes).astype(float)
bars = np.array(bars)

#Applied forces
P = np.zeros_like(nodes)
# P[0,0] = 1
# P[0,1] = -10
# P[0,2] = -10
# P[1,1] = -10
# P[1,2] = -10
# P[2,0] = 0.5
# P[5,0] = 0.6

#Support Displacement
Ur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Condition of DOF (1 = free, 0 = fixed)
DOFCON = np.ones_like(nodes).astype(int)
DOFCON[0,:] = 0
DOFCON[1,:] = 0
DOFCON[2,:] = 0
DOFCON[3,:] = 0

#Truss structural analysis 
def TrussAnalysis(): 
  NN = len(nodes)
  NE = len(bars)
  DOF = 3
  NDOF = DOF * NN
  #structural analysis
  d = nodes[bars[:,1],:] - nodes[bars[:,0],:]
  L = np.sqrt((d**2).sum(axis=1))
  angle = d.T/L
  a = np.concatenate((-angle.T,angle.T), axis=1)
  K = np.zeros([NDOF,NDOF])
  for k in range(NE):
    aux = DOF * bars[k,:]
    index = np.r_[aux[0]:aux[0] + DOF, aux[1]:aux[1] + DOF]
    ES = np.dot(a[k][np.newaxis].T*E*A, a[k][np.newaxis]) / L[k]
    K[np.ix_(index, index)] = K[np.ix_(index, index)] + ES
  freeDOF = DOFCON.flatten().nonzero()[0]
  supportDOF = (DOFCON.flatten() == 0).nonzero()[0]
  Kff = K[np.ix_(freeDOF, freeDOF)]
  Kfr = K[np.ix_(freeDOF, supportDOF)]
  Krf = Kfr.T
  Krr = K[np.ix_(supportDOF, supportDOF)]
  Pf = P.flatten()[freeDOF]
  Uf = np.linalg.solve(Kff, Pf)
  U = DOFCON.astype(float).flatten()
  U[freeDOF] = Uf
  U[supportDOF] = Ur
  U = U.reshape(NN, DOF)
  u = np.concatenate((U[bars[:,0]], U[bars[:,1]]), axis=1)
  N = E * A / L[:] * (a[:] + u[:]).sum(axis=1)
  R = (Krf[:] * Uf).sum(axis=1) + (Krr[:] * Ur).sum(axis=1)
  R = R.reshape(4, DOF)
  return np.array(N), np.array(R), U

def Plot(nodes, c, lt, lw, lg):
  plt.axes(projection='3d')
  for i in range(len(bars)):
    xi, xf = nodes[bars[i, 0], 0], nodes[bars[i, 1], 0]
    yi, yf = nodes[bars[i, 0], 1], nodes[bars[i, 1], 1]
    zi, zf = nodes[bars[i, 0], 2], nodes[bars[i, 1], 2]
    line, = plt.plot([xi, xf], [yi, yf], [zi, zf], color=c, linestyle=lt, linewidth=lw)
  line.set_label(lg)
  plt.legend(prop={'size': 10})

#Run test with known data
# N, R, U = TrussAnalysis()
# print('Axial Forces (positive = tension, negative = compression)')
# print(N[np.newaxis].T)
# print('Reaction Forces (positive = upward, negative = downward)')
# print(R)
# print('Deformation at nodes')
# print(U)
Plot(nodes, 'gray', '--', 1, 'Undeformed')
# scale = 1 #increase to make more evident in plot
# Dnodes = U * scale + nodes
# Plot(Dnodes, 'red', '-', 2, 'Deformed')
plt.show()