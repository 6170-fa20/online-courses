#!/usr/bin/python
import math

def get_e(u, v):
    return ((u * (math.e ** v)) - (2 * v * (math.e ** (-u)))) ** 2

def get_partial_diff_u(u, v):
    t1 = (math.e ** v)
    t2 = 2 * v * (math.e ** (-u))
    return 2 * (t1 + t2) * ((u * t1) - t2)

def get_partial_diff_v(u, v):
    t1 = u * (math.e ** v)
    t2 = 2 * (math.e ** (-u))
    return 2 * (t1 - (v * t2)) * (t1 - t2)

w = [1.00, 1.00]         # initial weights (u,v)
threshold = 10 ** (-14)  # required error value
learning_rate = 0.1      # the learning rate (eta)
i = 0

while True:
    i += 1
    error = get_e(w[0], w[1])

    # terminate if threshold achieved
    if error < threshold:
        break
    
    # update weights
    w = [w[0] - (learning_rate * get_partial_diff_u(w[0], w[1])),
         w[1] - (learning_rate * get_partial_diff_v(w[0], w[1]))]

# print the results
print 'Number of iterations =', i
print 'Final weights =', w
