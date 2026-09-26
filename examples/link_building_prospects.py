"""Link building: keep only prospects above a minimum domain rank."""
import os

from apify_client import ApifyClient

prospects = ["dev.to", "hashnode.com", "indiehackers.com", "allbirds.com", "gymshark.com"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/bulk-domain-authority-checker").call(run_input={
    "domains": prospects,
    "minDomainRank": 60,          # only strong sites
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    if "error" not in row:
        print(row["domain"], "rank", row["domainRank"], "| dofollow ratio", row["dofollowRatio"])
