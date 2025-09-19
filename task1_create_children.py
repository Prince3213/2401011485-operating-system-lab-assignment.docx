import os

def create_multiple_processes(count):
    child_pids = []
    for _ in range(count):
        child = os.fork()
        if child == 0:
            print(f"Child PID: {os.getpid()}, Parent PID: {os.getppid()}, Message: Hello from child")
            os._exit(0)
        else:
            child_pids.append(child)

    for _ in child_pids:
        os.wait()

if __name__ == "__main__":
    num = int(input("Enter number of child processes to create: "))
    create_multiple_processes(num)
