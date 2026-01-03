# ui/ascii_renderer.py

class AsciiMazeRenderer:
    WALL_CHAR = "#"
    PATH_CHAR = " "

    def render(self, grid):
        for row in grid:
            line = ""
            for cell in row:
                if cell == 1:  # WALL
                    line += "###"
                else:          # PATH
                    line += "   "
            print(line)
