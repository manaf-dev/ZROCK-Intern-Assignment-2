# Python class with a method that print a message

class PrintMessageClass:

    def __init__(self, message):
        self.message = message

    def message_printer(self):
        print(self.message)


message = "Hello, this message is to be printed by class method."
print_message = PrintMessageClass(message)
print_message.message_printer()
