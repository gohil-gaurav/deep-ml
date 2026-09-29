import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	
	rows, cols = len(a), len(a[0])
	new_rows, new_cols = new_shape
	if rows*cols != new_rows*new_cols:
		return []

	flat_matrix = []
	for r in range(rows):
		for c in range(cols):
			flat_matrix.append(a[r][c])

	reshaped_matrix = []
	index = 0
	for nr in range(new_rows):
		new_rows = []
		for nc in range(new_cols):
			new_rows.append(flat_matrix[index])
			index += 1
		reshaped_matrix.append(new_rows)

	return reshaped_matrix