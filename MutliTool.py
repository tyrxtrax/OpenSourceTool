import os
import sys
import requests
import base64
import base64
import random
import string

def banner():
    print("""
    ============================
    MultiTool for Hackers (Discord Edition)
    ============================
    """)

def option_1():
    print("Option 1: Generate a random Discord webhook URL (for testing purposes).")
    print("Webhook URL: https://discord.com/api/webhooks/<random_id>/<random_token>")

def option_2():
    print("Option 2: Send a test message to a Discord webhook.")
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message to send: ")
    response = requests.post(webhook_url, json={"content": message})
    print(f"Response: {response.status_code}")

def option_3():
    print("Option 3: Extract user IDs from a Discord message.")
    message = input("Enter the Discord message: ")
    user_ids = [word for word in message.split() if word.isdigit()]
    print("Extracted User IDs:", user_ids)

def option_4():
    print("Option 4: Encode a message in Base64.")
    message = input("Enter the message to encode: ")
    encoded = base64.b64encode(message.encode()).decode()
    print("Encoded Message:", encoded)

def option_5():
    print("Option 5: Decode a Base64 message.")
    encoded_message = input("Enter the Base64 encoded message: ")
    decoded = base64.b64decode(encoded_message.encode()).decode()
    print("Decoded Message:", decoded)

def option_6():
    print("Option 6: Check if a Discord invite link is valid.")
    invite = input("Enter the Discord invite link: ")
    response = requests.get(f"https://discord.com/api/v9/invites/{invite.split('/')[-1]}")
    if response.status_code == 200:
        print("Invite is valid.")
    else:
        print("Invite is invalid or expired.")

def option_7():
    print("Option 7: Generate a random password.")
    length = int(input("Enter the password length: "))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print("Generated Password:", password)

def option_8():
    print("Option 8: Fetch Discord server information (requires bot token).")
    token = input("Enter your bot token: ")
    guild_id = input("Enter the server (guild) ID: ")
    headers = {"Authorization": f"Bot {token}"}
    response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}", headers=headers)
    if response.status_code == 200:
        print("Server Info:", response.json())
    else:
        print("Failed to fetch server info. Check your token and guild ID.")

def option_9():
    print("Option 9: Ping a server to check connectivity.")
    server = input("Enter the server address (e.g., discord.com): ")
    response = os.system(f"ping -c 1 {server}" if os.name != 'nt' else f"ping {server}")
    if response == 0:
        print(f"Server {server} is reachable.")
    else:
        print(f"Server {server} is not reachable.")

def option_10():
    print("Option 10: Exit the tool.")
    sys.exit("Exiting the MultiTool. Goodbye!")

def main():
    banner()
    while True:
        print("""
        1. Generate random Discord webhook URL
        2. Send a test message to a Discord webhook
        3. Extract user IDs from a Discord message
        4. Encode a message in Base64
        5. Decode a Base64 message
        6. Check if a Discord invite link is valid
        7. Generate a random password
        8. Fetch Discord server information
        9. Ping a server to check connectivity
        10. Exit
        """)
        choice = input("Select an option (1-10): ")
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "6":
            option_6()
        elif choice == "7":
            option_7()
        elif choice == "8":
            option_8()
        elif choice == "9":
            option_9()
        elif choice == "10":
            option_10()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()