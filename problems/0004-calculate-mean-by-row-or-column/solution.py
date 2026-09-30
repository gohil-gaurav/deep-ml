def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	if mode not in ['row', 'column']:
		return []

	rows, columns = len(matrix), len(matrix[0])
	means = []

	if mode == 'row':
		for r in range(rows):
			mean = 0
			for c in range(columns):
				mean += matrix[r][c]
			mean /= columns
			means.append(mean)
	else:
		for c in range(columns):
			mean = 0
			for r in range(rows):
				mean += matrix[r][c]
			mean /= rows
			means.append(mean)
	return means