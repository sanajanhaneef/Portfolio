#Function to find the average of a batsman
runs = float(input("Enter number of runs"))
bats = float(input("Enter total times batted"))
notout = float(input("Enter times not out"))
average = runs / (bats - notout)
print(average)