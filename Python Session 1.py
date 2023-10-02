from statistics import mean

print("******** Session One **********")

def menu():
    while True:
        task = input('''
Select task:
[1] Task 1
[2] Task 2
[3] Task 3, 4 and 5
[4] Task 6
[5] Exit

''')
        if task == '1':
            print("What is your name?")
            name = input()
            print("Your name is", name + ". \n")



        elif task == '2':
            print("Enter a sentence, and we'll see how many characters are in it!")
            letters = input()
            print(len(letters), "\n")



        elif task == '3':
            height = input("Enter your height in centimetres: ")
            user_height_cm = int(height)
            print("Your height in centimeters is:", user_height_cm, "cm \n")

            height1 = input("Enter your first neighbours height in centimetres: ")
            neighbour1_height_cm = int(height1)

            height2 = input("\nEnter your second neighbours height in centimetres: ")
            neighbour2_height_cm = int(height2)

            heights = [user_height_cm, neighbour1_height_cm, neighbour2_height_cm]
            average = round(mean(heights), 2)
            inches = round(average / 2.54, 2)
            feet = round(inches / 12, 1)

            print("\nThe average height of you and your neighbours is: ", average, "cm")

            print("\nThe average height of you and your neighbours in inches is: ", inches, "inches")

            print("\nThe average height of you and your neighbours in feet is: ", feet, "feet")

            

        elif task == '4':
            heightFeet = input("How many feet tall are you? ")
            heightInches = input("And how many inches? ")
            user_height_feet = int(heightFeet)
            user_height_inches = int(heightInches)
            user_height = int(user_height_feet * 12) + int(user_height_inches)

            print("You are ", user_height, "inches tall")

            heightFeet1 = input("How many feet tall is neighbour 1? ")
            heightInches1 = input("And how many inches? ")
            user1_height_feet = int(heightFeet1)
            user1_height_inches = int(heightInches1)
            user1_height = int(user1_height_feet * 12) + int(user1_height_inches)

            heightFeet2 = input("How many feet tall is neighbour 2? ")
            heightInches2 = input("And how many inches? ")
            user2_height_feet = int(heightFeet2)
            user2_height_inches = int(heightInches2)
            user2_height = int(user2_height_feet * 12) + int(user2_height_inches)

            heightsInches = [user_height, user1_height, user2_height]
            average1 = round(mean(heightsInches), 2)
            convert = round((average1 / 12), 2)

            print("\nThe average height of you and your neighbours is: ", convert, "feet")



        elif task == '5':
            print("Student ID: 2207184")
            break

        else:
            print("Invalid choice. Please choose a numbered option between 1 & 5.")


menu()