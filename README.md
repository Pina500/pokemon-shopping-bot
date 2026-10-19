# Pokémon Shopping Assistant — Private Development Repository

A Windows-first Pokémon TCG watchlist and purchasing-assistance project, currently in personal trial. The software does not place orders, and product purchase handoff requires human review.

## Latest locally tested build
**V6 Trial Edition:** 24 automated tests passed locally. The release ZIP has been supplied in our ChatGPT conversation. The full V6 source is packaged inside that ZIP and should be uploaded to this repository before future GitHub-based changes.

## Safety and retailer coverage
- Simulation and live inventory observations are separated.
- Pokémon Center, Target, Walmart, Best Buy, and GameStop watchlists.
- Optional Best Buy official Products API; live access needs a valid developer key.
- Other retailers have no live inventory connector yet. Never claim otherwise.
- No automated ordering, payment, unauthorized scraping, or bot-protection bypassing.

## Next steps
1. Import the contents of the V6 release ZIP into this repository (app.py, bestbuy_api.py, tests/, launchers).
2. Set up Python unittest continuous integration.
3. Test Windows UI manually, then document findings.
4. Pursue retailer-authorized integrations and opt-in notifications.

**Never commit API keys, payment information, or customer data.**
