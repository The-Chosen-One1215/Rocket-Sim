# main.py
from working import handle_command
from terminal import terminal

if __name__ == "__main__":
    while True:
        command = terminal(">> ").strip().upper()
        if command == "EXIT":
            print("Exiting...")
            break
        handle_command(command)
