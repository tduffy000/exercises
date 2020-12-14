def block():
    return

class Foo:
    def __init__(self):
        self.is_first_finished = False
        self.is_second_finished = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.is_first_finished = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.is_first_finished:
            block()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.is_second_finished = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not (self.is_first_finished and self.is_second_finished):
            block()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
