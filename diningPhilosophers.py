import threading
import time
import random

# Define the number of philosophers
N = 4  # Since we are not exceeding 4

# Create a semaphore for each chopstick
chopsticks = [threading.Semaphore(1) for _ in range(N)]

# Create a binary semaphore (mutex) for mutual exclusion
mutex = threading.Semaphore(1)

# Function for each philosopher to pick up chopsticks, eat, and put them down
def philosopher(id):
    left = id
    right = (id + 1) % N

    while True:
        # Think for a random amount of time
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 5))

        # Ensure mutual exclusion when attempting to pick up chopsticks
        mutex.acquire()
        
        # Attempt to acquire the left chopstick
        acquired_left = chopsticks[left].acquire(blocking=False)
        if acquired_left:
            # Attempt to acquire the right chopstick
            acquired_right = chopsticks[right].acquire(blocking=False)
            if acquired_right:
                # Eat for a random amount of time
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 5))
                
                # Put down the right chopstick
                chopsticks[right].release()
            # Put down the left chopstick
            chopsticks[left].release()
        
        # Release the mutex semaphore
        mutex.release()

        if not (acquired_left and acquired_right):
            print(f"Philosopher {id} couldn't pick up both chopsticks and is thinking again.")

# Create and start philosopher threads
philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for p in philosophers:
    p.start()