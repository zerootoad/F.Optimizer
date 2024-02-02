import requests
from bs4 import BeautifulSoup
import sqlite3

class FetchedData:
    def fetch_data(self, url, class_name):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find_all("span", class_=class_name)
        return [item.text.strip() for item in data]

    def save_to_sqlite(self, data):
        conn = sqlite3.connect('dataset/fetched_data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS fetched_data
                     (cpu TEXT, gpu TEXT, drive TEXT, type TEXT)''')
        
        for item in data:
            c.execute("SELECT * FROM fetched_data WHERE cpu=? AND gpu=? AND drive=? AND type=?", item)
            existing_data = c.fetchone()
            if not existing_data:
                c.execute("INSERT INTO fetched_data VALUES (?, ?, ?, ?)", item)
        
        conn.commit()
        conn.close()

    def fetch_and_save(self, url_cpu, url_gpu, url_drive, data_type):
        cpus = self.fetch_data(url_cpu, "prdname")
        gpus = self.fetch_data(url_gpu, "prdname")
        drives = self.fetch_data(url_drive, "prdname")
        data = [(cpu, gpu, drive, data_type) for cpu, gpu, drive in zip(cpus, gpus, drives)]
        self.save_to_sqlite(data)

    def save_fetched_data(self):
        print("\nSaving fetched data...")
        self.fetch_and_save(
            "https://www.cpubenchmark.net/low_end_cpus.html",
            "https://www.videocardbenchmark.net/low_end_gpus.html",
            "https://www.harddrivebenchmark.net/low_end_drives.html",
            "Low End"
        )
        self.fetch_and_save(
            "https://www.cpubenchmark.net/midlow_range_cpus.html",
            "https://www.videocardbenchmark.net/midlow_range_gpus.html",
            "https://www.harddrivebenchmark.net/low_mid_range_drives.html",
            "Low Mid Range"
        )
        self.fetch_and_save(
            "https://www.cpubenchmark.net/mid_range_cpus.html",
            "https://www.videocardbenchmark.net/mid_range_gpus.html",
            "https://www.harddrivebenchmark.net/mid_range_drives.html",
            "High Mid Range"
        )
        self.fetch_and_save(
            "https://www.cpubenchmark.net/high_end_cpus.html",
            "https://www.videocardbenchmark.net/high_end_gpus.html",
            "https://www.harddrivebenchmark.net/high_end_drives.html",
            "High End"
        )

data_fetcher = FetchedData()
data_fetcher.save_fetched_data()
