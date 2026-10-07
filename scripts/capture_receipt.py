"""Fetch public stable-Studio receipt and save only reviewable evidence fields."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import requests
from genlayer_py.abi import calldata

parser = argparse.ArgumentParser()
parser.add_argument('transaction_hash')
parser.add_argument('output')
parser.add_argument('--canonical-source')
args = parser.parse_args()
response = requests.post('https://studio.genlayer.com/api', json={'jsonrpc':'2.0','id':1,'method':'eth_getTransactionByHash','params':[args.transaction_hash]}, timeout=60)
response.raise_for_status()
raw = response.json()
if 'error' in raw:
    raise RuntimeError(raw['error'])
r = raw['result']
summary = {k:r.get(k) for k in ('hash','from_address','to_address','value','type','status','result_name','created_at','leader_only','execution_mode','num_of_initial_validators','rotation_count','last_round')}
summary['rounds'] = []
for round_data in r.get('consensus_history', {}).get('consensus_results', []):
    item = {'status_changes':round_data.get('status_changes'), 'consensus_round':round_data.get('consensus_round'), 'leaders':[], 'validators':[]}
    for leader in round_data.get('leader_result', []):
        observed = {'execution_result':leader.get('execution_result'), 'vote':leader.get('vote')}
        for index, encoded in leader.get('eq_outputs', {}).items():
            try:
                observed.setdefault('equivalence_outputs', {})[index] = calldata.decode(base64.b64decode(encoded)[1:])
            except Exception:
                observed.setdefault('equivalence_output_hashes', {})[index] = hashlib.sha256(base64.b64decode(encoded)).hexdigest()
        item['leaders'].append(observed)
    for validator in round_data.get('validator_results', []):
        item['validators'].append({'address':validator.get('node_config',{}).get('address'), 'vote':validator.get('vote'), 'execution_result':validator.get('execution_result')})
    summary['rounds'].append(item)
if args.canonical_source:
    deployed = base64.b64decode(r['data']['contract_code'])
    summary['source_sha256'] = hashlib.sha256(deployed).hexdigest()
    summary['source_matches_canonical'] = deployed == Path(args.canonical_source).read_bytes()
    if not summary['source_matches_canonical']:
        raise RuntimeError('Deployed source differs from canonical source')
Path(args.output).write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary.get(k) for k in ('hash','status','result_name','leader_only','source_sha256','source_matches_canonical','rotation_count')}))
