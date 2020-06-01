
#Here are the dependencies (in this case Comma Seperated Values(CSV) and Operating System(OS))
import csv
import os


#Assign a variable to load the data file from a path. in this case file is located in Resources folder. 

file_to_load = os.path.join("Resources/election_results.csv")

#Assign a variable to save the output file (election_results.txt) in Analysis folder

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize or set the Total Election vote counter to zero. This has to be done before the loop

total_votes = 0

#initialize a new empty list for counties

county_options = []

#Declare an empty dictionary for the counties and vote key value pair

county_votes = {}

#Initialize all three winning counter variable to zer0
wnning_county = " "
winningVote_count = 0
winning_percentage = 0

#Open and read the election data file using with open () method

with open(file_to_load) as election_data:

#Now we can read the election data file with reader function

    file_reader = csv.reader(election_data)

#After reading the file we can print(if interested) each row in the csv file

    headers = next(file_reader)

#Here we inplement a For Loop to perform counts. In this loop we look at county and value pair. County at index 1
 
    for row in file_reader:
        total_votes = total_votes  +1

        county_name = row[1]  

#check to see if county name does not match any existing name

        if county_name not in county_options:

            county_options.append(county_name) 

#Set each candidates vote count to 0
            county_votes[county_name] = 0


#increament county vote count variable by one

        county_votes[county_name] += 1

#Here we save the output of the result into a text file using the "With open() method"

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")

    print(election_results, end="")

#At this point we write into a text file (election_result.txt)

    txt_file.write(election_results)

#Determine the percentage of vote looping through the counts

    for county_name in county_votes:

#Retrieve vote count of a candidate

        votes = county_votes[county_name]

        vote_percentage = float(votes) / float(total_votes) * 100
        
        countyVotes_results = (f"{county_name}: {vote_percentage:.1f}% ({ votes:,})\n")


        txt_file.write(countyVotes_results)

#We inplement aconditional if statement to check votes against winnig vote and winning percentage
        
        if (votes > winningVote_count) and (vote_percentage > winning_percentage):
            winningVote_count = votes
            winning_percentage = vote_percentage
            winning_county = county_name

        print(f"{county_name}:{vote_percentage:,.1f}% ({votes:,})\n")


#Here we create a summary of the outcome.The winning vote count and winning percentage for the winning county

    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winningVote_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_county_summary)

    print("Largest County Tournout:" + winning_county)

    txt_file.write(winning_county_summary)