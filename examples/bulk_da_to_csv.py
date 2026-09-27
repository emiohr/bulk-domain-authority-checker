"""Domain authority + backlink metrics for a list of domains -> CSV.

pip install "apify-client>=3"
export APIFY_TOKEN=...   # free account: https://console.apify.com
"""
import csv
import os

from apify_client import ApifyClient

DOMAINS = ["dev.to", "allbirds.com", "gymshark.com", "hashnode.com", "indiehackers.com"]
COLUMNS = ["domain", "domainRank", "referringDomains", "backlinks", "dofollowRatio", "spamScore", "brokenBacklinks"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/bulk-domain-authority-checker").call(run_input={"domains": DOMAINS})

with open("domain_authority.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for row in sorted(client.dataset(run.default_dataset_id).iterate_items(), key=lambda r: -(r.get("domainRank") or 0)):
        if "error" not in row:
            writer.writerow(row)
            print(f'{row["domain"]:<18} rank {row["domainRank"]:<4} ref. domains {row["referringDomains"]:>8,}  backlinks {row["backlinks"]:>10,}')
print("Saved domain_authority.csv")
