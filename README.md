# Bulk Domain Authority Checker API — DA & backlinks for 1,000s of domains (Python, Node.js, cURL)

Check **domain authority and backlinks for a whole list of domains at once**: a **domain rank (0–100)**, **referring domains**, **total backlinks**, the **dofollow / nofollow split** and **30-day changes**, as JSON or a CSV-ready table. You pay per domain, with **no $129+/month Ahrefs or Semrush subscription**.

It uses the [**Bulk Domain Authority & Backlink Checker**](https://apify.com/jesting_grass/bulk-domain-authority-checker) on Apify, which reads a commercial backlink index. Invalid domains and domains without backlink data are not charged.

📖 Tutorial: [Check domain authority for 1,000 sites at once with Python](https://dev.to/jesting_grass/check-domain-authority-for-1000-sites-at-once-with-python-a-pay-per-use-ahrefs-alternative-570i)

## Quick start (Python)

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=your_token   # free account at https://console.apify.com
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("jesting_grass/bulk-domain-authority-checker").call(run_input={
    "domains": ["dev.to", "hashnode.com", "indiehackers.com", "allbirds.com", "gymshark.com"],
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["domain"], row.get("domainRank"), row.get("referringDomains"), row.get("backlinks"))
```

Real output (September 2026):

| domain | domainRank | referringDomains | backlinks | dofollowRatio | spamScore |
|---|---|---|---|---|---|
| dev.to | 82 | 93,830 | 17,292,820 | 0.81 | 13 |
| hashnode.com | 82 | 88,946 | 10,021,858 | 0.95 | 23 |
| indiehackers.com | 68 | 14,704 | 709,281 | 0.95 | 16 |
| gymshark.com | 59 | 9,663 | 99,941 | 0.63 | 24 |
| allbirds.com | 58 | 9,310 | 91,766 | 0.88 | 6 |

URLs are fine as input: `https://`, `www.` and paths are stripped, and duplicates are removed.

## Examples

| File | What it does |
|---|---|
| [`bulk_da_to_csv.py`](examples/bulk_da_to_csv.py) | Domain rank and backlink metrics for a list of domains → `domain_authority.csv` |
| [`link_building_prospects.py`](examples/link_building_prospects.py) | Link building: keep only prospects above a minimum domain rank (`minDomainRank`) |
| [`node.js`](examples/node.js) | Same in Node.js |
| [`curl.sh`](examples/curl.sh) | One HTTP call, JSON back |

## Output fields

| Field | Meaning |
|---|---|
| `domainRank` | Authority score 0–100 from the domain's backlink profile (similar in spirit to Moz DA or Ahrefs DR, not identical) |
| `referringDomains`, `referringMainDomains` | Unique websites (and root domains) linking to the domain |
| `backlinks`, `dofollowBacklinks`, `nofollowBacklinks`, `dofollowRatio` | Total links and their quality split |
| `referringIps`, `referringSubnets`, `referringPages` | Diversity of linking sites |
| `textBacklinks`, `imageBacklinks`, `redirectBacklinks` | Link types |
| `spamScore` | 0–100 spam signal of the backlink profile |
| `brokenBacklinks` | Links pointing to pages that no longer work |
| `newReferringDomains`, `lostReferringDomains`, `referringDomainsChange`, `newBacklinks`, `lostBacklinks`, `backlinksChange` | Last 30 days, with `includeChanges: true` |

## Ahrefs vs Semrush vs this

| | Ahrefs | Semrush | This |
|---|---|---|---|
| Price | Lite from $129/month | SEO plan from $139/month | pay per domain, no subscription |
| Bulk list of domains | yes (Batch Analysis) | yes (Bulk Analysis) | yes, thousands per run |
| Filter by authority | manual | manual | `minDomainRank` input |
| Works from n8n / Make / Zapier / AI agents | via API on higher plans | via API on higher plans | yes, plus Apify MCP server |

Prices as listed on the vendors' pricing pages in September 2026 (monthly billing).

## Use cases

- **Link building**: qualify guest-post and outreach prospects by authority before you email them
- **SEO audits**: benchmark a client against competitors in one run
- **Expired domains and domain investing**: screen lists by referring domains and dofollow ratio
- **Agencies and lead gen**: add authority columns to a list of websites
- **Monitoring**: schedule a weekly run and track referring-domain changes

## FAQ

**Is domain rank the same as Moz DA or Ahrefs DR?** No. Each vendor computes authority from its own backlink index, so the numbers differ between tools. Use one score consistently to compare domains with each other.

**Can I get the individual backlinks?** This returns aggregate metrics per domain. Open an issue on the [Actor page](https://apify.com/jesting_grass/bulk-domain-authority-checker/issues) if you need backlink lists.

## More SEO tools from the same developer

- [Backlink Checker API](https://github.com/emiohr/backlink-checker-api): every backlink, referring domains and competitor link gap
- [Keyword Research API](https://github.com/emiohr/keyword-research-api): search volume, keyword difficulty, intent and AI Overviews in bulk
- [Google Trends API](https://github.com/emiohr/google-trends-api): interest over time, rising queries and regions
- [BuiltWith & Wappalyzer alternative](https://github.com/emiohr/builtwith-wappalyzer-alternative): tech stack of any website in bulk

*Not affiliated with Ahrefs, Semrush or Moz; names are used for comparison only. Examples are MIT licensed.*
