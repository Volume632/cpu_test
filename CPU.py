import psutil
import pandas as pd

def get_processes_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'username': proc.info['username']
    })
    return processes

def main():
    processes = get_processes_info()
    df = pd.DataFrame(processes)
    print(df)

if __name__ == '__main__':
    main()    