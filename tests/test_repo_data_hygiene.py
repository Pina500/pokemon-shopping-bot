"""Prevent accidental tracking of local trial state and telemetry."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IgnoreRulesTests(unittest.TestCase):
    def test_trial_state_patterns_are_present(self):
        rules = {
            line.strip()
            for line in (ROOT / '.gitignore').read_text(encoding='utf-8').splitlines()
            if line.strip() and not line.startswith('#')
        }
        expected = {
            'tasks-v11.json', 'events-v12.jsonl', 'supervisor-v13.jsonl',
            'PokemonBotLab/', 'watchlist.json', 'approved_signals.json',
            '.env', '.env.*', '*.pid', '*.sqlite', '*.sqlite3', '*.db',
            'playwright-report/', 'test-results/',
        }
        self.assertTrue(expected.issubset(rules), expected - rules)


if __name__ == '__main__':
    unittest.main()
