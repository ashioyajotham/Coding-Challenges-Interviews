import math
import csv

def find_correction_angle(binary_image):
	# Parsing the csv
	results = []
	with open(binary_image) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			results.append(row)
	
	# Dropping the column labels
	results = results[1:]
	# Converting strings to ints
	results = [[int(num) for num in result] for result in results]

	# Search for the first row of the square
	for i in range(len(results)):
		if 1 in (results[i]):
			top_y = i
			break

	# Finding the coordinate of the upper point
	top_x = results[top_y].index(1)
	#Finding the coordinate of the lower point that forms a Pythagorean triangle
	bottom_y = top_y + 5
	bottom_x = results[bottom_y].index(1)

	# Check if it's already rotated to prevent division by 0
	if bottom_x == top_x:
		return 0

	# Use tan relationship to find theta and cast to an int
	correction_angle = int(math.degrees(math.atan(5 / (bottom_x - top_x))))

	return correction_angle