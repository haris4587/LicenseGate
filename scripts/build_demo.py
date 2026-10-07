"""Build a reproducible package from public commit-pinned files (no signing)."""
import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('release_commit')
parser.add_argument('--output', default='evidence/demo-package.json')
args = parser.parse_args()
repo = 'haris4587/LicenseGate'
base = f'https://raw.githubusercontent.com/{repo}/{args.release_commit}/'
files = [('project-license', 'PROJECT_LICENSE', 'fixtures/PROJECT-LICENSE.txt', args.release_commit), ('manifest', 'RELEASE_MANIFEST', 'fixtures/release-manifest.json', args.release_commit), ('distribution', 'DISTRIBUTION', 'fixtures/distribution-missing-attribution.txt', args.release_commit), ('dep-license', 'DEPENDENCY_LICENSE', 'fixtures/MIT-LICENSE.txt', '80b4310c14f0b4a1e07f366889260c9eb48ae5d4')]
evidence = []
manifest = None
for eid, role, path, commit in files:
    url = f'https://raw.githubusercontent.com/{repo}/{commit}/{path}'
    with urllib.request.urlopen(url, timeout=30) as response:
        body = response.read()
    evidence.append({'id': eid, 'role': role, 'url': url, 'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)})
    if role == 'RELEASE_MANIFEST':
        manifest = json.loads(body)
package = dict(manifest)
package.update(commit=args.release_commit, policy='Permit MIT dependencies in binary distribution only when the distributed artifact includes the complete dependency copyright and permission notices. Missing notices are remediable requirements, not a material license incompatibility. Assess only the synthetic committed artifact inventory; do not assume separately published license review evidence is shipped with it.', evidence=evidence)
Path(args.output).parent.mkdir(parents=True, exist_ok=True)
Path(args.output).write_text(json.dumps(package, indent=2) + '\n')
print(json.dumps(package, separators=(',', ':')))
