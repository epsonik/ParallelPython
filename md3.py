import math, time
import pp

def part_sum(start, end):
    """Calculates partial sum"""
    sum = 0
    for x in xrange(start, end):
        if x % 2 == 0:
           sum -= 1.0 / x
        else:
           sum += 1.0 / x
    return sum

print """Usage: python dynamic_ncpus.py"""
start = 1
end = 20000000

# Divide the task into 64 subtasks
parts = 64
step = (end - start) / parts + 1

# Create jobserver
job_server = pp.Server()

# Execute the same task with different amount of active workers and measure the time
ncpus=4
job_server.set_ncpus(ncpus)
jobs = []
start_time = time.time()
print "Starting ", job_server.get_ncpus(), " workers"
for index in xrange(parts):
    starti = start+index*step
    endi = min(start+(index+1)*step, end)
    # Submit a job which will calculate partial sum
    # part_sum - the function
    # (starti, endi) - tuple with arguments for part_sum
    # () - tuple with functions on which function part_sum depends
    # () - tuple with module names which must be imported before part_sum execution
    jobs.append(job_server.submit(part_sum, (starti, endi)))

    # Retrieve all the results and calculate their sum
part_sum1 = sum([job() for job in jobs])
    # Print the partial sum
print "Partial sum is", part_sum1, "| diff =", math.log(2) - part_sum1

print "Time elapsed: ", time.time() - start_time, "s"
