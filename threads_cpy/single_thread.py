import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

# When you create a Thread, you pass it a function and a list containing the
# arguments to that function. In this case, you’re telling the Thread to run
# thread_function() and to pass it 1 as an argument.

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

# A daemon thread will shut down immediately when the program exits.
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")

# To tell one thread to wait for another thread to finish, you call .join().
    x.join()

    logging.info("Main    : all done")
