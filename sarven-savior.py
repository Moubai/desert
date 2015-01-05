# An ARRAY is a list of items.
# This array is a list of your friends' names.
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# Array indices start at 0, not 1!
friendIndex = 0

# Loop over each name in the array.
while friendIndex < len(friendNames):
    # Use square brackets to get a name from the array.
    friendName = friendNames[friendIndex]

    # Tell your friend to go home.
    # Use + to connect two strings.
    self.say(friendName + ', go home!')
    friendIndex +=1
    # Increment the index to get the next name from the array.
self.moveXY(28, 30)
self.buildXY("fence", 29, 30)
    
# Go back and build a fence to keep the ogres out.
