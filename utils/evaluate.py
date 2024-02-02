import wmi, sqlite3, os, re

class pcInfo():
    def __init__(self):
        self.c = wmi.WMI()

    def get_cpu(self):
        for cpu in self.c.Win32_Processor():
            cpu_name = re.sub(r'\([^)]*\)', '', cpu.Name).strip()
            cpu_name = cpu_name.replace(" CPU", "").strip()
            return cpu_name

    def get_gpu(self):
        for gpu in self.c.Win32_VideoController():
            gpu_name = re.sub(r'\([^)]*\)', '', gpu.Name).strip()
            return gpu_name

    def get_os(self):
        for os in self.c.Win32_OperatingSystem():
            caption = os.Caption.lower()
            if 'windows' in caption:
                os_type = 'Microsoft'
            elif 'linux' in caption:
                os_type = 'Linux'
            elif 'mac' in caption or 'darwin' in caption:
                os_type = 'Mac'
            break
        return os_type
    
class pcType():
    def main(self, cpu, gpu):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_directory, '..', 'dataset', 'fetched_data.db')

        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        c.execute(f"SELECT * FROM fetched_data")
        data = c.fetchall()

        for row in data:
            if cpu and cpu.lower() in row[0].lower():
                print("CPU: " + row[0] + " | type: " + row[3])
            if gpu and gpu.lower() in row[1].lower():
                print("GPU: " + row[1] + " | type: " + row[3])

        conn.close()
        