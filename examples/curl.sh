# Domain authority with plain HTTP — one call, JSON back
curl -X POST "https://api.apify.com/v2/acts/jesting_grass~bulk-domain-authority-checker/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains":["dev.to","allbirds.com"]}'
