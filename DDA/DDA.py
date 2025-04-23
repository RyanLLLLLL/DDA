from math import sin, cos, pi, sqrt

def normalize(vector):
	magnitude = sqrt(vector[0]**2 + vector[1]**2)
	vector = (vector[0]/magnitude, vector[1]/magnitude)
	return vector
	
def normalize_3D(vector):
	magnitude = sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
	vector = (vector[0]/magnitude, vector[1]/magnitude, vector[2]/magnitude)
	return vector
	
def get_first_intersect(grid, start_position, end_position):
	max_dist = (end_position[0]-start_position[0], end_position[1]-start_position[1])
	direction = normalize(max_dist)
	max_dist = sqrt(max_dist[0]**2 + max_dist[1]**2)
	if direction[0] == 0 or direction[1] == 0:
		direction = (direction[0]+0.00001, direction[1]+0.00001)
	step_size = (sqrt(1+(direction[1]/direction[0])**2), sqrt(1+(direction[0]/direction[1])**2))
	grid_w = len(grid) - 1
	grid_h = len(grid[0]) - 1
	
	x_ray_position = start_position
	x_ray_distance = 0
	y_ray_position = start_position
	y_ray_distance = 0
	current_ray = None
	
	if direction[0] > 0:
		x_multiplier = 1 - (start_position[0] % 1)
	else:
		x_multiplier = start_position[0] % 1
	if x_multiplier == 0: x_multiplier = 1
	x_ray_position = (x_ray_position[0] + (direction[0]*step_size[0]*x_multiplier), x_ray_position[1] + (direction[1]*step_size[0]*x_multiplier))
	x_ray_distance += step_size[0] * x_multiplier
	
	if direction[1] > 0:
		y_multiplier = 1 - (start_position[1] % 1)
	else:
		y_multiplier = start_position[1] % 1
	if y_multiplier == 0: y_multiplier = 1
	y_ray_position = (y_ray_position[0] + (direction[0]*step_size[1]*y_multiplier), y_ray_position[1] + (direction[1]*step_size[1]*y_multiplier))
	y_ray_distance += step_size[1] * y_multiplier
	
	if grid[int(start_position[0])][int(start_position[1])] != 0:
		return start_position, 0
	
	while True:
		if x_ray_distance < y_ray_distance:
			check_position = (x_ray_position[0], x_ray_position[1])
			current_ray = 'x'
		else:
			check_position = (y_ray_position[0], y_ray_position[1])
			current_ray = 'y'
			
		if current_ray == 'x':
			ray_pos = (int(x_ray_position[0]), int(x_ray_position[1]))
			outside_grid = ray_pos[0] < 0 or ray_pos[0] > grid_w or ray_pos[1] < 0 or ray_pos[1] > grid_h
			
			if x_ray_distance >= max_dist or outside_grid:
				return None, max_dist
		elif current_ray == 'y':
			ray_pos = (int(y_ray_position[0]), int(y_ray_position[1]))
			outside_grid = ray_pos[0] < 0 or ray_pos[0] > grid_w or ray_pos[1] < 0 or ray_pos[1] > grid_h
		
			if y_ray_distance >= max_dist or outside_grid:
				return None, max_dist
		if current_ray == 'x':
			if direction[0] > 0:
				check_position = (check_position[0]+0.1, check_position[1])
			else:
				check_position = (check_position[0]-0.1, check_position[1])
		elif current_ray == 'y':
			if direction[1] > 0:
				check_position = (check_position[0], check_position[1]+0.1)
			else:
				check_position = (check_position[0], check_position[1]-0.1)
			
		if grid[int(check_position[0])][int(check_position[1])] != 0:
			if current_ray == 'x':
				check_position = (int(check_position[0]), check_position[1])
				return check_position, x_ray_distance
			elif current_ray == 'y':
				check_position = (check_position[0], int(check_position[1]))
				return check_position, y_ray_distance

		if current_ray == 'x':
			x_ray_position = (x_ray_position[0] + direction[0]*step_size[0], x_ray_position[1] + direction[1]*step_size[0])
			x_ray_distance += step_size[0]
		elif current_ray == 'y':
			y_ray_position = (y_ray_position[0] + direction[0]*step_size[1], y_ray_position[1] + direction[1]*step_size[1])
			y_ray_distance += step_size[1]
			
