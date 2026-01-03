#迷路生成のライブラリの確認用フォルダ

from mazegenerator.mazegenerator import MazeGenerator

gen = MazeGenerator(seed=42)
maze = gen.generate()

print(maze)
