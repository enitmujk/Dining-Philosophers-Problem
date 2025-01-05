import threading
import time

# Define the Philosopher class
class Philosopher(threading.Thread):
    def __init__(self, name, left_chopstick, right_chopstick):
        threading.Thread.__init__(self)
        self.name = name
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.state = "thinking"

    def run(self):
        if self.name == "Ayn Rand":
            print(f"\n{self.name} is {self.state}.")
        elif self.name == "Michel Foucault":
            # Ensures Michel Foucault is printed immediately after Ayn Rand
            time.sleep(0.1)
            print(f"\n{self.name} is {self.state}.")
        else:
            print(f"\n{self.name} is {self.state}.")

# Create the chopsticks (semaphores)
chopsticks = [threading.Semaphore(1) for _ in range(5)]

# Create the philosophers
philosophers = [
    Philosopher("Friedrich Nietzsche", chopsticks[0], chopsticks[1]),
    Philosopher("Karl Marx", chopsticks[1], chopsticks[2]),
    Philosopher("Ayn Rand", chopsticks[2], chopsticks[3]),
    Philosopher("Jean-Paul Sartre", chopsticks[3], chopsticks[4]),
    Philosopher("Michel Foucault", chopsticks[4], chopsticks[0])
]

# Start the philosophers' threads
for philosopher in philosophers:
    philosopher.start()

# Ensure all threads complete
for philosopher in philosophers:
    philosopher.join()