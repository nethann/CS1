"""
This is a comment block. Any text written inbetween the set of 3 double quotes
is ignored by python when the program is run! Comments are super useful for
explaining what your program does to anyone who reads it. In order to run this 
program, click the play button at the top right of this window.

^ You may delete the instructions above this line ^

Program Description:
This program asks the user to enter their name and prints a welcome message to 
the user that run this program. The welcome message includes the time and day 
of the class lectures and this current lab session.

Author: [Thinisha Nethan Nagendran]
"""

# This is an inline comment. Only text on this line is ignored.
# Inline comments always start with # symbol
# These are used to explain individual lines of code
# ^ You may delete these instructions ^

#variables
lecture_start_time = "11:00am"
lecture_start_days = "Monday & Wednesday"

lab_start_time = "11:00am"
lab_start_day = "Tuesday"


#input & print
user_name = str(input("What is your name? "))
print(f'Hello {user_name}!\nWelcome to the CSCS/DSCI 1301 Principles of Computer/Data Science Course!\nOur class is held every {lecture_start_days} at {lecture_start_time}\nOur lab session is held every {lab_start_day} on {lab_start_time}')


