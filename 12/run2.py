# Take the input of part 1 to fill in part 2
at1k = 45120 # the value at iteration 1000
delta = 45 # the delta between each step at iteration 1000 (assuming convergence by then)
iters = 50000000000
at5b = at1k + (delta * (iters-1000))
print at5b
