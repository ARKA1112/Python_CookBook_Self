#Chapter 5 page 172

import time
import threading

class Countdown:
    def __init__(self,n) -> None:
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()


    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


    def __getstate__(self) -> object:
        return self.n


    def __setstate__(self,n):
        self.__init__(n)