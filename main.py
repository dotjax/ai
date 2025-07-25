print("Type 'exit' or 'quit' to terminate the program.")
try:
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
except KeyboardInterrupt:
    print("\nKeyboard interrupt detected. Exiting...")
