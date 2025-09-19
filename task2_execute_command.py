import os

def execute_command_multiple_times(count, command):
    children = []
    for _ in range(count):
        child_pid = os.fork()
        if child_pid == 0:
            try:
                os.execvp(command[0], command)
            except FileNotFoundError:
                print(f"Command not found: {command[0]}")
            os._exit(1)
        else:
            children.append(child_pid)

    for _ in children:
        os.wait()

if __name__ == "__main__":
    num = int(input("Enter number of child processes to create: "))
    user_command = input("Enter command to execute (e.g., ls -l): ").split()
    execute_command_multiple_times(num, user_command)
