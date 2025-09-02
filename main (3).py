
'''
Author: Ethan Smith
Description: Fitness Tracker 
Date: 25/8/25
Version: 1.1
'''

# ----------- main routine -----------
if __name__ == "__main__":

    # ask for name and age
    name = input("Hello, what is your name? ")
    while True:
        try:
            age = int(input("What is your age? "))
            break
        except ValueError:
            print("Please enter a valid number for your age.")

    print("Welcome", name + "!", "Let's track your fitness results.")

    # collect 5 workout results
    results = []

    for i in range(5):
        while True:
            try:
                result = int(input(f"Enter workout result #{i+1} (minutes, between 10 and 60): "))
                if result < 10 or result > 60:
                    print("That’s not in the valid range (10–60). Try again.")
                else:
                    results.append(result)
                    break
            except ValueError:
                print("That’s not a number. Please enter a number between 10 and 60.")

    # print results
    print("\n--- Results ---")
    print("All results:", results)

    # calculate average
    average = sum(results) / len(results)
    print("Average time:", round(average, 2), "minutes")

    # best (fastest) result
    best = min(results)
    print("Best (fastest) time:", best, "minutes")

    # personalised message
    if best <= 15:
        print("Amazing work,", name + "! You are super fast!")
    elif average <= 30:
        print("Nice job,", name + "! You are doing really well, keep it up!")
    else:
        print("Good effort,", name + ". Keep training and you'll improve!")