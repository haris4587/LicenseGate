# Deployment

Canonical source: `contracts/licensegate.py`. No external wallet is required. Use the account selector in https://studio.genlayer.com and Studio-provided accounts.

Stable Studionet: chain 61999, RPC https://studio.genlayer.com/api, Explorer https://explorer-studio.genlayer.com. The Studio UI may label this hosted development chain as local; it is the official stable Studionet endpoint. Do not substitute studio-dev (61997) or Bradbury (4221).

Process:
1. Run the complete test suite and `genvm-lint check contracts/licensegate.py`.
2. Push the canonical source to main and verify its bytes via GitHub.
3. Record its source commit and SHA-256. Import that file into Studio. If an old file with the same name already exists, use a distinct Studio import filename containing the exact canonical bytes; duplicate-name imports can retain old editor contents. The repository source remains contracts/licensegate.py. Verify the deployed transaction source hash rather than trusting the editor filename.
4. Select Full Consensus before deployment/execution. Deploy LicenseGate with no constructor arguments and no transferred value.
5. Build the package using `scripts/build_demo.py` with the pinned release commit and independently verify every public evidence hash and length.
6. Create `licensegate-demo-attribution-v1` with that JSON and a bounded future Unix deadline.
7. Run `review`, wait for the network FINALIZED status, then call `finalize` and wait for FINALIZED again.
8. Read `get_review`, record FINAL state, retrieval manifest, outcome and decision hash. Recompute the decision hash using `scripts/verify_decision.py`.
9. Save all deployment and demonstration receipts, exact state and source identity; push evidence/docs to main and verify the new head.

Live records are placed in `evidence/deployment.json` and referenced by EVIDENCE.md once confirmed. Never interpret an execution request or ACCEPTED receipt as verified network FINALIZED success.

Verified active deployment: `0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5`. See EVIDENCE.md and evidence/deployment.json for source identity, transaction hashes, final record and independent decision-hash verification. The final evidence commit retains identical deployed source bytes.

Re-read and verify (public read-only calls):
```sh
python scripts/read_review.py 0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5 licensegate-demo-attribution-v1 --sender 0xd215472bEC1a71f4cFe2f6e0F6e3A3C85d58aAd7
python scripts/verify_decision.py evidence/final-state.json 0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5
```
