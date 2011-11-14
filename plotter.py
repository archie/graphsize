
import matplotlib.pyplot as plt
import numpy as np

def print_data(filename, size):
    out = open(filename, 'w')
    keys = size.keys()
    keys.sort()
    for k in keys:
        out.write("%d \t %d\n" % (k, int(size[k])))
    out.close()

if __name__ == '__main__':
#    print_data(size)