def get_first_intersect_with_wrap(grid, start_position, end_position):
	max_dist = (end_position[0]-start_position[0], end_position[1]-start_position[1])
	direction = normalize(max_dist)
	max_dist = sqrt(max_dist[0]**2 + max_dist[1]**2)
	if direction[0] == 0 or direction[1] == 0:
		direction = (direction[0]+0.00001, direction[1]+0.00001)
	step_size = (sqrt(1+(direction[1]/direction[0])**2), sqrt(1+(direction[0]/direction[1])**2))
	grid_w = len(grid)
	grid_h = len(grid[0])
	
	x_ray_position = start_position
	x_ray_distance = 0
	y_ray_position = start_position
	y_ray_distance = 0
	current_ray = None
	
	if direction[0] > 0:
		x_multiplier = 1 - (start_position[0] % 1)
	else:
		x_multiplier = start_position[0] % 1
	if x_multiplier == 0: x_multiplier = 1
	x_ray_position = (x_ray_position[0] + (direction[0]*step_size[0]*x_multiplier), x_ray_position[1] + (direction[1]*step_size[0]*x_multiplier))
	x_ray_distance += step_size[0] * x_multiplier
	
	if direction[1] > 0:
		y_multiplier = 1 - (start_position[1] % 1)
	else:
		y_multiplier = start_position[1] % 1
	if y_multiplier == 0: y_multiplier = 1
	y_ray_position = (y_ray_position[0] + (direction[0]*step_size[1]*y_multiplier), y_ray_position[1] + (direction[1]*step_size[1]*y_multiplier))
	y_ray_distance += step_size[1] * y_multiplier
	
	if grid[int(start_position[0])][int(start_position[1])] != 0:
		return start_position, 0
	
	while True:
		if x_ray_distance < y_ray_distance:
			check_position = (x_ray_position[0], x_ray_position[1])
			current_ray = 'x'
		else:
			check_position = (y_ray_position[0], y_ray_position[1])
			current_ray = 'y'
			
		if current_ray == 'x':
			ray_pos = (int(x_ray_position[0]), int(x_ray_position[1]))
			if x_ray_distance >= max_dist:
				return None, max_dist
				
		elif current_ray == 'y':
			ray_pos = (int(y_ray_position[0]), int(y_ray_position[1]))
			if y_ray_distance >= max_dist:
				return None, max_dist
				
		if current_ray == 'x':
			if direction[0] > 0:
				check_position = (check_position[0]+0.1, check_position[1])
			else:
				check_position = (check_position[0]-0.1, check_position[1])
		elif current_ray == 'y':
			if direction[1] > 0:
				check_position = (check_position[0], check_position[1]+0.1)
			else:
				check_position = (check_position[0], check_position[1]-0.1)
			
		check_position = (check_position[0]%grid_w, check_position[1]%grid_h)
		if grid[int(check_position[0])][int(check_position[1])] != 0:
			if current_ray == 'x':
				check_position = (int(check_position[0]), check_position[1])
				return check_position, x_ray_distance
			elif current_ray == 'y':
				check_position = (check_position[0], int(check_position[1]))
				return check_position, y_ray_distance

		if current_ray == 'x':
			x_ray_position = (x_ray_position[0] + direction[0]*step_size[0], x_ray_position[1] + direction[1]*step_size[0])
			x_ray_distance += step_size[0]
		elif current_ray == 'y':
			y_ray_position = (y_ray_position[0] + direction[0]*step_size[1], y_ray_position[1] + direction[1]*step_size[1])
			y_ray_distance += step_size[1]
			
