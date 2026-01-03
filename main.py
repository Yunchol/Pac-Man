# main.py（テスト用）

from maze.maze_adapter import MazeAdapter
from ui.ascii_renderer import AsciiMazeRenderer


def main() -> None:
    maze = MazeAdapter(width=15, height=15, seed=1)
    renderer = AsciiMazeRenderer()
    renderer.render(maze.grid)


if __name__ == "__main__":
    main()
