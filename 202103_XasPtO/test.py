import numpy
a=numpy.array([[0.0],[1.0]])
print(a)
b=numpy.append(a,numpy.reshape([0.1,0.2],(2,1)),axis=1)
print(b)
