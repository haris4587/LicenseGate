# Review evidence

This demonstration uses synthetic MIT-license fixtures and a release inventory explicitly missing copyright/permission notices. It is designed to yield ACTION_REQUIRED. It makes no assertion about an actual production binary or legal compliance.

Dependency fixture commit: `80b4310c14f0b4a1e07f366889260c9eb48ae5d4`.

- https://raw.githubusercontent.com/haris4587/LicenseGate/80b4310c14f0b4a1e07f366889260c9eb48ae5d4/fixtures/MIT-LICENSE.txt
- The release-bound project license, exact release manifest and distribution inventory are pinned by `scripts/build_demo.py` and saved in `evidence/demo-package.json` after publication.

Local tests use mocked web/LLM responses and the official SDK. They cover deterministic permissions, evidence authentication, lifecycle, schema and validator disagreement. They do not establish actual model accuracy, prompt-injection immunity or network consensus. XML test results and the canonical contract ABI are in evidence/.

Current official references checked during implementation:
- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- https://docs.genlayer.com/developers/intelligent-contracts/features/transaction-context
- https://docs.genlayer.com/developers/intelligent-contracts/testing
- https://docs.genlayer.com/api-references/genlayer-linter
- https://docs.genlayer.com/developers/networks
- https://sdk.genlayer.com/

The web-access guide contains examples using status_code; the pinned SDK's actual `genlayer.gl.nondet.web.Response` has `status`, `headers` and `body`. The implementation and tests use the declared `status` field. The exact SDK runner is pinned in the canonical source header. `gl.vm.UserError`, `gl.vm.run_nondet_unsafe`, `gl.eq_principle.strict_eq`, `gl.nondet.web.get`, `gl.nondet.exec_prompt(response_format='json')`, `gl.message.sender_address` and the transaction-pinned UTC clock were checked against the SDK and GenVM validation.



## Verified live demonstration — 2026-10-07

Active contract: `0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5` ([Explorer](https://explorer-studio.genlayer.com/address/0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5)). Stable Studionet chain 61999; Studio-provided account; zero value; NORMAL/Full Consensus, not simulation or leader-only.

Deployed source commit: `4a1a47ea374d1d54608809641f4c8aaf082e524f`. Canonical `contracts/licensegate.py` SHA-256: `b7cf829c0ebf7da75d15e8ceb279c9f0683dbbfdb292eb95f9d4bb319225dca7` (18143 bytes). The deployment receipt's actual `contract_code` bytes were decoded and compared with the canonical file, not inferred from an editor filename. The source is unchanged in the final evidence commit.

| Operation | Finalized transaction |
| --- | --- |
| deployment | [0x57b33966ea14305028b9631245fb49146c84aa03a3979cb250fe29c249966a93](https://explorer-studio.genlayer.com/tx/0x57b33966ea14305028b9631245fb49146c84aa03a3979cb250fe29c249966a93) |
| creation | [0x3b81b851d85f178469f59707231bf62c4ef191106755aaa19839c5188a4add27](https://explorer-studio.genlayer.com/tx/0x3b81b851d85f178469f59707231bf62c4ef191106755aaa19839c5188a4add27) |
| adjudication | [0x8ae2df79a3ed562dcdae7ea202d884c2e91378ce46defb1e65011d227a116fbb](https://explorer-studio.genlayer.com/tx/0x8ae2df79a3ed562dcdae7ea202d884c2e91378ce46defb1e65011d227a116fbb) |
| finalization | [0xec1c6e6d2ef5ef0e8902f55e6e4c86df842de67c86d3de7176d172991fbc56ec](https://explorer-studio.genlayer.com/tx/0xec1c6e6d2ef5ef0e8902f55e6e4c86df842de67c86d3de7176d172991fbc56ec) |

Review `licensegate-demo-attribution-v1` is FINAL with ACTION_REQUIRED. All four evidence entries are AUTHENTICATED, quality score 100. The missing actions are to ship the full demo-lib MIT copyright/permission notice and include the dependency notice/license file in the synthetic binary package. No material incompatibility was reported.

Adjudication receipt: FINALIZED, SUCCESS, MAJORITY_AGREE, zero rotations, five initial validators. Final votes include three AGREE, one DISAGREE, one IDLE; this is majority agreement, not unanimity. Creation, deployment and application finalization also finalized successfully. The application decision hash was independently recomputed and matched: `dfcb89e3bffad2d5a8d6c74a0e7a9f1deb8bbbdc0df8c6d74969e9799dcd7c6d`.

The exact final record is `evidence/final-state.json`; public receipts are deployment-transaction.json, create-review-transaction.json, adjudication-transaction.json and finalization-transaction.json. `evidence/deployment.json` binds these records to the source commit/hash; `evidence/live-explorer-proof.jpg` captures all four FINALIZED successful transactions. `evidence/reviewed-state.json` records the preceding REVIEWED state.

### Public authenticated inputs

- project-license: https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/PROJECT-LICENSE.txt — 1090 bytes, SHA-256 `17b7fd84b25865de28cfb2fa5921de1e88c73702240023948a901178e3c3c7f1`.
- manifest: https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/release-manifest.json — 453 bytes, SHA-256 `854808a99f2e47054cea395217fc509adba0b04e6396bb5e093fff1fbe8d28b7`.
- distribution: https://raw.githubusercontent.com/haris4587/LicenseGate/bf9516033695cf2c5002bb0d32b6692754313bf2/fixtures/distribution-missing-attribution.txt — 621 bytes, SHA-256 `1ec43be1f165411b6aba3e101d19731a28efb0c92386bd2ccf285defbbe68ea4`.
- dep-license: https://raw.githubusercontent.com/haris4587/LicenseGate/80b4310c14f0b4a1e07f366889260c9eb48ae5d4/fixtures/MIT-LICENSE.txt — 1090 bytes, SHA-256 `17b7fd84b25865de28cfb2fa5921de1e88c73702240023948a901178e3c3c7f1`.

Release fixture source is the earlier immutable release commit bf9516033695cf2c5002bb0d32b6692754313bf2; the Intelligent Contract was deployed from corrected source commit 4a1a47ea374d1d54608809641f4c8aaf082e524f. These are different identities for different purposes.

### Superseded attempts

The first deployed version at 0x888e71C12439Caf60b5996Cd1Cfb8A10F1D7e4e8 compared citation subsets exactly. Although live leaders agreed on ACTION_REQUIRED, independently valid citation subsets differed and consensus became UNDETERMINED. The corrected source preserves exact evidence/outcome checks, rejects fabricated citations and compares valid citation sets semantically with their supporting evidence. Regression tests cover that distinction. `superseded-review-attempt.json` and `superseded-deployment-transaction.json` preserve the failed attempt; its eventual network lifecycle FINALIZED status does not establish successful adjudication.

A duplicate-name Studio import then deployed the old editor contents to 0x07D7bAa3C45041311B73B4851C111c1d72Adcacb. Deployment source-byte verification detected the mismatch. That deployment and its locked state are explicitly marked superseded. Importing a distinct filename with the exact corrected bytes produced the active instance above; its source identity was verified before live review. No superseded address is the canonical deployment.

Final local run: 76 tests passed, no failures, 3.05 seconds. GenVM lint's three checks and SDK validation passed; the linter reports a newer runner exists, but the explicitly pinned runner validated. Local SDK tests mock web/model responses and do not establish model accuracy or consensus. The live receipt independently establishes this one successful Full Consensus example.
