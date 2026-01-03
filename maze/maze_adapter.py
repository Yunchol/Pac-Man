# maze/maze_adapter.py

from typing import List
from mazegenerator.mazegenerator import MazeGenerator


class MazeAdapter:
    """
    Adapter for the external A-Maze-ing MazeGenerator.
    Converts generated maze into a game-friendly grid.
    """

    WALL = 1
    PATH = 0

    def __init__(self, width: int, height: int, seed: int) -> None:
        self.width = width
        self.height = height
        self.seed = seed

        try:
            generator = MazeGenerator(
                size=(width, height),
                perfect=False,
                seed=seed,
            )
            generator.generate()
            self.grid = self._convert(generator.maze)
        except Exception as e:
            # 42必須：絶対に落ちない
            print(f"[MazeAdapter] Maze generation failed: {e}")
            self.grid = self._fallback_grid()

    def _convert(self, raw_maze) -> List[List[int]]:
        grid: List[List[int]] = []

        for row in raw_maze:
            grid_row: List[int] = []
            for cell in row:
                # 15 = 上下左右すべて壁 → 完全な壁
                if cell == 15:
                    grid_row.append(self.WALL)
                else:
                    grid_row.append(self.PATH)
            grid.append(grid_row)

        return grid


    def _fallback_grid(self) -> List[List[int]]:
        """
        Simple fallback maze used if generator fails.
        """
        grid: List[List[int]] = []

        for y in range(self.height):
            row: List[int] = []
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    row.append(self.WALL)
                else:
                    row.append(self.PATH)
            grid.append(row)

        return grid

    def is_wall(self, x: int, y: int) -> bool:
        return self.grid[y][x] == self.WALL
