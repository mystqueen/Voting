nominees = {
    "Rose":0,
    "Patrick":2, 
    "Bright":4, 
    "Mike":1, 
    "Archimedes":0
    }

def vote():
    
    print("Who would you like to vote for: ")
    counts = 1
    for nomineeToVoteFor in nominees.keys():
        print(f"{counts}. {nomineeToVoteFor}")
        counts +1

    userInput = int(input())

    if userInput == "1":
        nominees["Rose"] +=1
    elif userInput == "2":
        nominees["Patrick"] +=1
    elif userInput == "3":
        nominees["Bright"] +=1
    elif userInput == "4":
        nominees["Mike"] +=1
    elif userInput == "5":
        nominees["Archimedes"] +=1

    keysOfNominees = list(nominees.keys())
    print(f"Thank You! You have voted for {keysOfNominees[userInput-1]}")

def viewVotes():
    for nomineeToVoteFor in nominees.keys():
        print(f"{nomineeToVoteFor}: {nominees[nomineeToVoteFor]} votes")

if __name__ == "__main__":
     print("Welcome To ESA Awards")
userInput = int(input("1.Vote \n2.View votes \n3.Exit \n"))
if userInput == 1:
        vote()
elif userInput == 2:
        viewVotes()
elif userInput == 3:
        End
else:
        print("Invalid Input.")
    
        
        
    


        


