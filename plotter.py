def run(no_of_times, function, args):
    collected_results = [function(**args) for x in xrange(no_of_times)]
    average = sum(collected_results) / no_of_times
    return average

def print_data(filename, data):
    out = open(filename, 'w')
    keys = data.keys()
    keys.sort()
    for k in keys:
        out.write("%d \t %d\n" % (k, int(data[k])))
    out.close()
