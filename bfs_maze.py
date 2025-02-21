import time

from collections import deque

class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('\033[96m*\x1b[0m', end=' ')   # print a blue *
                else:
                    print(self.grid[r][c], end=' ')      # prints a space or wall
            print()
        print()

    def moves(self):
        moves = []
        y = self.location[0]
        x = self.location[1]

        if y - 1 >= 0 and self.grid[y-1][x] == ' ':
            moves.append('U')

        if y + 1 < len(self.grid) and self.grid[y+1][x] == ' ':
            moves.append('D')

        if x - 1 >= 0 and self.grid[y][x-1] == ' ':
            moves.append('L')

        if x + 1 < len(self.grid) and self.grid[y][x+1] == ' ':
            moves.append('R')

        return moves
        

    def neighbor(self, move):
        y = self.location[0]
        x = self.location[1]

        if move == "U":
            newLocation = (y-1,x)

        if move == "D":
            newLocation = (y+1,x)

        if move == "L":
            newLocation = (y,x-1)

        if move == "R":
            newLocation = (y,x+1)
        

        return Maze(self.grid, newLocation)


class Agent():
    def bfs(self, maze, goal):
        frontier = deque([(maze.location, [])])
        visited = set()

        while frontier:
            (current, path) = frontier.popleft()
            # print(current,path)
            

            if current == goal:
                return path  
            
            visited.add(current)

            current_maze = Maze(maze.grid, current)
            for move in current_maze.moves():
                neighbor = current_maze.neighbor(move).location
                
                if neighbor not in visited:
                    frontier.append((neighbor, path + [move]))
                    visited.add(neighbor)  

        return None  

def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid,(1,1)) # start location
    maze.display()

    agent = Agent()
    goal = (19, 18)
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.50)
        maze.display()



if __name__ == '__main__':
    main()