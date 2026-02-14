# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.
#Josiah Hendley
#2/13/26
# Movie

def main():

num_movies = int(input("How many movies do you want to enter? "))

total_tickets = 0
count = 1

while count <= num_movies:
    movie = input("Enter the movie name: ")
    tickets = int(input("How many tickets for this movie? "))
    
    total_tickets += tickets
    count += 1

print("Total number of tickets desired:", total_tickets)

if __name__ == '__main__':
    main()
