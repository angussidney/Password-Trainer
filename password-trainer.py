"""
Password Trainer v1.0
Copyright (c) 2016 angussidney
Released under the MIT license

This program helps you remember long, complicated, (and most importantly) secure passwords.

Code review by Josay [http://codereview.stackexchange.com/users/9452/josay] from Code Review StackExchange
http://codereview.stackexchange.com/a/119076/81838
"""

import os

PASSWORD = "password123" # Insert your password here 
MAXIMUM_TRIES = 3 # The maximum number of attempts before the program stops annoying the user.

def main():
    """Prompts the user for their password and provides feedback."""
    for try_index in range(MAXIMUM_TRIES):
        password_attempt = raw_input("Please type your password: ")
        print
        if password_attempt == PASSWORD:
            print "You entered your password correctly."
            break # Skips directly to end of session
        else:
            print "Your attempt was incorrect.\n"
            print_differences(password_attempt)
            raw_input("\nPress any key to continue...")
            clear_screen()
    print "\nPassword training is complete for this session."
    raw_input("Press any key to continue...")

def clear_screen():
    """Clears the screen for a new password attempt."""
    os.system("cls" if os.name=="nt" else "clear")

def print_differences(attempt):
    """Prints the differences between the password attempt and the real password.
    Raises an error if the attempt is of the wrong length.

    Keyword arguments:
    attempt -- the password attempt
    
    Example output:
    Correct password: password123
    
    Your attempt:     passwood124
    Errors:                 x   x
    Corrections:            r   3
    """
    if len(attempt) != len(PASSWORD):
        print "Your password attempt was of the wrong length."
        print "Your attempt should have been %s characters long." % str(len(PASSWORD))
        print "No password accuracy breakdown available."
    else:
        print "Correct password: %s\n" % PASSWORD
        print "Your attempt:     %s" % attempt
        errors = "".join(" " if a == p else "x" for p, a in zip(PASSWORD, attempt))
        print "Errors:           %s" % errors
        corrections = "".join(" " if a == p else p for p, a in zip(PASSWORD, attempt))
        print "Corrections:      %s" % corrections

if __name__ == "__main__":
    main()
