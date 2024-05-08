# We are creating this file to log all the execution going to happen in the project eg. all the
# exceptions and many other things in a text file.So, that we can refer back to them when needed.

# A "log file" is a text file that records the events or messages that occur during the execution
# of a program.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("The LOGGING has started")


# Explaination of above program ====>

""" 1. `import logging`: This line imports a module named `logging` into your Python script. This module is presumably used for logging purposes.

2. `import os`: Here, the `os` module is imported. This module provides a way to interact with the operating system, such as creating directories and working with file paths.

3. `from datetime import datetime`: This line imports the `datetime` class from the `datetime` module. The `datetime` class allows you to work with dates and times.

4. `LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"`: This line creates a variable named `LOG_FILE`. It uses the `datetime.now()` function to get the current date and time, and then formats it as a string in the format `month_day_year_hour_minute_second.log`. This will be used as the name of the log file.

5. `logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)`: Here, a variable named `logs_path` is created. It uses the `os.getcwd()` function to get the current working directory and joins it with the "logs" folder and the `LOG_FILE` variable to create a full path to the log file. This path will be where the log file is stored.

6. `os.makedirs(logs_path,exist_ok=True)`: This line creates the directory specified by the `logs_path` variable if it doesn't already exist. The `exist_ok=True` parameter ensures that the code won't raise an error if the directory already exists.

7. `LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)`: Here, a variable named `LOG_FILE_PATH` is created by joining the `logs_path` and `LOG_FILE` variables together. This gives you the full path to the log file, including the filename.

8. `logging.basicConfig(...)`: This is where the configuration for the logging system is set up using the `basicConfig` function from the `logging` module.

   - `filename = LOG_FILE_PATH`: This specifies the filename for the log file. It uses the `LOG_FILE_PATH` variable created earlier, so logs will be written to the file with the path you specified.
   
   - `format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"`: This sets the format for each log message. It includes information like the timestamp (`%(asctime)s`), line number (`%(lineno)d`), logger name (`%(name)s`), log level (`%(levelname)s`), and the actual log message (`%(message)s`).

   %(asctime)s ---> ascending time

   - `level = logging.Info()`: This sets the minimum logging level to `INFO`. This means that only log messages with an `INFO` level or higher (e.g., `WARNING`, `ERROR`, `CRITICAL`) will be written to the log file.

Overall, this code sets up a logging system that creates a new log file with a unique name based on the current date and time, and it specifies the format and logging level for the log messages. It's a useful way to keep track of what happens in your Python script.
"""


# What does logging logging.basicConfig(...) is doing ?

"""
---> "configuration for the logging system" refers to the settings and parameters that are used to set up how the Python logging module should behave. The `logging.basicConfig(...)` function call is used to configure various aspects of the logging system, such as:

1. **Filename**: You specify the filename where log messages will be written. This is done with the `filename` parameter, which you set to `LOG_FILE_PATH`. It tells the logging system where to save the log messages.

2. **Log Message Format**: You define how each log message should be formatted using the `format` parameter. In your code, you provided a format string "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s". This format string specifies how each log message should look, including details like the timestamp, line number, logger name, log level, and the actual log message.

3. **Log Level**: The `level` parameter sets the minimum log level that should be recorded. In your code, you set it to `logging.Info()`, which means that only log messages with an `INFO` level or higher (e.g., `WARNING`, `ERROR`, `CRITICAL`) will be written to the log file.

These configuration settings help you control and customize how log messages are generated and stored. By specifying the log file path, format, and log level, you can tailor the logging system to meet your specific needs. For example, you might choose to log detailed information during development (`DEBUG` level), but only important events in production (`INFO` level or higher). The format also allows you to include relevant metadata alongside log messages for easier debugging and analysis. 
"""
