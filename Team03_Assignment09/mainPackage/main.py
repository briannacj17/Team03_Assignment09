#main.py
# Name: Team03
# Assignment Number: Assignment 09
# Due Date: 4-04-2024
# Course/Section:IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Research API's and extract interesting data
# Citations: https://restcountries.com/

from utilsPackage.restCountriesAPI import *

if __name__ == "__main__":
    while True:
        print("Press 1 to start querying:")
        print("q. Quit")

        choice = input("\n Enter your choice:")

        if choice == '1':
            REST_Countries()  # Will prompt for countryInput
        if choice.lower() == 'q':
            print("Exiting the program...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please choose again.")


    
    
    