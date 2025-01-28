if __name__ == '__main__':
    N = int(input())  # Read the number of commands
    l = []  # Initialize an empty list
    
    for _ in range(N):
        com, *args = input().split()  # Read command and its arguments
        getattr(l, com)(*map(int, args)) if com != "print" else print(l)  # Execute command