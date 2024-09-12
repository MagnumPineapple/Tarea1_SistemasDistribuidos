import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor

dataset_path = "/home/magnum/T1_SD/archive/3rd_lev_domains.csv"
df = pd.read_csv(dataset_path, nrows=10000)

domains = df['ascension.gov.ac'].tolist()

def fetch(domain, index):
    response = requests.get(f'http://localhost:5000/resolve?domain={domain}')
    print(f"Sample {index}: {response.json()}")

with ThreadPoolExecutor(max_workers=10) as executor: 
    for index, domain in enumerate(domains, start=1):
        executor.submit(fetch, domain, index)
