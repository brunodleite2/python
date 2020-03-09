class Solution:

    def __init__(self):
        self.grid = None

    def cleanup_surround_points(self, row, column):
        if self.grid[row][column] == "0":
            return

        self.grid[row][column] = "0"

        if row: # not 0
            self.cleanup_surround_points(row - 1, column)


        if row < len(self.grid) - 1:
            self.cleanup_surround_points(row + 1, column)

        if column: # not 0
            self.cleanup_surround_points(row, column - 1)

        if column < len(self.grid[row]) - 1:
            self.cleanup_surround_points(row, column + 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        number_island = 0

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                point_data = self.grid[row][column]

                if point_data == "1":
                    number_island += 1
                    self.cleanup_surround_points(row, column)

        return number_island


### Solution 2
class Solution:

    def __init__(self):
        self.grid = None
        self.clusters = None

    def ckeck_surround_points(self, row, column, island_id):
        if row: # not 0
            point_data = self.grid[row -1 ][column]
            if point_data == "1" and (row - 1, column) not in self.clusters:
                self.clusters[(row - 1, column)] = island_id
                self.ckeck_surround_points(row -1 , column, island_id)

        if row < len(self.grid) - 1:
            point_data = self.grid[row + 1 ][column]
            if point_data == "1" and (row + 1, column) not in self.clusters:
                self.clusters[(row + 1, column)] = island_id
                self.ckeck_surround_points(row + 1 , column, island_id)

        if column: # not 0
            point_data = self.grid[row][column -1 ]
            if point_data == "1" and (row, column - 1) not in self.clusters:
                self.clusters[(row, column - 1)] = island_id
                self.ckeck_surround_points(row , column -1 , island_id)

        if column < len(self.grid[row]) - 1:
            point_data = self.grid[row][column + 1 ]
            if point_data == "1" and (row, column + 1) not in self.clusters:
                self.clusters[(row, column + 1)] = island_id
                self.ckeck_surround_points(row , column + 1, island_id)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.clusters = {}

        number_island = 0

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                point_data = self.grid[row][column]

                if point_data == "1" and (row, column) not in self.clusters:
                    number_island += 1
                    self.clusters[(row, column)] = number_island
                    self.ckeck_surround_points(row, column, number_island)

        print(self.clusters)
        return number_island





