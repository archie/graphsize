
import matplotlib.pyplot as plt
import numpy as np

size = {5000: 55121.113809549948, 10000: 57250.614733575734, 15000: 59161.128741237109, 20000: 59306.802628643381}

def plot_xy (x_list, y_list):
    plt.ylabel('Estimated graph size')
    plt.xlabel('Sample size')
    plt.title('Affect of sample size')
    
    plt.ylim([0,60000])
    plt.plot(x_list, y_list)
    plt.show()

def print_data(filename, size):
    out = open(filename, 'w')
    for k in size:
        out.write("%d \t %d\n" % (k, int(size[k])))
    out.close()

if __name__ == '__main__':
    print_data(size)
