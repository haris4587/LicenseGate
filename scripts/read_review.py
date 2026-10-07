"""Read finalized state from stable Studionet; never signs or sends a write."""
import argparse
import json
import requests
from pathlib import Path
from genlayer_py.abi import calldata
from genlayer_py.abi.transactions import serialize

parser = argparse.ArgumentParser()
parser.add_argument('contract_address')
parser.add_argument('review_id')
parser.add_argument('--sender', default='0x0000000000000000000000000000000000000000')
parser.add_argument('--output', default='evidence/final-state.json')
args = parser.parse_args()
encoded = serialize([calldata.encode({'method': 'get_review', 'args': [args.review_id]}), b'\x00'])
params = {'type': 'read', 'to': args.contract_address, 'from': args.sender, 'data': encoded, 'transaction_hash_variant': 'latest-final'}
payload = {'jsonrpc': '2.0', 'id': 1, 'method': 'gen_call', 'params': [params]}
response = requests.post('https://studio.genlayer.com/api', json=payload, timeout=60)
response.raise_for_status()
receipt = response.json()
if 'error' in receipt:
    raise RuntimeError(receipt['error'])
value = calldata.decode(bytes.fromhex(receipt['result'].removeprefix('0x')))
state = json.loads(value)
Path(args.output).write_text(json.dumps(state, indent=2) + '\n')
print(json.dumps({'state': state['state'], 'outcome': state['result']['outcome'] if state['result'] else None, 'decision_hash': state['decision_hash'], 'evidence_quality_score': state['evidence_quality_score']}))
