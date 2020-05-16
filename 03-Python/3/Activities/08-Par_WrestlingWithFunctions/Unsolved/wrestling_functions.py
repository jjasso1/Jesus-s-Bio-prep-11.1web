import os
import csv

# @TODO Path to collect data from the Resources folder


# @TODO Define a function called print_percentages and have it accept the 'wrestler_data' as its sole parameter
# 'wrestler_data' being a list containing data for a single wrestler

    # Implement the following steps (that say TODO) for each wrestler inside the print_percentages function

    # @TODO Find the total number of matches wrestled by this wrestler
    
    # @TODO Find the percentage of matches won
    
    # @TODO Find the percentage of matches lost
    
    # @TODO Find the percentage of matches drawn
    
    # @TODO Print out the wrestler's name and their percentage stats
    
    
# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")


    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
