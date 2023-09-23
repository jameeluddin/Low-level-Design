from Design_patterns.LoggingSystem.log_processor import LogProcessor


class InfoLogProcessor(LogProcessor):
    def log(self, log_level, msg):
        if log_level == "INFO":
            print("INFO " + msg)
        else:
            super().log(log_level, msg)

