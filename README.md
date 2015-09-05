# Idea
Save the 25 most upvoted submissions of the day to a csv 
file with the columns: submission name, number of upvotes,

The file main.py is run every 24 hours and the results are saved to a postgres database, storing
just the submission title and score.

# Goal
In the long term, the goal is to be able to data mine the top submissions every day for
frequent patterns. The hypothesis is that some combinations of words are more likely to be 
recieve a higher score. This could be mined using frequent pattern mining techniques such as apriori.
