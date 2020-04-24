import sys

def fibonacci(n):
    low = 0
    high = 1
    sequence = [low, high]
    for _ in range(2, n):
        sequence.append(low + high)
        temp = high
        high = low + high
        low = temp

    return sequence[:n]

if __name__ == '__main__':
    print(compute_sequence(int(sys.argv[1])))
