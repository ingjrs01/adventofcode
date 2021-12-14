import time
startTime = time.time()

# read lines into a list
with open ('input', 'r') as input_file:
    lines = []
    for line in input_file:
        lines.append( line.strip() )


## helper functions
def wait_for_next_departure( time_now, bus_line ):
    return bus_line - ( time_now % bus_line )


def next_departure( operating_buses, start_time ):
    waiting_times = []
    for bus in operating_buses:
        waiting_times.append( wait_for_next_departure( time_arrival_port, bus ) )
    next_time = min( waiting_times )
    next_bus = operating_buses[ waiting_times.index( next_time ) ]
    return next_bus, next_time


from fractions import gcd

# least common multiplier
def lcm( a, b ):
    return a * b / gcd( a, b )


# magic time = timestamp so bus-a is able to depart, and bus-b departs at timestamp + offset
def magic_time( a, b, offset, increment, initial_time = 0 ):
    magic_found = False
    time = initial_time - offset
    while not magic_found:
        if ( ( time + offset ) % b  != 0 ) or ( time % a != 0 ):
            time += increment
        else:
            magic_found = True
    return time


def next_magic_time( operating_buses, offset_buses, bus_schedule ):
    initial_time = 0
    last_bus = len( operating_buses ) - 1
    time_increment = operating_buses[ last_bus ]
    i = last_bus - 1
    while i >= 0:
        offset_iteration = offset_buses[i+1] - offset_buses[i]
        initial_time = magic_time( operating_buses[i], operating_buses[i+1], offset_iteration, time_increment, initial_time )
        time_increment = lcm( operating_buses[i], time_increment )
        i -= 1
    return initial_time


# parse inputs
time_arrival_port = int( lines[0] )
bus_schedule = lines[1].split(',')


# answers
operating_buses = [ int( bus ) for bus in bus_schedule if bus != 'x' ]

earliest_bus = next_departure( operating_buses, time_arrival_port )
star_25 = earliest_bus[0] * earliest_bus[1]


offset_buses = [ bus_schedule.index( str( bus ) ) for bus in operating_buses ]
star_26 = next_magic_time( operating_buses, offset_buses, bus_schedule )

print( 'ID of earliest bus * waiting minutes (star 25): {}'.format( star_25 ) )
print( 'Earliest *magic* timestamp (star 26): {}'.format( star_26 ) )


# calculate & output execution time
executionTime = (time.time() - startTime)
print
print( 'Execution time in seconds: ' + str(executionTime) )

