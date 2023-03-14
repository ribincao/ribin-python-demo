import threading
import queue


class Actor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.inbox = queue.Queue()

    def send(self, message):
        self.inbox.put(message)

    def run(self):
        while True:
            message = self.inbox.get()
            if message == 'die':
                break
            self.process_message(message)

    def process_message(self, message):
        print(message)


if __name__ == '__main__':
    alice = Actor()
    alice.start()
    alice.send('Hello, ribincao!')
    alice.send('Goodbye, ribincao!')
    alice.send('die')
    alice.join()

