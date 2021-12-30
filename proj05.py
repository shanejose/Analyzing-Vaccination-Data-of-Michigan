####################################################################################################################################
#
# CSE 231
# Project 5
#
#   Algorithm
#
#       function open_file()
#           prompt an user input for reading the file
#           write a while loop with condition = True
#               do a try an except method which prompts for user input until it reads a text file
#               the condition for except method is FileNotFoundError 
#               break the loop if it finds a text file or else print the except prompt as directed by the project
#           return the text file
#
#       function fix_county_string(s)
#           assign the parameter to string
#           use if-elif statements based on the last index of the word to add letters to make a complete word "County
#               For ex: if s[-1] == "C" then add "ounty" to string s
#           return s
#
#       function find_min_max_column(fp,start,end)
#           call reset_file_pointer_to_beginning to start at the beginning of the file
#           set min_val = 105 and max_val = 0, convert them to float
#           skip the header line of the text file by using the method readline()
#           write a for loop to go through every line of the file
#               assign a value to variable "value" by slicing the line with "start" and "end"
#               use if-else statements to update min_val and max_val while going through the for loop
#               in the if-else statement when updating min_value and max_value create a variable str(min_county) and str(max_county)
#               Assign the county name to the str(min_county) and str(max_county) using the index values given from the project
#           return min_val,min_county,max_val,max_county
#
#       function display_min_max(s,min_val, min_county, max_val, max_county)
#           copy the print statements given from the project
#           format the print statements by inserting all the parameters
#           display the print statements
#
#       function all_vaccinated(fp)     
#           call reset_file_pointer_to_beginning to start at the beginning of the file
#           skip the header line of the text file by using the method readline()
#           create a variable called total
#           create a for loop to read every line of the text file 
#               assign total to line(86:101)
#               update the total by adding all the values from that column
#           print the value using the format statement given from the project
#           return total 
#
#
#       function main():
#           call the function open_file() to get the text file
#           then call the function display_options() to print all the prompts 
#           prompt the user for an option
#           create a  while loop with condition that if the user enters enters q then the program ends
#               assign the input to an integer value
#               create if-elif statements depending on the user input (1-4)
#                   assign start value and end value for index slicing based on user input
#                   call the function find_min_max_column(fp,start,end)
#                   assign str(s) directed by the project depending the user input
#                   call function display_min_max(s,min_val, min_county, max_val, max_county) to print out the results
#                   call the function display_options() to print all the prompts 
#                   then prompt the user for an option then go back to the start of the loop
#               if the user entered 5 call the function all_vaccinated(fp) and display_options() to get and print value
#                   call the function display_options() to print all the prompts 
#                   then prompt the user for an option then go back to the start of the loop
#               else statement should print invalid input and prompts the user for an option
#                   
#
###################################################################################################################################
def reset_file_pointer_to_beginning(fp):
    """
    DO NOT CHANGE
    Resets file pointer to the beginning and returns updated file pointer
    
    Parameters: file pointer object
    return: file pointer object
    """
    fp.seek(0)
    return fp

def open_file():
    ''' Insert Docstring'''
    file_name = input("Input a file for reading: ")
    check = True
    if file_name == "":
        filepointer = ""
        return filepointer
    while check == True:
        try:
            filepointer = open(file_name)
            break
        except FileNotFoundError:
            print("Invalid filename, please try again.")
            file_name = input("Input a file for reading: ")
            continue
    
    return filepointer

def fix_county_string(s):
    ''' Insert Docstring'''
    
    s = str(s)
    
    
    
    if s[-1] == "C":
        s += "ounty"
    elif s[-1] == "o":
        s += "unty"
    elif s[-1] == "u":
        s += "nty"
    elif s[-1] == "n":
        s += "ty"
    elif s[-1] == "t":
        s += "y"
    elif s [-1] == "":
        s += "County"
        
    return s

def find_min_max_column(fp,start,end):
    ''' Insert Docstring'''
    
    fp = reset_file_pointer_to_beginning(fp)
    
    min_val = 105
    min_val = float(min_val)
    max_val = 0
    max_val = float(max_val)
    min_county = ""
    max_county = ""
    fp.readline()
    for line in fp:
        
        
        value = line[start:end]
        value = float(value.strip())
        
        if value < min_val:
            min_val = value
            min_county = line[24:43]
            
        if value > max_val:
            max_val = value
            max_county = line[24:43]
    
    fix_county_string(min_county)
    fix_county_string(max_county)
   
    return min_val,min_county,max_val,max_county
        
   

def display_min_max(s,min_val, min_county, max_val, max_county):
    ''' Insert Docstring'''

        
    print("\nPercent vaccinated for {}".format(s))
    print("\n\t Minimum is in {} at {}%".format(min_county, min_val))
    print("\t Maximum is in {} at {}%".format(max_county, max_val))
        
    
        
    
 
def all_vaccinated(fp):
    
    fp = reset_file_pointer_to_beginning(fp)
    
    
    
    total = 0
    fp.readline()
    for line in fp:
        
        total += int(line[86:101])
    
    print("\nTotal vaccinated in Michigan: {:,d}".format(total))
    return total
        
        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Minimum and Maximum of all vaccinated
    2: Minimum and Maximum of those 12 and older
    3: Minimum and Maximum of those 18 and older
    4: Minimum and Maximum of those 65 and older
    5: Total vaccinated for Michigan
    q: quit\n"""
    print(OPTIONS)
 

def main():
    ''' Insert Docstring'''
    fp = open_file()
    display_options()
    answer = input("Select and option, q to quit: ")
    
    while answer != "q" and answer != "":
        if answer.isdigit():
            answer = int(answer)
            
            if 1<=answer<=5:
                
                if answer == 1:
                    start = 71
                    end = 86
                    n = find_min_max_column(fp, start, end)
                    s = "all"
                    display_min_max(s,n[0], n[1], n[2], n[3])
                    display_options()
                    answer = input("Select and option, q to quit: ")
                    continue
                    
                elif answer == 2:
                    start = 136
                    end = 150
                    n = find_min_max_column(fp, start, end)
                    s = "age 12 and older"
                    display_min_max(s,n[0], n[1], n[2], n[3])
                    display_options()
                    answer = input("Select and option, q to quit: ")
                    continue
                
                elif answer == 3:
                    start = 183
                    end = 200
                    n = find_min_max_column(fp, start, end)
                    s = "age 18 and older"
                    display_min_max(s,n[0], n[1], n[2], n[3])
                    display_options()
                    answer = input("Select and option, q to quit: ")
                    continue
                
                elif answer == 4:
                    start = 230
                    end = 234
                    n = find_min_max_column(fp, start, end)
                    s = "age 65 and older"
                    display_min_max(s,n[0], n[1], n[2], n[3])
                    display_options()
                    answer = input("Select and option, q to quit: ")
                    continue
                
                elif answer == 5:
                    all_vaccinated(fp)
                    display_options()
                    answer = input("Select and option, q to quit: ")
                    continue
                
                else:
                    print("Invalid option; please try again.")
                    answer = input("Select and option, q to quit: ")
                    continue
                          
        print("Invalid option; please try again.")
        answer = input("Select and option, q to quit: ")
    
    
        
    
    
    
    
        
    
    
    
        
   
    
    
    

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.         
if __name__ == "__main__":
    main()
