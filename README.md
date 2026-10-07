# LicenseGate

Consensus-backed review of open-source release compatibility against an immutable technical distribution policy.

**LicenseGate is a technical policy tool, not legal advice. It does not make legally binding determinations.** Do not treat a CLEAR result as a legal opinion, warranty, or assurance about the completeness of a release's supply chain.

## Why GenLayer is central

Ordinary deterministic contracts can check addresses, hashes, sizes and deadlines, but cannot interpret license language against a release's intended distribution model and natural-language policy. LicenseGate uses GenLayer validator web retrieval and LLM execution for that interpretation. Each semantic validator fetches the evidence itself, independently performs the assessment, checks objective fingerprints and decision fields, and compares the complete obligations and reasoning. The accepted decision is stored by the Intelligent Contract; an off-chain service cannot submit its own authoritative verdict.

No website, external wallet connection, user account system, backend, database, token economics or payments are included. Use GenLayer Studio's supplied development accounts to write; any RPC client can read finalized records.

## Protocol

`create_review(review_id, package_json, deadline)` atomically enters EVIDENCE_LOCKED. There is no mutable OPEN drafting phase. The maintainer cannot replace the policy, evidence, identity or dependencies. Duplicate IDs and repeat reviews for the same maintainer/repository/commit/artifact are rejected.

`review(review_id)` is maintainer-only and permitted through the deadline, inclusive. Objective retrieval manifests are agreed with strict equality. If any file cannot be authenticated or its release manifest does not match, the result is INCONCLUSIVE without asking an LLM to salvage it. Otherwise, leader and validators independently fetch and interpret the authenticated documents. Validators must agree on fingerprints, overall and per-dependency outcomes; valid citations and the substantive obligations and reasoning must be semantically equivalent. Invalid structured model output becomes INCONCLUSIVE. A network unable to agree does not advance the record.

`finalize(review_id)` is permissionless after REVIEWED, or strictly after the deadline for a still locked review. Expired unreviewed records finalize as INCONCLUSIVE. FINAL is terminal. These application states are separate from the network transaction status: confirm the transaction is FINALIZED before reporting its state as a live proof. There are no application appeals; the chain's own consensus lifecycle still applies.

Each record stores owner, exact package, policy hash, dependency hash, authenticated retrieval manifest, structured result, quality score, deterministic timestamps and append-only state history. Final SHA-256 binds the complete record with an empty decision_hash placeholder plus protocol name, contract address and chain ID. This includes the release identity, full repository commit, citations and finalization time. See `scripts/verify_decision.py`.

## Evidence and release identity

The package fields are documented by `scripts/build_demo.py` and the committed demonstration package. Every dependency has an ID, name, exact version, repository, full 40-character lowercase commit and a license evidence ID. Evidence has ID, role, canonical HTTPS URL, expected SHA-256 and exact byte length. Only full-commit-pinned `raw.githubusercontent.com/owner/repo/<40 hex>/path` is supported. Mutable branches/tags, abbreviated SHAs, query strings, credentials, fragments, ports, encoded paths and traversal are rejected.

PROJECT_LICENSE and RELEASE_MANIFEST must come from the release repository and commit. DISTRIBUTION documents must also be release-bound. Dependency LICENSE sources must match the dependency repository and commit. NOTICE sources must belong to the release or a committed dependency. Evidence roles: PROJECT_LICENSE, RELEASE_MANIFEST, DEPENDENCY_LICENSE, NOTICE, DISTRIBUTION.

RELEASE_MANIFEST is an exact JSON object with project, release, repository, artifact, declared_license, distribution and dependencies matching the package. Its own commit is authenticated by its URL: writing its own future commit into its contents would be circular. It is parsed and compared deterministically before semantic assessment. The manifest and project LICENSE are release-bound even when dependency licenses come from earlier commits.

Bounds: 1–8 dependencies; 3–20 evidence files; 24,000 bytes/file; 96,000 committed bytes total; 20,000-byte package; policy up to 4,000 characters; deadline 60 seconds to 30 days ahead. UTF-8 text only. Authentication score is the integer percentage of evidence entries that are AUTHENTICATED, not model confidence or a legal-risk score. A score of 100 alone does not imply CLEAR.

## Distribution models

