import psutil
value = psutil.cpu_times()
print(value)
for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
    if  process.info['name'] == 'Teams.exe':
        if process.info['status'] == 'running':
            process.name = 'myprocess'
        print(process)