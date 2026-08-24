# ============================================================
# INKYSHAMAN IT TOOLKIT
# main.py
#
# This is the main controller of the application.
#
# main.py is responsible for:
#   1. Importing functionality from other modules
#   2. Displaying information to the user
#   3. Showing the main menu
#   4. Receiving user input
#   5. Deciding what the program should do
#   6. Keeping the application running
# ============================================================


# ============================================================
# IMPORTS
# ============================================================
# TYPE: Module imports
#
# An import allows this file to use code that exists in another
# Python file.
#
# We are importing functions from system_info.py and
# network_info.py instead of putting all of the code into
# main.py.
#
# This is part of SOFTWARE ENGINEERING:
# "Separation of Responsibilities"
# ============================================================

from system_info import get_system_info

from network_info import (
    get_network_info,
    get_external_ip,
    test_internet_connection
)


# ============================================================
# FUNCTION: show_system_info()
# ============================================================
# TYPE: Function
#
# PURPOSE:
# This function gets the system information from
# system_info.py and displays it to the user.
#
# Notice that this function does NOT collect the information
# itself.
#
# get_system_info() handles the data collection.
# show_system_info() handles displaying it.
#
# This separation makes the program easier to maintain.
# ============================================================

def show_system_info():

    # --------------------------------------------------------
    # FUNCTION CALL + VARIABLE
    # --------------------------------------------------------
    # get_system_info() calls the function we imported from
    # system_info.py.
    #
    # The information returned by that function is stored
    # inside a variable called "info".
    #
    # TYPE:
    #   Variable
    #
    # The actual data inside "info" is a dictionary.
    # --------------------------------------------------------

    info = get_system_info()


    # --------------------------------------------------------
    # OUTPUT
    # --------------------------------------------------------
    # print() is a built-in Python function used to display
    # information in the terminal.
    #
    # "\n" creates a blank line before the text.
    # --------------------------------------------------------

    print("\n========================================")
    print("          SYSTEM INFORMATION")
    print("========================================")


    # --------------------------------------------------------
    # FOR LOOP + DICTIONARY ITERATION
    # --------------------------------------------------------
    # TYPE:
    #   for loop
    #   dictionary
    #   iteration
    #
    # info is a dictionary.
    #
    # .items() gives us both the KEY and VALUE from each
    # dictionary entry.
    #
    # Example:
    #
    # "RAM": "32.00 GB"
    #
    # key   = "RAM"
    # value = "32.00 GB"
    #
    # The loop processes each item in the dictionary.
    # --------------------------------------------------------

    for key, value in info.items():

        # ----------------------------------------------------
        # f-string
        # ----------------------------------------------------
        # TYPE:
        #   Formatted String
    #
        # The f before the quotation marks allows us to insert
        # variables directly into the string.
        #
        # {key} is replaced with the actual dictionary key.
        # {value} is replaced with the actual dictionary value.
        #
        # Example:
        #
        # Computer Name: INKY-PC
        # RAM: 32.00 GB
        # ----------------------------------------------------

        print(f"{key}: {value}")


    # --------------------------------------------------------
    # OUTPUT
    # --------------------------------------------------------
    # Displays a closing line to make the output easier to read.
    # --------------------------------------------------------

    print("========================================")


# ============================================================
# FUNCTION: show_network_info()
# ============================================================
# TYPE: Function
#
# PURPOSE:
# This function collects and displays network information.
#
# The actual networking functionality lives in network_info.py.
#
# main.py controls WHEN it is displayed.
# ============================================================

def show_network_info():

    # --------------------------------------------------------
    # VARIABLES
    # --------------------------------------------------------
    # get_network_info() returns a dictionary containing things
    # such as:
    #
    # Hostname
    # Local IP
    #
    # That dictionary is stored in "network".
    # --------------------------------------------------------

    network = get_network_info()


    # --------------------------------------------------------
    # VARIABLE
    # --------------------------------------------------------
    # get_external_ip() returns the computer/network's public
    # IP address.
    #
    # We store that value in "external_ip".
    # --------------------------------------------------------

    external_ip = get_external_ip()


    # --------------------------------------------------------
    # OUTPUT
    # --------------------------------------------------------

    print("\n========================================")
    print("          NETWORK DIAGNOSTICS")
    print("========================================")


    # --------------------------------------------------------
    # FOR LOOP + DICTIONARY
    # --------------------------------------------------------
    # We iterate through the network dictionary just like we
    # did with the system information dictionary.
    # --------------------------------------------------------

    for key, value in network.items():
        print(f"{key}: {value}")


    # --------------------------------------------------------
    # F-STRING + VARIABLE
    # --------------------------------------------------------
    # Displays the external/public IP address.
    # --------------------------------------------------------

    print(f"External IP: {external_ip}")


    # ========================================================
    # CONDITIONAL STATEMENT
    # ========================================================
    # TYPE:
    #   if / else
    #   conditional logic
    #
    # test_internet_connection() returns either:
    #
    # True
    #
    # or
    #
    # False
    #
    # If the result is True, we display "Connected".
    # Otherwise, we display "Offline".
    # ========================================================

    if test_internet_connection():
        print("Internet: Connected")

    else:
        print("Internet: Offline")


    print("========================================")


