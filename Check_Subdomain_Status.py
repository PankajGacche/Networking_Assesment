import requests
from tabulate import tabulate
import os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
rootfolder = os.path.dirname(os.path.abspath(__file__))
subdomain_validation_check_log = os.path.join(rootfolder, "subdomain_validation_check.log")

# Log start of the Python script
with open(subdomain_validation_check_log, 'a') as log:
    log.write(f"Python script started at {date}\n")

    # List of subdomains to check
    subdomains = ['en.wikipedia.org', 'store.example.com','en.m.wikipedia.org', 'secure.wikimedia.org/wikipedia/en/wiki/Main_Page']

    def check_subdomains(subdomains):
        results = []
        for subdomain in subdomains:
            try:
                response = requests.get(f"http://{subdomain}")
                if response.status_code == 200:
                    status = 'UP'
                else:
                    status = 'DOWN'
            except requests.ConnectionError:
                status = 'DOWN'
            results.append([subdomain, status])
        return results

    def print_status_table(results):
        headers = ["Subdomain", "Status"]
        print(tabulate(results, headers=headers, tablefmt="grid"))

    def main():
            results = check_subdomains(subdomains)
            log.write(f"Sub-domain availibility check at {date}\n")
            log.write(f"{results}")
            print("")
            print(f"Sub-domain availibility check at {date}\n")
            print_status_table(results)

    if __name__ == "__main__":
        main()
