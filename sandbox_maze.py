#迷路生成のライブラリの確認用フォルダ

from mazegenerator.mazegenerator import MazeGenerator

gen = MazeGenerator(size=(10, 10), perfect=False, seed=42)
gen.generate()

for row in gen.maze:
    print(row)
