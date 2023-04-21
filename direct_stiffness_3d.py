import numpy as np
import matplotlib.pyplot as plt

#truss structure data
E = 1e4
A = 0.111

nodes = []
bars = []

#test data
nodes.append([-37.5,0,200])
nodes.append([37.5,0,200])
nodes.append([-37.5,37.5,100])
nodes.append([37.5,37.5,100])
nodes.append([37.5,-37.5,100])
nodes.append([-37.5,-37.5,100])
nodes.append([-100,100,0])
nodes.append([100,100,0])
nodes.append([100,-100,0])
nodes.append([-100,-100,0])

bars.append([0,1])
bars.append([3,0])
bars.append([2,1])
bars.append([4,0])
bars.append([5,1])
bars.append([3,1])
bars.append([4,1])
bars.append([2,0])
bars.append([5,0])
bars.append([5,2])
bars.append([4,3])
bars.append([2,3])
bars.append([5,4])
bars.append([9,2])
bars.append([6,5])
bars.append([8,3])
bars.append([7,4])
bars.append([6,3])
bars.append([7,2])
bars.append([9,4])
bars.append([8,5])
bars.append([9,5])
bars.append([6,2])
bars.append([7,3])
bars.append([8,4])

nodes = np.array(nodes).astype(float)
bars = np.array(bars)

#Applied forces
P = np.zeros_like(nodes)
P[0,0] = 1
P[0,1] = -10
P[0,2] = -10
P[1,1] = -10
P[1,2] = -10
P[2,0] = 0.5
P[5,0] = 0.6

#Support Displacement
Ur = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Condition of DOF (1 = free, 0 = fixed)
DOFCON = np.ones_like(nodes).astype(int)
DOFCON[6,:] = 0
DOFCON[7,:] = 0
DOFCON[8,:] = 0
DOFCON[9,:] = 0

#Truss structural analysis 
def TrussAnalysis(): 
  NN = len(nodes)
  NE = len(bars)
  DOF = 2
  NDOF = DOF * NN
  #structural analysis
  d = nodes[bars[:,1],:] - nodes[bars[:,0],:]
  L = np.sqrt((d**2).sum(axis=1))
  angle = d.T/L
  a = np.concatenate((-angle.T,angle.T), axis=1)
  K = np.zeros([NDOF,NDOF])
  for k in range(NE):
    aux = 2*bars[k,:]
    index = np.r_[aux[0]:aux[0]+2,aux[1]:aux[1]+2]
    ES = np.dot(a[k][np.newaxis].T*E*A,a[k][np.newaxis])/L[k]
    K[np.ix_(index,index)] = K[np.ix_(index,index)] + ES
  freeDOF = DOFCON.flatten().nonzero()[0]
  supportDOF = (DOFCON.flatten() == 0).nonzero()[0]
  Kff = K[np.ix_(freeDOF,freeDOF)]
  Kfr = K[np.ix_(freeDOF,supportDOF)]
  Krf = Kfr.T
  Krr = K[np.ix_(supportDOF,supportDOF)]
  Pf = P.flatten()[freeDOF]
  Uf = np.linalg.solve(Kff,Pf)
  U = DOFCON.astype(float).flatten()
  U[freeDOF] = Uf
  U[supportDOF] = Ur
  U = U.reshape(NN, DOF)
  u = np.concatenate((U[bars[:,0]],U[bars[:,1]]),axis=1)
  N = E*A/L[:]*(a[:]+u[:]).sum(axis=1)
  R = (Krf[:]*Uf).sum(axis=1) + (Krr[:]*Ur).sum(axis=1)
  R = R.reshape(2,DOF)
  return np.array(N), np.array(R), U

def Plot(nodes,c,lt,lw,lg):
  plt.axes(projection='3d')
  for i in range(len(bars)):
    xi, xf = nodes[bars[i,0],0], nodes[bars[i,1],0]
    yi, yf = nodes[bars[i,0],1], nodes[bars[i,1],1]
    zi, zf = nodes[bars[i,0],2], nodes[bars[i,1],2]
    line, = plt.plot([xi, xf], [yi, yf], [zi, zf], color=c, linestyle=lt, linewidth=lw)
  line.set_label(lg)
  plt.legend(prop={'size': 8})
  plt.show()

#Run test
Plot(nodes, 'gray', '--', 1, 'Undeformed')