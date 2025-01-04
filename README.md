Executive Summary: This project aims to develop a console-based simulation of the classic Dining
Philosophers Problem, a well-known synchronization challenge in operating systems. The program
will represent philosophers as threads and forks as shared resources managed by semaphores. The
solution will ensure that philosophers alternate between thinking and eating while preventing
deadlock and starvation. The project demonstrates key concepts in process synchronization,
threading, and resource management in a simple and educational manner.

Key Features:
  1. Philosopher Simulation
    o Represents 3 philosophers using threads.
    o Philosophers alternate between "Thinking" and "Eating" states.
  2. Fork Management
    o Forks are managed using semaphores to control access.
  3. Deadlock Prevention
    o Implements techniques like limiting concurrent philosophers or asymmetric fork-
picking strategies to avoid deadlock.
  4. Console Output
    o Displays real-time updates of philosopher states and fork usage.

Proposed Implementation:
  1. Philosopher Class:
    o Encapsulates philosopher behavior (thinking, picking forks, eating, releasing forks).
    o Each philosopher operates in an infinite loop simulating their lifecycle.
  2. Forks as Resources:
    o Forks are represented as semaphores, ensuring exclusive access.
    o Philosopher threads attempt to acquire two forks (left and right) before eating.
  3. Deadlock Prevention:
    o Limits the number of philosophers picking forks simultaneously to .
    o Alternatively, uses an asymmetric strategy for fork acquisition (odd philosophers
pick left first, even pick right first).
  4. Console Interface:
    o Logs state changes (e.g., "Philosopher 1 is eating," "Philosopher 2 is thinking").
