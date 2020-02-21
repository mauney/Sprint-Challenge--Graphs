from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# make a list of all the terminals
# map the shortest path to each
print(world.room_grid)
terminals = [room.id for room in [row for row in world.room_grid] if room and len(room.get_exits()) == 1]
print(terminals)
# print(f'room exits: ')
for row in world.room_grid:
    for room in row:
        if room and len(room.get_exits()) == 1:
            print(room.id)


## Maybe try this afterwards ##
# walk a path until it termintates
# keep track of non-terminal rooms for all walks
# categorize it as a loop if exits exist other than the one entered by
# otherwise, call it a terminal
# find all of these, recording the path taken and the number of steps
# stop when all edges have been walked
# this may miss a loop - but maybe not if the