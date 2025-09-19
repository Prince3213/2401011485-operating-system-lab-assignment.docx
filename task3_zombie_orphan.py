import os
import time

def zombie_process():
    child_pid = os.fork()
    if child_pid == 0:
        print(f"Child PID {os.getpid()} exiting immediately to become zombie.")
        os._exit(0)
    else:
        print("Parent sleeping for 15 seconds. Check zombie using 'ps -el | grep defunct' in another terminal.")
        time.sleep(15)
        print("Parent exiting now.")

def orphan_process():
    child_pid = os.fork()
    if child_pid == 0:
        print(f"Child PID {os.getpid()} will be orphaned. Sleeping for 15 seconds.")
        time.sleep(15)
        print("Child finished execution.")
    else:
        print("Parent exiting immediately, leaving child as orphan.")
        os._exit(0)

if __name__ == "__main__":
    option = input("Choose scenario:\n1. Zombie process\n2. Orphan process\nEnter choice (1 or 2): ")
    if option == "1":
        zombie_process()
    elif option == "2":
        orphan_process()
    else:
        print("Invalid choice entered.")