| Value | Meaning |
| --- | --- |
| SOURCE | Source distribution |
| BINARY | Compiled binary distribution |
| LINKED | Library/application linkage |
| MODIFIED | Modified redistribution |
| SAAS | Hosted use |

The interpretation must respect the selected model; hosted use and redistribution cannot be assumed equivalent.

## Outcomes

| Outcome | Required basis |
| --- | --- |
| CLEAR | Authenticated evidence affirmatively establishes the policy and obligations are satisfied |
| ACTION_REQUIRED | Concrete missing actions, such as copyright/permission notices, attribution, source offers or disclosures |
| BLOCKED | Authenticated material incompatibility with the locked release policy |
| INCONCLUSIVE | Missing, unavailable, contradictory, changed, invalid or unsupported evidence/assessment |

Per-dependency results contain obligations, missing_actions, incompatibilities and citations. Every assessed dependency must cite its committed license evidence. Overall precedence is INCONCLUSIVE, then BLOCKED, then ACTION_REQUIRED, then CLEAR, so uncertainty cannot become a safe-looking result.

## Trust boundary and limitations

Hashes prove fetched bytes match a caller's commitments; they do not prove publisher identity, repository ownership, upstream authenticity or dependency completeness. A version-pinned fork can still contain misleading material. Reviewers must inspect source provenance. Release manifests and artifact documentation are maintainer attestations: LicenseGate does not download, build, reverse-engineer or independently inspect a binary, and it cannot detect undisclosed dependencies. The artifact field is an identifier, not a verified artifact content hash. The examples are clearly synthetic fixtures, not audits of real distributed binaries.

All fetched material and caller policy text are untrusted prompt data. Fixed protocol instructions prohibit following embedded instructions and require evidence-only judgment. Prompt isolation, independent model assessment, bounded outputs and citation checks reduce injection risk but do not guarantee model correctness or adversarial robustness. Local mocked tests do not prove real-model injection resistance. No owner, model or API is allowed to change deterministic permissions, deadlines or state transitions.

Unavailable evidence can differ between validators. Strict disagreement or changes between retrieval stages can leave a transaction undetermined/reverted rather than record INCONCLUSIVE. The deterministic expiry path remains available. Evidence caps bound accepted data and prompts, but the SDK's web API does not offer a response streaming cap: transport may fetch an oversized response before the contract rejects it.

All public methods and constructor are nonpayable. There are no rewards, escrow or accepted fund paths; copied evidence provides no reward to steal. Replaying the same bytes from a different maintainer creates a distinct address-bound review, never overwrites the original. Forced transfers outside this API are not a supported funding mechanism.

## Run checks

Python 3.12+:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
genvm-lint check contracts/licensegate.py
```

The suite uses official `genlayer-test` Direct Mode and the actual pinned SDK. SDK v0.2.16 contains the contract's dependency runner. A small test-only adapter executes strict equality's sandbox callback in-process because Direct Mode does not isolate that Sandbox transport. It preserves the SDK Return wrapper and tests independent re-fetch and disagreement; it does not simulate network finality. Live Full Consensus is separate. GenVM lint/SDK validation verifies the canonical source and ABI; CI repeats lint and tests.

## Deployment and proof

See [DEPLOYMENT.md](DEPLOYMENT.md), [EVIDENCE.md](EVIDENCE.md), [SECURITY.md](SECURITY.md) and `evidence/`. Always deploy the pushed canonical source bytes and record source SHA-256 and source commit. Studionet is a hosted development network with temporary state; durable repository evidence is necessary. The source dependency is pinned and uses current namespaced APIs verified against the actual SDK.

Recommended submission classification: AI & Agents; Verifiable Inference; Developer Tools (use the closest available portal tags).

Verified live proof: [active contract](https://explorer-studio.genlayer.com/address/0x866Be66A0Ff5998c3bc858f3766c2802e2c447a5), FINAL / ACTION_REQUIRED, four authenticated evidence files, Full Consensus MAJORITY_AGREE. All 76 local tests and GenVM lint/SDK validation passed. Exact receipts, final state, recomputable digest and source-byte comparison are documented in [EVIDENCE.md](EVIDENCE.md). See [SUBMISSION.md](SUBMISSION.md) for submission-ready fields.
