"""
I am building a retrieval system. Given the following song lyric


{song}


You are tasked to produce a list of 8 emotions that I will later use to retrieve the song. 


Please provide only a list of comma-separated emotions.
"""


"""
We have a simple song retrieval system. It accepts eight emotions. You are tasked to suggest between 1 and 4 emotions to match the users' feelings. Suggest more emotions for longer sentences and just one or two for small ones, trying to condense the central theme of the input.


Examples:


Input: "I had a great day!" 

"Joy"

Input: "I am exhausted today and not feeling well."

"Exhaustion, Discomfort, and Fatigue"

Input: "I am in Love"

"Love"


Please, suggest emotions for input = "{user_input}", and reply ONLY with a list of emotions/feelings/vibes.
"""

user_input = "I am happy"

# We use chatGPT to get emotions from a user's input

emotions = chain.run(user_input=user_input)

# We find the k more similar song

matches = db.similarity_search_with_score(emotions, distance_metric="cos", k=k)