# LicenseGate submission

## 1. Project name

LicenseGate

## 2. One-line description

Consensus-backed open-source release compatibility review against an immutable technical distribution policy.

## 3. Full description

LicenseGate locks an exact software release, repository commit, artifact identifier, distribution model, natural-language policy and bounded dependency/evidence package. GenLayer validators independently retrieve full-commit-pinned public documents, authenticate SHA-256 and byte length, and interpret license obligations against the locked policy. Deterministic rules govern authorization, replay protection, deadlines, immutable state and final decision hashing. Results are CLEAR, ACTION_REQUIRED, BLOCKED or INCONCLUSIVE with per-dependency obligations, missing actions, incompatibilities, citations and an authenticated retrieval manifest. This is a technical policy tool, not legal advice or a legally binding determination. It assesses supplied evidence and does not establish publisher identity or dependency completeness.

## 4. Recommended tags

AI & Agents; Verifiable Inference; Developer Tools — choose the closest available submission portal tags.

## 5. GitHub repository

https://github.com/haris4587/LicenseGate

## 6. Active contract address

0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5

## 7. Explorer contract link

https://explorer-studio.genlayer.com/address/0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5

## 8. Deployment transaction

0x57b33966ea14305028b9631245fb49146c84aa03a3979cb250fe29c249966a93

## 9. Full Consensus demonstration transaction

0x8ae2df79a3ed562dcdae7ea202d884c2e91378ce46defb1e65011d227a116fbb

## 10. Final deployed source commit

4a1a47ea374d1d54608809641f4c8aaf082e524f

## 11. Contract SHA-256

b7cf829c0ebf7da75d15e8ceb279c9f0683dbbfdb292eb95f9d4bb319225dca7

## 12. Local test results

76 passed, 0 failed (3.05 seconds); GenVM lint 3 checks passed; SDK validation passed. CI on deployed source commit passed: https://github.com/haris4587/LicenseGate/actions/runs/37633934940. XML and validation records are committed.

## 13. Live test result

FINAL / ACTION_REQUIRED; all four files AUTHENTICATED; quality score 100; adjudication FINALIZED / MAJORITY_AGREE / NORMAL, zero rotations. Application finalization transaction 0xec1c6e6d2ef5ef0e8902f55e6e4c86df842de67c86d3de7176d172991fbc56ec. Decision hash independently verified: dfcb89e3bffad2d5a8d6c74a0e7a9f1deb8bbbdc0df8c6d74969e9799dcd7c6d. Majority agreement is not unanimity.

## 14. Evidence URLs

- https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/PROJECT-LICENSE.txt
- https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/release-manifest.json
- https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/distribution-missing-attribution.txt
- https://raw.githubusercontent.com/haris4587/LicenseGate/80b4310c14f0b4a1e07f366889260c9eb48ae5d4/fixtures/MIT-LICENSE.txt

## 15. Why GenLayer is central

Hashes, access control and deadlines are deterministic; interpreting natural-language license obligations against a distribution model and policy is semantic. GenLayer executes authenticated web retrieval and independent validator interpretation inside the Intelligent Contract consensus workflow. Validators assess evidence themselves rather than approving an externally supplied verdict.

## 16. Final GitHub commit

The commit containing this submission and final evidence; obtain with git log -1 --format=%H -- SUBMISSION.md. The exact SHA is provided in the completion response. A commit cannot embed its own SHA.

## 17. Important files pushed

contracts/licensegate.py; tests/test_licensegate.py; fixtures/MIT-LICENSE.txt, PROJECT-LICENSE.txt, release-manifest.json, distribution-missing-attribution.txt; README.md; SECURITY.md; DEPLOYMENT.md; EVIDENCE.md; SUBMISSION.md; scripts/build_demo.py, read_review.py, capture_receipt.py, verify_decision.py; evidence/demo-package.json, deployment.json, final-state.json, reviewed-state.json, deployment-transaction.json, create-review-transaction.json, adjudication-transaction.json, finalization-transaction.json, live-explorer-proof.jpg, local-tests.xml, local-validation.txt, contract-schema.json, superseded attempt records; .github/workflows/tests.yml; requirements-dev.txt; pytest.ini; LICENSE; .gitignore.
