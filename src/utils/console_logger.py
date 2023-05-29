import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ConsoleLogger:
    __logs = []
    __result_round_logs = []
    
    @staticmethod
    def log(msg):
        print(msg)
        ConsoleLogger.__logs.append(msg)
            
    @staticmethod
    def result_log(msg):
        ConsoleLogger.__result_round_logs.append(msg)
            

    @staticmethod
    def get_logs():
        return ConsoleLogger.__logs
    
    @staticmethod
    def get_result_logs():
        return ConsoleLogger.__result_round_logs
    
    @staticmethod
    def get_result_logs():
        return ConsoleLogger.__result_round_logs

    @staticmethod
    def clear_logs():
        ConsoleLogger.__logs = []
        ConsoleLogger.__result_round_logs = []
    
    @staticmethod
    def print_logs():
        for log in ConsoleLogger.get_logs():
            print(log)
    
    @staticmethod
    def print_result_logs():
        print("#### Logs ####")
        for log in ConsoleLogger.get_result_logs():
            print(log)