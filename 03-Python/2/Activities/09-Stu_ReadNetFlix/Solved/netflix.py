# Modules
import os
import csv

# import modules
# define path of the file to read, file_path
# open the csv file
# user input -> movie_title
# csv.reader to get a handle on the file (iterator -> iterate over the rows) -> csvreader
# skip the header row (next(csvreader))
# for loop to iterate over csvreader (data rows excluding the header)
    # compare movie_title to the title in the current row, row[0], if match
        # print the title, ratings from each row

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
movie_found = False

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # # BONUS: Set variable to confirm we have found the video
            movie_found = True

            # # BONUS: Stop at first results to avoid duplicates
            break

# # If the video is never found, alert the user
if not movie_found:
    print("Sorry about this, we don't seem to have what you are looking for!")