# ============================================================
# FUNCTION: main()
# ============================================================
# TYPE:
#   Function
#
# PURPOSE:
# This is the MAIN CONTROL FUNCTION of the application.
#
# It controls the program's menu and determines which feature
# the user wants to run.
#
# Think of main() as the control center of the application.
# ============================================================

def main():

    # ========================================================
    # WHILE LOOP
    # ========================================================
    # TYPE:
    #   Loop
#
    # while True means:
    #
    # "Keep running this block of code."
    #
    # The program will continue showing the menu until we
    # explicitly stop the loop using "break".
    #
    # This is what allows the user to run multiple tools
    # without restarting the program.
    # ========================================================

    while True:

        # ----------------------------------------------------
        # APPLICATION HEADER
        # ----------------------------------------------------
        # TYPE:
        #   Output
        #
        # This displays the title of the program.
        # ----------------------------------------------------

        print("\n========================================")
        print("       INKYSHAMAN IT TOOLKIT")
        print("              v1.0")
        print("========================================")


        # ----------------------------------------------------
        # MENU OPTIONS
        # ----------------------------------------------------
        # TYPE:
        #   Output
        #
        # These are the options the user can choose.
        # ----------------------------------------------------

        print()
        print("1. System Information")
        print("2. Network Diagnostics")
        print("3. Exit")
        print()


        # ====================================================
        # USER INPUT
        # ====================================================
        # TYPE:
        #   Input
        #   Variable
# 
        # input() pauses the program and waits for the user
        # to type something.
        #
        # IMPORTANT:
        # input() ALWAYS returns text (a string).
        #
        # So if the user enters:
        #
        # 1
        #
        # Python actually receives:
        #
        # "1"
        #
        # That's why later we compare choice to "1" instead
        # of the number 1.
        # ====================================================

        choice = input("Select an option: ")


        # ====================================================
        # CONDITIONAL LOGIC
        # ====================================================
        # TYPE:
        #   if statement
        #
        # We use the user's choice to determine what the
        # program should do.
        # ====================================================

        if choice == "1":

            # ------------------------------------------------
            # FUNCTION CALL
            # ------------------------------------------------
            # Run the system information tool.
            # ------------------------------------------------

            show_system_info()


            # ------------------------------------------------
            # USER INPUT / PAUSE
            # ------------------------------------------------
            # This pauses the program after displaying the
            # information.
            #
            # The user presses Enter when they're ready to
            # return to the main menu.
            # ------------------------------------------------

            input("\nPress Enter to return to the menu...")


        # ====================================================
        # ELIF
        # ====================================================
        # TYPE:
        #   Conditional statement
        #
        # elif means:
        #
        # "If the previous condition wasn't true, check this
        # condition."
        # ====================================================

        elif choice == "2":

            # ------------------------------------------------
            # FUNCTION CALL
            # ------------------------------------------------
            # Run the network diagnostic tool.
            # ------------------------------------------------

            show_network_info()


            # ------------------------------------------------
            # USER INPUT / PAUSE
            # ------------------------------------------------

            input("\nPress Enter to return to the menu...")


        # ====================================================
        # EXIT CONDITION
        # ====================================================
        # If the user chooses option 3, we stop the while loop.
        # ====================================================

        elif choice == "3":

            print("\nExiting InkyShaman IT Toolkit...")


            # ------------------------------------------------
            # BREAK
            # ------------------------------------------------
            # TYPE:
            #   Loop control statement
            #
            # break immediately stops the current loop.
            #
            # Since this is our while True loop, break is what
            # allows the user to actually exit the program.
            # ------------------------------------------------

            break


        # ====================================================
        # ELSE
        # ====================================================
        # TYPE:
        #   Conditional statement
        #
        # If the user enters something other than:
        #
        # "1"
        # "2"
        # "3"
        #
        # the program reaches this block.
        # ====================================================

        else:

            print("\nInvalid option. Please try again.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# TYPE:
#   Conditional
#   Special Python variable
#
# __name__ is a special Python variable.
#
# When Python runs this file directly:
#
#     python src\main.py
#
# Python sets:
#
#     __name__ = "__main__"
#
# Therefore, this condition becomes True and main() runs.
#
# This is a very common Python programming pattern.
#
# It also prevents main() from automatically running if another
# Python file imports main.py.
# ============================================================

if __name__ == "__main__":
    main()