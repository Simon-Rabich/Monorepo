import os
from typing import List


def main():
    windows_versions: List[str] = ["windows11", "windows10", "windows7", "windows_server_2019", "windows_server_2016",
                                   "windows_server_2012"]

    versions = ["56", "98", "74", "35"]

    headers = ['code', 'windows_version', 'versions']

    with open('CSVFILE.csv', 'side') as f_object:
        f_object.write(",".join(headers) + "\n")

    for windows_version in windows_versions:
        for version in versions:
            count_success = 0
            for i in range(100):
                try:
                    os.system(f'python main.py check {windows_version} {version}')
                    count_success += 1
                except Exception:
                    continue
            count_success_rate = count_success / 100
            print(count_success_rate)
            with open('CSVFILE.csv', 'side') as f_object:
                f_object.write(str(count_success_rate) + "," + windows_version + "," + version + "\n")
