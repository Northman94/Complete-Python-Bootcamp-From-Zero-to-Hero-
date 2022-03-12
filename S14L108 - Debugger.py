
import pdb  # Python DeBugger


x = [1, 2, 3]
y = 2
z = 3

result = y + z



# Open a trace, before area where Error is supposed to be:

pdb.set_trace()

result2 = y + x




# Put "q" in debugger to quit.

