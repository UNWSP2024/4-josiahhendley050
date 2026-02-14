# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.
# Program #5: Bank Balance
# Josiah Hendley
# 2/13/26
# Bank Balance

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         # initialize for while loop
    total = 0.0

    # ---------------------------------------------
    # PSEUDOCODE: Budget Analysis / Bank Balance
    # ---------------------------------------------
    # START
    #
    # Display "Enter the amount budgeted for the month:"
    # Input budget
    #
    # Set total_expenses = 0
    #
    # Display "Enter your expenses for the month."
    # Display "Enter 0 when you are finished."
    #
    # Input expense
    #
    # WHILE expense is not equal to 0
    #       total_expenses = total_expenses + expense
    #       Input next expense
    # END WHILE
    #
    # Set difference = budget - total_expenses
    #
    # IF difference > 0 THEN
    #       Display "You are under budget by", difference
    # ELSE IF difference < 0 THEN
    #       Display "You are over budget by", absolute value of difference
    # ELSE
    #       Display "You spent exactly your budget."
    # END IF
    #
    # END
    # ---------------------------------------------

    # Python Program Starts Here

    budget = float(input("Enter the amount budgeted for the month: "))

    total_expenses = 0

    print("Enter your expenses for the month.")
    print("Enter 0 when you are finished.")

    expense = float(input("Enter an expense: "))

    while expense != 0:
        total_expenses += expense
        expense = float(input("Enter an expense: "))

    difference = budget - total_expenses

    print("\nTotal expenses:", total_expenses)

    if difference > 0:
        print("You are under budget by $", difference)
    elif difference < 0:
        print("You are over budget by $", abs(difference))
    else:
        print("You spent exactly your budget.")

if __name__ == '__main__':
    main()


