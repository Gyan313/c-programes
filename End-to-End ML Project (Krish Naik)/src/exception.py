# We imported above "sys" lib to help out with the exception occurs in the whole project.
import sys

# imported "logger.py" file as "import logger", so that we can log the exception occuring,in whole project.
import logging

import logger


def exception_message_detail(exception, exception_detail: sys):
    _, _, exc_tb = exception_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    exception_message = f"Exception occured in python script name {file_name}, line number {exc_tb.tb_lineno} has exception message {str(exception)}"

    return exception_message


class CustomException(Exception):
    # __init__ is the constructor of the "CustomException" class
    def __init__(self, exception_message, exception_detail: sys):
        super().__init__(exception_message)
        # We used super here cause see we are inheriting the Exception class of python,
        # so , we used super to initialize variables in the parent class that are necessary for the child class to function properly.
        self.exception_message = exception_message_detail(
            exception_message, exception_detail
        )

    # If you print the object of the CustomException class, this __str__() will be called.
    def __str__(self) -> str:
        return self.exception_message


# simple, example of how our customException and logger.py file deal with the below exception.
if __name__ == "__main__":
    try:
        z = 1 / 0
    except Exception as e:
        logging.info("Divide By zero")
        raise CustomException(e, sys)


# how above works ---->

# 1) Lets start with exception_message_detail function.

# exception_detail.exc_info() ----> this will return 3 values (If an exception e is currently handled (so exception() would return e), exc_info() returns the tuple (type(e), e, e.__traceback__). That is, a tuple containing the type of the exception (a subclass of BaseException), the exception itself, and a traceback object which typically encapsulates the call stack at the point where the exception last occurred.)

# https://docs.python.org/3/library/sys.html ----> visit this to understand sys.exc_info() deep.

# 2)  super.__init__(exception_message) ---> explained with an example.
""" 
class ParentClass:
    def __init__(self, message):
        self.message = message

class ChildClass(ParentClass):
    def __init__(self, exception_message):
        super().__init__(exception_message)
        # Rest of the child class's initialization code

# Create an instance of ChildClass
child_instance = ChildClass("An exception occurred.")

# Now, child_instance.message will contain "An exception occurred."
 """


# This code we written above work for all the exceptions occured in our project if we call
# CustomException class in every (try-except) scenerio.
# See, how powerful it is , we just needed to write code one time and can use it as much as we can.
