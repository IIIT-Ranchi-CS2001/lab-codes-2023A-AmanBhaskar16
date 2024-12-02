# lab-7

import random
import math
import matplotlib.pyplot as plt

# Step 1: Form a list of K random numbers within a limit N
def generate_random_numbers(K, N):
    return [random.randint(1, N) for _ in range(K)]

# Step 2: Functions to find prime and composite numbers
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_prime_composite(numbers):
    primes = []
    composites = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        elif num > 1:  # Composite numbers are greater than 1
            composites.append(num)
    return primes, composites

# Step 3: Calculate squares of primes and square roots of composites
def calculate_squares_and_roots(primes, composites):
    prime_squares = [num ** 2 for num in primes]
    composite_roots = [math.sqrt(num) for num in composites]
    return prime_squares, composite_roots

# Step 4: Plotting the results
def plot_results(primes, prime_squares, composites, composite_roots):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Subplot 1: Prime numbers vs their squares
    ax1.scatter(primes, prime_squares, color='blue')
    ax1.set_title('Prime Numbers vs Their Squares')
    ax1.set_xlabel('Prime Numbers')
    ax1.set_ylabel('Squares of Prime Numbers')

    # Subplot 2: Composite numbers vs their square roots
    ax2.scatter(composites, composite_roots, color='red')
    ax2.set_title('Composite Numbers vs Their Square Roots')
    ax2.set_xlabel('Composite Numbers')
    ax2.set_ylabel('Square Roots of Composite Numbers')

    plt.tight_layout()
    plt.show()

# Main program
if __name__ == "__main__":
    # User input for K and N
    K = int(input("Enter the number of random numbers (K, minimum 10): "))
    N = int(input("Enter the upper limit for random numbers (N): "))

    if K < 10:
        print("K must be at least 10.")
    else:
        # Generate random numbers
        numbers = generate_random_numbers(K, N)
        print("Random Numbers:", numbers)

        # Separate prime and composite numbers
        primes, composites = separate_prime_composite(numbers)
        print("Prime Numbers:", primes)
        print("Composite Numbers:", composites)

        # Calculate squares of primes and square roots of composites
        prime_squares, composite_roots = calculate_squares_and_roots(primes, composites)

        # Plot the results
        plot_results(primes, prime_squares, composites, composite_roots)
