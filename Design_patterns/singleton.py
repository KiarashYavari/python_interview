# scenario: Think of a logging system, you only need one object to 
# write out the logs into files, console or database. 
# Because having multiple loggers may lead to inconsistent logs 
# or file conflicts. For this problem we use singleton design:

class SingletonLogger:
    _instance = None  # This holds the singleton instance

    def __new__(cls, *args, **kwargs):
        # If an instance doesn't already exist, create one
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_file):
        # We ensure this is only initialized once
        if not hasattr(self, "initialized"):
            self.log_file = log_file
            with open(self.log_file, "w") as file:
                file.write("Logger Initialized\n")
            self.initialized = True  # Set a flag to prevent reinitialization

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")


# Usage
logger1 = SingletonLogger("./Design_patterns/logfile.txt")
logger2 = SingletonLogger("./Design_patterns/logfile.txt")

logger1.log("First log message")
logger2.log("Second log message")

print(logger1 is logger2)  # True, both are the same instance
