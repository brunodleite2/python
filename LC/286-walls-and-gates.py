# BEST SOLUTION... Look for gates such as a maze!
class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        EMPTY = 2**31 -1
        WALL = -1
        GATE = 0

        def shortest_path(r, c, dist=0):
            dist += 1

            # LOOP
            if dist > max(len(rooms), len(rooms[0])):
                return EMPTY

            # BORDERS
            if r < 0 or c < 0 or r > len(rooms) - 1 or c > len(rooms[0]) - 1: # TODO: maybe empty
                return EMPTY

            room = rooms[r][c]

            if room == WALL:
                return EMPTY

            if room == GATE:
                return dist


            return min(shortest_path(r - 1, c, dist),  shortest_path(r + 1, c, dist),
                       shortest_path(r, c - 1, dist), shortest_path(r, c + 1, dist))


        if not rooms:
            return rooms

        for r in range(len(rooms)):
            for c in range(len(rooms[0])):

                room = rooms[r][c]

                if room in [ WALL, GATE ]:
                    continue

                room = min(shortest_path(r - 1, c),  shortest_path(r + 1, c),
                           shortest_path(r, c - 1), shortest_path(r, c + 1))

                rooms[r][c] = room

        return rooms
