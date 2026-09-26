// Bulk domain authority check in Node.js — npm i apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('jesting_grass/bulk-domain-authority-checker').call({
    domains: ['dev.to', 'allbirds.com', 'gymshark.com'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.domain, row.domainRank, row.referringDomains);
