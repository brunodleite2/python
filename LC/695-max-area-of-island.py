class Solution:
    def __init__(self):
        self.grid = None
        self.clusters = None
        self.island_size = None

    def update_results(self, row, column, island_id):
        self.clusters[(row, column)] = island_id
        self.update_island_size(island_id)
        self.ckeck_surround_points(row, column, island_id)

    def ckeck_surround_points(self, row, column, island_id):
        if row: # not 0
            point_data = self.grid[row -1 ][column]

            if point_data == 1 and (row - 1, column) not in self.clusters:
                self.update_results(row - 1, column, island_id)

        if row < len(self.grid) - 1:
            point_data = self.grid[row + 1 ][column]
            if point_data == 1 and (row + 1, column) not in self.clusters:
                self.update_results(row + 1, column, island_id)

        if column: # not 0
            point_data = self.grid[row][column -1 ]
            if point_data == 1 and (row, column - 1) not in self.clusters:
                self.update_results(row, column - 1, island_id)

        if column < len(self.grid[row]) - 1:
            point_data = self.grid[row][column + 1 ]
            if point_data == 1 and (row, column + 1) not in self.clusters:
                self.update_results(row, column + 1, island_id)


    def update_island_size(self, island_id):
        if island_id not in self.island_size:
            self.island_size[island_id] = 1
            return

        self.island_size[island_id] += 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.clusters = {}
        self.island_size = {} # id:size

        island_id = 0

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                point_data = self.grid[row][column]

                if point_data == 1 and (row, column) not in self.clusters:
                    island_id += 1
                    self.update_results(row, column, island_id)


        if not self.island_size.values():
            return 0

        return max(self.island_size.values())