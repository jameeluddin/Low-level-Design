from Design_patterns.LoggingSystem.debug_log_processor import DebugLogProcessor
from Design_patterns.LoggingSystem.error_log_processor import ErrorLogProcessor
from Design_patterns.LoggingSystem.info_log_processor import InfoLogProcessor


def main():
    error = ErrorLogProcessor()
    debug = DebugLogProcessor()
    info = InfoLogProcessor()

    info.set_next(debug).set_next(error)

    info.log("ERROR", "This is jameel")


if __name__ == "__main__":
    main()

