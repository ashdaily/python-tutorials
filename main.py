from clear_csv_file import clear # from <file_name> import <function_name>


clear("example.csv")

# hire a clerk to feed all the student data
# write the file
for i in range(1000000000):
    name = input("Enter the name")
    age = input("Enter the age")
    gender = input("Enter the gender")

    with open("example.csv", "a") as csv_file: # open a file and make it equals to csv_file
        csv_file.write(f"{name}, {age}, {gender} \n") # concatenation using a formatted string
        csv_file.close()

# Find a better way to write the csv file
# How to improve this sofware
# list, dictionary, boolean, strings, int -> JSON

# Sofware name : Visual code studio


