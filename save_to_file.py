import psutil
import pandas as pd
import json

def get_processes_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'username': proc.info['username']
        })
    return processes

def write_to_json(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, "w") as file:
                file.write(result.to_json())
        return wrapper
    return decorator

@write_to_json("processes.json")
def main():
    processes = get_processes_info()
    df = pd.DataFrame(processes)
    return df

if __name__ == '__main__':
    main()