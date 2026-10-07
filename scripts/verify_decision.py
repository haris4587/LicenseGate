"""Recompute a FINAL review digest using its exact deployed domain."""
import argparse
import hashlib
import json
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('state_file')
parser.add_argument('contract_address')
parser.add_argument('--chain-id', type=int, default=61999)
args = parser.parse_args()
r = json.loads(Path(args.state_file).read_text())
assert r['state'] == 'FINAL'
expected, r['decision_hash'] = r['decision_hash'], ''
bound = {'protocol': 'LicenseGate-v1', 'contract': args.contract_address, 'chain_id': args.chain_id, 'review': r}
actual = hashlib.sha256(json.dumps(bound, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()
assert actual == expected, f'Digest mismatch: {actual} != {expected}'
print('Verified decision_hash:', actual)
