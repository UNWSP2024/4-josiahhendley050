# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.
#Josiah Hendley
#2/13/26
#Rainfall Program

def main():
years = int(input("Enter the number of years: "))

total_rainfall = 0
total_months = years * 12

for year in range(1, years + 1):
    print("Year", year)
    
    for month in range(1, 12 + 1):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months

print("\nNumber of months:", total_months)
print("Total inches of rainfall:", total_rainfall)
print("Average rainfall per month:", average_rainfall)
  


if __name__ == '__main__':
    main()
