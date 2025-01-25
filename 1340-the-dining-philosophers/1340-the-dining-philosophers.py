import threading

class DiningPhilosophers:
    def __init__(self):
        # Single mutex to control access to the critical section
        self.mutex = threading.Lock()

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        # Lock the critical section to ensure only one philosopher eats at a time
        with self.mutex:
            # Pick up forks
            pickLeftFork()
            pickRightFork()

            # Eat
            eat()

            # Put down forks
            putLeftFork()
            putRightFork()
