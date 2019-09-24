#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# Challenge: Solve all the problems with Monte Carlo

# # Question 1
# ## Project Euler 
# ### Under the rainbow (no 493)
# 
# https://projecteuler.net/problem=493
# 
# 70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
# 
# What is the expected number of distinct colours in 20 randomly picked balls?

# In[2]:


# Solution 1
n = 10000
urn = [1,2,3,4,5,6,7] * 10
trials = []
for _ in range(n):
    choices = np.random.choice(urn, 20)
    distinct_colors = len(np.unique(choices))
    trials.append(distinct_colors)
sum(trials)/len(trials)


# # Question 2
# 
# Estimate the number pi

# In[3]:


# Solution 2
# Visualization of the procedure
# Ratio of dots falling into the circle is pi/4

# Generate quarter circle
x = np.arange(0,1.01,0.01)
y = np.sqrt(1-x**2)
plt.figure(figsize=(5,5))
plt.plot(x,y)

# Generate random points in 1 by 1 square
n = 500
dots_x = np.random.uniform(0,1,n)
dots_y = np.random.uniform(0,1,n)

# dots outside the circle
plt.scatter(dots_x[dots_y>np.sqrt(1-dots_x**2)], dots_y[dots_y>np.sqrt(1-dots_x**2)])
# dots inside the circle
plt.scatter(dots_x[dots_y<=np.sqrt(1-dots_x**2)], dots_y[dots_y<=np.sqrt(1-dots_x**2)])


# In[4]:


# Solution 2
# Generate points
n = 10000000
dots_x = np.random.uniform(0,1,n)
dots_y = np.random.uniform(0,1,n)

# array with dots 
# inside the circle as True (1)
# outside the circle as False (0)
counter = dots_y<np.sqrt(1-dots_x**2)

# True/(True+False)
ratio = np.mean(counter)

# ratio = pi/4
# estimate = ratio*4
print('Estimate:', ratio*4, 'Pi:', np.pi)


# # Question 3
# 
# You are fabricating an electrode structure etched into the glass. First you etch the glass (100 nm) and then coat an electrode (95 nm) with an insulator on top (4 nm). Your customer requires the remaining gap ( = trench - electrode - insulator) to be between 0-2 nm. Given that your process parameters are normally distributed as Trench N(100, 2), Electrode N(95, 1) and Insulator N(4, 0.5). Guess the percentage of your products that will meet the spec and suggest improvements.

# In[5]:


# Solution 3
n = 100
trench = np.random.normal(100, 2, n)
electrodes = np.random.normal(95, 1, n)
silica = np.random.normal(4, 0.5, n)
gap = trench - electrodes - silica
plt.hist(gap[gap>2], color = 'red')
plt.hist(gap[gap<0], color = 'red')
plt.hist(gap[(gap>=0) & (gap<=2)], color = 'blue')
print(sum((gap>=0) & (gap<=2))/len(gap)*100, '% meets the spec')


# # Question 4
# ## Mont Hall Problem
# 
# Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
# 
# https://en.wikipedia.org/wiki/Monty_Hall_problem

# In[6]:


# Solution 4
'''
Assume the car is always behind the door 1
If you choose to stay, you only win if you choose 1 in the first place
If you choose to switch, you only win if you didn't choose 1 in the first place

P(stay) = Randomly choose from [1,2,3], calculate the ratio of 1's.
P(switch) = 1-P(stay)
'''
n = 10000
P_stay = sum(np.random.randint(1,4,n)==1)/n
P_switch = 1-P_stay
P_switch, P_stay


# # Question 5
# ## Project Euler 
# ### Flea Circus (no 213)
# 
# https://projecteuler.net/problem=213
#     
# A 30×30 grid of squares contains 900 fleas, initially one flea per square.
# When a bell is rung, each flea jumps to an adjacent square at random (usually 4 possibilities, except for fleas on the edge of the grid or at the corners).
# 
# What is the expected number of unoccupied squares after 50 rings of the bell?

# In[7]:


# Solution 5
n = 10
rings_of_the_bell = 50
board_size = (30,30)
trials = []

for _ in range(n):
    A = np.ones(board_size) # 900 fleas
    for _ in range(rings_of_the_bell):
        A_next = A.copy()
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                moves = np.array([[0,1],[0,-1],[1,0],[-1,0]])
                
                # update possible moves for corners/edges
                if i==0:
                    moves = moves[moves[:,0]!=-1]
                if i==A.shape[0]-1:
                    moves = moves[moves[:,0]!=1]
                if j==0:
                    moves = moves[moves[:,1]!=-1]
                if j==A.shape[1]-1:
                    moves = moves[moves[:,1]!=1]
                
                for flea in range(int(A[i,j])):
                    move = np.random.choice(range(len(moves)))
                    a,b = moves[move]
                    A_next[i+a,j+b]=A_next[i+a,j+b]+1
                    A_next[i,j]-=1
                            
        A=A_next.copy() # move on to the next bell
    trials.append(np.sum(A==0)) # count unoccupied squares

np.mean(np.array(trials))


# In[ ]:




