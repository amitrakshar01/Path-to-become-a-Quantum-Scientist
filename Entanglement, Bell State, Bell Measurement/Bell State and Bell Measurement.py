#!/usr/bin/env python
# coding: utf-8

# In[5]:


import qiskit as qk


# # Bell State
# 
# Hadamard Gate on Qubit 0
# <br>CNOT Gate on Qubit 1 Controlled on Qubit 0

# In[6]:


q = qk.QuantumRegister(2)
c = qk.ClassicalRegister(2)
circuit = qk.QuantumCircuit(q , c)
circuit.h(q[0])
circuit.cx(q[0] , q[1])
circuit.measure(q[0] , c[0])
circuit.measure(q[1] , c[1])
print(circuit)


# # Bell Measurement
# 
# CNOT Gate on Qubit 1 controlled on Qubit 0
# <br>Hadamard Gate on Qubit 0
# <br>Sigma X Gate on both Qubit 0 and Qubit 1

# In[8]:


qm = qk.QuantumRegister(2)
cm = qk.ClassicalRegister(2)
circuitm = qk.QuantumCircuit(qm , cm)
circuitm.cx(qm[0] , qm[1])
circuitm.h(qm[0])
circuitm.x(qm[0])
circuitm.x(qm[1])
circuitm.measure(qm[0] , cm[0])
circuitm.measure(qm[1] , cm[1])
print(circuitm)

