class Observer:
    def __init__(self, name, Formatter):
        self.name = name
        self._Formatter = Formatter

    def update(self, message):
        print(f'{self.name} get the message: ', end='')
        print(self._Formatter.format(message))

class BasicFormatter():
    def format(self, message):
        return f'{message}!'

class FormatterDecorator(BasicFormatter):
    def __init__(self, Formatter):
        self._Formatter = Formatter

    def format(self, message):
        return self._Formatter.format(message)

# The above are fixed classes, please do not modify it.
# Please complete other classes here >>

class Messenger:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def send_message(self, message):
        for observer in self.observers:
            observer.update(message)        

class ReverseDecorator(FormatterDecorator):
    def format(self, message):
        formatted_message = super().format(message)
        return self.reverse(formatted_message)

    def reverse(self, message):
        # Formatting: reversing the message
        return message[::-1]

class StarDecorator(FormatterDecorator):
    def format(self, message):
        formatted_message = super().format(message)
        return self.addStar(formatted_message)

    def addStar(self, message):
        # Formatting: adding * at the beginning and the end of the message
        return f'*{message}*'
    
# << Please complete other classes here
# The following are the test cases, please do not modify them

# messenger is the subject to be observed
messenger = Messenger()

'''
Create Formatters by using decorator pattern.
Then use the Formatters to create observers.
'''
observers = [
    Observer("Alice", BasicFormatter()),
    Observer("Bob", ReverseDecorator(BasicFormatter())),
    Observer("Charlie", StarDecorator(BasicFormatter())),
    Observer("Dave", ReverseDecorator(StarDecorator(BasicFormatter())))
]

# Add the subscribers (observers) to the messenger
for observer in observers:
    messenger.attach(observer)

# Send the message
messenger.send_message("Hello, observer")

'''
Output:
Alice get the message: Hello, observer!
Bob get the message: !revresbo ,olleH
Charlie get the message: *Hello, observer!*
Dave get the message: *!revresbo ,olleH*
'''
