#Make sure you pass your own gam_path
import colorama
from colorama import Fore, Style
import subprocess

# Initialize colorama
colorama.init()

def generate_gam_command(account_to_delegate, delegate_to):
    gam_path = "/Users/a.mishra/bin/gam/gam"
    command = f"{gam_path} user {account_to_delegate} add delegate {delegate_to}"
    subprocess.run(command, shell=True, check=True)
    return command

def generate_gam_remove_command(account_to_remove,delete_from):
    gam_path = "/Users/a.mishra/bin/gam/gam"
    command = f"{gam_path} user {account_to_remove} delete delegate {delete_from}"
    subprocess.run(command, shell=True, check=True)
    return command

# Function to display colored output
def print_colorful(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

# Display options
print_colorful("Select an option:", Fore.CYAN)
print("1. Delegate")
print("2. Remove Delegation")

option = input("Enter your choice (1/2): ")

# Delegate option
if option == "1":
    print_colorful("\nDelegate selected", Fore.GREEN)
    account_to_delegate = input("Enter the account to delegate: ")
    delegate_to = input("Enter the account to delegate to: ")

    #Input Validation
    if(account_to_delegate and delegate_to.endswith('@lufa.com')):
        command = generate_gam_command(account_to_delegate, delegate_to)
        print(command)

    else:
        print_colorful("\nInvalid input!", Fore.RED)
        

    # Generate command
    

# Remove delegation option
elif option == "2":
    print_colorful("\nRemove Delegation selected", Fore.GREEN)
    account_to_remove = input("Enter the account to remove Delegation: ")
    delete_from=input("Enter the account to remove delegation from: ")

    #Input Validation
    if(account_to_remove and delete_from.endswith("@lufa.com")):
        command = generate_gam_remove_command(account_to_remove,delete_from)
        print(command)
    else:
        print_colorful("\nInvalid input!", Fore.RED)


    # Generate command
    
    
    

else:
    print_colorful("\nInvalid option selected!", Fore.RED)