def get_first_intersect_3D(grid, start_position, end_position):
	max_dist = (end_position[0]-start_position[0], end_position[1]-start_position[1], end_position[2]-start_position[2])
	direction = normalize_3D(max_dist)
	max_dist = sqrt(max_dist[0]**2 + max_dist[1]**2 + max_dist[2]**2)
	if direction[0] == 0 or direction[1] == 0 or direction[2] == 0:
		direction = (direction[0]+0.00001, direction[1]+0.00001, direction[2]+0.00001)
	step_size = (1 / abs(direction[0]), 1 / abs(direction[1]), 1 / abs(direction[2]))
	
	grid_w = len(grid) - 1
	grid_h = len(grid[0]) - 1
	grid_d = len(grid[0][0]) - 1
	
	x_ray_position = start_position
	x_ray_distance = 0
	y_ray_position = start_position
	y_ray_distance = 0
	z_ray_position = start_position
	z_ray_distance = 0
	current_ray = None
	
	if direction[0] > 0:
		x_multiplier = 1 - (start_position[0] % 1)
	else:
		x_multiplier = start_position[0] % 1
	if x_multiplier == 0: x_multiplier = 1
	x_ray_position = (x_ray_position[0] + (direction[0]*step_size[0]*x_multiplier), x_ray_position[1] + (direction[1]*step_size[0]*x_multiplier), x_ray_position[2] + (direction[2]*step_size[0]*x_multiplier))
	x_ray_distance += step_size[0] * x_multiplier
	
	if direction[1] > 0:
		y_multiplier = 1 - (start_position[1] % 1)
	else:
		y_multiplier = start_position[1] % 1
	if y_multiplier == 0: y_multiplier = 1
	y_ray_position = (y_ray_position[0] + (direction[0]*step_size[1]*y_multiplier), y_ray_position[1] + (direction[1]*step_size[1]*y_multiplier), y_ray_position[2] + (direction[2]*step_size[1]*y_multiplier))
	y_ray_distance += step_size[1] * y_multiplier
	
	if direction[2] > 0:
		z_multiplier = 1 - (start_position[2] % 1)
	else:
		z_multiplier = start_position[2] % 1
	if z_multiplier == 0: z_multiplier = 1
	z_ray_position = (z_ray_position[0] + (direction[0]*step_size[2]*z_multiplier), z_ray_position[1] + (direction[1]*step_size[2]*z_multiplier), z_ray_position[2] + (direction[2]*step_size[2]*z_multiplier))
	z_ray_distance += step_size[2] * z_multiplier
	
	if grid[int(start_position[0])][int(start_position[1])][int(start_position[2])] != 0:
		return start_position, 0
	
	while True:
		if x_ray_distance < y_ray_distance and x_ray_distance < z_ray_distance:
			check_position = (x_ray_position[0], x_ray_position[1], x_ray_position[2])
			current_ray = 'x'
		elif y_ray_distance < z_ray_distance:
			check_position = (y_ray_position[0], y_ray_position[1], y_ray_position[2])
			current_ray = 'y'
		else:
			check_position = (z_ray_position[0], z_ray_position[1], z_ray_position[2])
			current_ray = 'z'
			
		if current_ray == 'x':
			ray_pos = (int(x_ray_position[0]), int(x_ray_position[1]), int(x_ray_position[2]))
			outside_grid = ray_pos[0] < 0 or ray_pos[0] > grid_w or ray_pos[1] < 0 or ray_pos[1] > grid_h or ray_pos[2] < 0 or ray_pos[2] > grid_d
			if x_ray_distance >= max_dist or outside_grid:
				return None, max_dist
				
		elif current_ray == 'y':
			ray_pos = (int(y_ray_position[0]), int(y_ray_position[1]), int(y_ray_position[2]))
			outside_grid = ray_pos[0] < 0 or ray_pos[0] > grid_w or ray_pos[1] < 0 or ray_pos[1] > grid_h or ray_pos[2] < 0 or ray_pos[2] > grid_d
			if y_ray_distance >= max_dist or outside_grid:
				return None, max_dist
				
		else:
			ray_pos = (int(z_ray_position[0]), int(z_ray_position[1]), int(z_ray_position[2]))
			outside_grid = ray_pos[0] < 0 or ray_pos[0] > grid_w or ray_pos[1] < 0 or ray_pos[1] > grid_h or ray_pos[2] < 0 or ray_pos[2] > grid_d
			if z_ray_distance >= max_dist or outside_grid:
				return None, max_dist
				
		if current_ray == 'x':
			if direction[0] > 0:
				check_position = (check_position[0]+0.1, check_position[1], check_position[2])
			else:
				check_position = (check_position[0]-0.1, check_position[1], check_position[2])
		elif current_ray == 'y':
			if direction[1] > 0:
				check_position = (check_position[0], check_position[1]+0.1, check_position[2])
			else:
				check_position = (check_position[0], check_position[1]-0.1, check_position[2])
		else:
			if direction[2] > 0:
				check_position = (check_position[0], check_position[1], check_position[2]+0.1)
			else:
				check_position = (check_position[0], check_position[1], check_position[2]-0.1)
			
		if grid[int(check_position[0])][int(check_position[1])][int(check_position[2])] != 0:
			if current_ray == 'x':
				check_position = (int(check_position[0]), check_position[1], check_position[2])
				return check_position, x_ray_distance
			elif current_ray == 'y':
				check_position = (check_position[0], int(check_position[1]), check_position[2])
				return check_position, y_ray_distance
			else:
				check_position = (check_position[0], check_position[1], int(check_position[2]))
				return check_position, z_ray_distance

		if current_ray == 'x':
			x_ray_position = (x_ray_position[0] + direction[0]*step_size[0], x_ray_position[1] + direction[1]*step_size[0], x_ray_position[2] + direction[2]*step_size[0])
			x_ray_distance += step_size[0]
		elif current_ray == 'y':
			y_ray_position = (y_ray_position[0] + direction[0]*step_size[1], y_ray_position[1] + direction[1]*step_size[1], y_ray_position[2] + direction[2]*step_size[1])
			y_ray_distance += step_size[1]
		else:
			z_ray_position = (z_ray_position[0] + direction[0]*step_size[2], z_ray_position[1] + direction[1]*step_size[2], z_ray_position[2] + direction[2]*step_size[2])
			z_ray_distance += step_size[2]
			
if __name__ == '__main__':
	map = []
	for x in range(4):
		layer = []
		for y in range(4):
			row = []
			for z in range(4):
				if x == 3 and y == 3 and z == 3 and False:
					row.append(1)
				else:
					row.append(0)
			layer.append(row)
		map.append(layer)
	print((get_first_intersect_3D(map, (0.5, 0.5, 0.5), (6, 6, 6))))
