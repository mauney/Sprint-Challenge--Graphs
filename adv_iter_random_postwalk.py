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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

# player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def pick_unexplored(room):
    """Using a fixed order, return a room's first unexplored direction"""
    directions_sequence = ['n', 's', 'e', 'w']
    random.shuffle(directions_sequence)
    for direction in directions_sequence:
        explored = room.get(direction)
        if explored == '?':
            return direction
    return None


def find_unexplored(room, graph):
    """Look for closest unexplored exit and return a path to it"""
    # Create an empty queue
    q = []
    # Add a path to the room_id to the queue
    q.append([room])
    # Create an empty set to store visited rooms
    visited = set()
    # While the queue is not empty...
    while q:
        # Dequeue the first path
        path = q.pop(0)
        # grab the last room from the path
        room = path[-1]
        # if last room has an unexplored exit, return the path
        if pick_unexplored(graph[room]):
            rewind = []
            for i in range(1, len(path)):
                for room_direction, room_id in graph[path[i-1]].items():
                    if room_id == path[i]:
                        rewind.append(room_direction)
                        break
            return rewind
        # If it has not been visited...
        if room not in visited:
            # Mark it as visited
            visited.add(room)
            # Then add a path to all unvisited rooms to the back of the queue
            for next_room in graph[room].values():
                if next_room not in visited:
                    q.append(path + [next_room])

    return None


def explore_world(player, traversal_path):
    reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    # add first room to graph and initialize exits
    graph = {player.current_room.id: {}}
    for exits in player.current_room.get_exits():
        graph[player.current_room.id][exits] = '?'
    # enter a room in an unexplored direction
    direction = pick_unexplored(graph[player.current_room.id])
    if direction is None:
        print("Help, I am trapped in a room with no exits!")
        return -1
    
    prev_room = player.current_room
    player.travel(direction)
    traversal_path.append(direction)

    while True:
        # if new room, add to graph and initialize exits
        if player.current_room.id not in graph:
            graph[player.current_room.id] = {}
            for exits in player.current_room.get_exits():
                graph[player.current_room.id][exits] = '?'
        # if entered from unexplored direction, make connections between room and previous room
        if graph[player.current_room.id][reverse[direction]] == '?':
            graph[player.current_room.id][reverse[direction]] = prev_room.id
            graph[prev_room.id][direction] = player.current_room.id
        # if there is an unexplored exit:
        direction = pick_unexplored(graph[player.current_room.id])
        if direction:
            # enter room in that direction
            prev_room = player.current_room
            player.travel(direction)
            # add step to traversal_path
            traversal_path.append(direction)
        # else there is not an unexplored exit:
        else:
            # map a path to the closest unexplored exit
            return_path = find_unexplored(player.current_room.id, graph)
            # if there are no unexplored exits, traversal is complete
            if return_path is None:
                break
            # walk path while adding to traversal_path
            while return_path:
                direction = return_path.pop(0)
                player.travel(direction)
                traversal_path.append(direction)

    return graph


def traversal_test(traversal_path, seed, best_score):
    # Create new player and clear traversal_path
    player = Player(world.starting_room)
    traversal_path = []
    # print(f'traversal check: {traversal_path}')

    explore_world(player, traversal_path)

    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        if len(traversal_path) < best_score['best']:
            best_score['best'] = len(traversal_path)
            print(f'seed: {seed}')
            # print(f'traversal: {traversal_path}')
            print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
            print('----------------------------')
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f'seed: {seed}')
        # print(f'traversal: {traversal_path}')
        print(f"{len(traversal_path)} moves, {len(room_graph) - len(visited_rooms)} unvisited rooms")
        print('----------------------------')

    

best_score = {'best': 964}
for i in range(20000, 30000):
    random.seed(i)
    traversal_test(traversal_path, i, best_score)

# explore_world(player, traversal_path) 

# model = explore_world(player, traversal_path)
# print(f'traversal_path: {traversal_path}')
# print(f'model: {model}')


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
