from itertools import permutations

directions = ['n', 'e', 's', 'w']

for perm in permutations(directions):
    print(perm)

direction_sequences = [('n', 'e', 's', 'w'),
                       ('n', 'e', 'w', 's'),
                       ('n', 's', 'e', 'w'),
                       ('n', 's', 'w', 'e'),
                       ('n', 'w', 'e', 's'),
                       ('n', 'w', 's', 'e'),
                       ('e', 'n', 's', 'w'),
                       ('e', 'n', 'w', 's'),
                       ('e', 's', 'n', 'w'),
                       ('e', 's', 'w', 'n'),
                       ('e', 'w', 'n', 's'),
                       ('e', 'w', 's', 'n'),
                       ('s', 'n', 'e', 'w'),
                       ('s', 'n', 'w', 'e'),
                       ('s', 'e', 'n', 'w'),
                       ('s', 'e', 'w', 'n'),
                       ('s', 'w', 'n', 'e'),
                       ('s', 'w', 'e', 'n'),
                       ('w', 'n', 'e', 's'),
                       ('w', 'n', 's', 'e'),
                       ('w', 'e', 'n', 's'),
                       ('w', 'e', 's', 'n'),
                       ('w', 's', 'n', 'e'),
                       ('w', 's', 'e', 'n')]
