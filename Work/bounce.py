# bounce.py
#
# Exercise 1.5
start_height = 100.0
bounce_height = 0
counter = 1

while counter <= 10:
	bounce_height = ((start_height /5) * 3)
	print(counter ,' : ', bounce_height, ' meters')
	start_height = bounce_height
	counter = counter + 1
