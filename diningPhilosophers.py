import threading
import time
import random

# defines the number of philosophers
N = 4  # four philosophers

# creates a semaphore for each chopstick
chopsticks = [threading.Semaphore(1) for _ in range(N)]

# creates a binary semaphore (mutex) for mutual exclusion
mutex = threading.Semaphore(1)

# function for each philosopher to pick up chopsticks, eat, and put them down
def philosopher(id):
    left = id
    right = (id + 1) % N

    while True:
        # thinks for a random amount of time
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 5))

        # ensures mutual exclusion when attempting to pick up chopsticks
        mutex.acquire()
        
        # attempts to acquire the left chopstick
        acquired_left = chopsticks[left].acquire(blocking=False)
        if acquired_left:
            # attempts to acquire the right chopstick
            acquired_right = chopsticks[right].acquire(blocking=False)
            if acquired_right:
                # eats for a random amount of time
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 5))
                
                # puts down the right chopstick
                chopsticks[right].release()
            # puts down the left chopstick
            chopsticks[left].release()
        
        # releases the mutex semaphore
        mutex.release()

        if not (acquired_left and acquired_right):
            print(f"Philosopher {id} couldn't pick up both chopsticks and is thinking again.")

# function that creates and start philosopher threads
philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for p in philosophers:
    p.start()