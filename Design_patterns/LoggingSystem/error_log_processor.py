from Design_patterns.LoggingSystem.log_processor import LogProcessor


class ErrorLogProcessor(LogProcessor):
    def log(self, log_level, msg):
        if log_level == "ERROR":
            print("Error " + msg)
        else:
            super().log(log_level, msg)

