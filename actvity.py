print("=== Python Shutdown Utility ===")
print("This will shut down your computer.")
print("Make sure you have saved all your work.\n")

confirm = input("Do you really want to shut down? (yes/no): ").strip().lower()

if confirm == "yes":
    
    try:
        delay = int(input("Enter delay in seconds before shutdown (0 for immediate): ").strip())
        if delay < 0:
            print("Delay cannot be negative. Shutdown cancelled.")
        else:
            print(f"Shutting down in {delay} seconds...")
            
            __import__('os').system(f"shutdown /s /t {delay}")
    except ValueError:
        print("Invalid number entered. Shutdown cancelled.")
else:
    print("Shutdown cancelled.")