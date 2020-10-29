from collections import deque

def search(lines, pattern, history=5):
	# deque会自动剔除大于maxlen时左边的数据
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
	with open(r'/data/code/test.txt') as f:
		for line, prevlines in search(f, '5', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-' * 20)
