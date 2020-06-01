
#Here are the dependencies (in this case Comma Seperated Values(CSV) and Operating System(OS))
import csv
import os


#Assign a variable to load file from a path 

file_to_load = os.path.join("Resources/election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize the Total vote counter to zero. This has to be done before the loop
total_votes = 0

#initialize a new empty dictionarylist candidate options
candidate_options = []

#Declare an empty dictionary
candidate_votes = {}

#Initialize all three winning counter variable to zer0
wnning_candidate = " "
winning_count = 0
winning_percentage = 0

#Open and read the election result file using with open () method

with open(file_to_load) as election_data:

#Now we can read the election data file with reader function

    file_reader = csv.reader(election_data)

#After reading the file we can print each row in the csv file

    headers = next(file_reader)
#    print(headers)


    for row in file_reader:
        total_votes = total_votes  +1

        candidate_name = row[2]  

      

#check to see if candidate's name does not match any existing name

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name) 

#Set each candidates vote count to 0
            candidate_votes[candidate_name] = 0


#increament candidates vote count by one
        candidate_votes[candidate_name] += 1

#Here we save the output of the result into a text file

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)

#Determine the percentage of vote looping through the counts

    for candidate in candidate_votes:

#Retrieve vote count of a candidate

        votes = candidate_votes[candidate]

        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({ votes:,})\n")

#        print(candidate_results)
        
#        txt_file.write(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

#        print(candidate_options)

#        print(f"{candidate}:{vote_percentage:,.1f}% ({votes:,})\n\n")

#Print the candidate name and percentage of votes
#        print(f"{candidate}: received {vote_percentage}% of the vote.\n")

#    print(candidate_options)


#Here we create a summary for the winner. The winning vote count and winning percentage

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)