from Utilities import (
    datetime_menu,
    math_menu,
    random_menu,
    uuid_menu,
    file_menu,
    explore_module
)


def main():

    while True:

        print("===================================")
        print("Welcome To Multi-Utility Toolkit")
        print("===================================")

        print("""
========================================
          Choose an option
========================================

1. DateTime and Time Operation
2. Mathematical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UID)
5. File Operation (Custom Module)
6. Explore Module Attribute (dir())
7. Exit

========================================
""")

        try:

            user = int(input("Enter your Choice Here... "))

        except ValueError:

            print("Please enter a valid number.")

            continue

        if user == 1:

            datetime_menu()

        elif user == 2:

            math_menu()

        elif user == 3:

            random_menu()

        elif user == 4:

            uuid_menu()

        elif user == 5:

            file_menu()

        elif user == 6:

            explore_module()

        elif user == 7:

            print("""
            ============================================
            Thank you for using the Multi-Utility Toolkit!
            ============================================
            """)
            break

        else:

            print("Invalid Input. Please check choice again.")
        input("""
.............................................................................
    Press Enter RE-ENTER into the Program---(Multi-Utility Toolkit!)---
.............................................................................
        """)


if __name__ == "__main__":
    main()