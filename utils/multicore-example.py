from multiprocessing import Pool


# Define a worker — a function which will be executed in parallel
def worker(x):
    return sum([k for k in range(0, x)])


num_processors = 3

# Create a pool of processors
p = Pool(processes=num_processors)

N = 4 * 10 ** 4

output = p.map(worker, [i for i in range(0, N)])
