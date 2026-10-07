# Security properties and review

**Technical policy assessment only; not legal advice or legally binding.**

| Threat | Control | Remaining boundary |
| --- | --- | --- |
| Mutable references/SSRF/credential URLs | Narrow raw GitHub HTTPS allowlist, exact full commits and canonical path grammar | GitHub availability; redirects are handled by SDK and final bytes must authenticate |
| Misbound dependency or release | Deterministic repository/commit checks and exact release manifest comparison | Publisher identity and completeness require human provenance review |
| Changed content | SHA-256 and byte length, strict-equality retrieval manifest; semantic-stage refetch must match | Divergent retrieval may prevent network agreement |
| Unavailable or invalid UTF-8 | Explicit status and INCONCLUSIVE, no partial favorable result | Retry by protocol is not an endless application appeal |
| Large inputs | Counts, per-file and total committed bytes, bounded policy/package/results | Web transport itself cannot be streaming-limited by this SDK |
| Leader-only verification | Every semantic validator reruns fetch and interpretation; fingerprints and stable decisions equal; prose equivalent | Model/provider quality and consensus assumptions |
| Injection in files or caller policy | All inputs declared DATA under fixed evidence-only instructions; independent assessment and schema checks | No claim of perfect injection resistance |
| Fabricated citations/favorable omissions | IDs must exist; each dependency cites license; all dependency IDs required; outcome consistency | Semantic checks establish actual relevance, not schema alone |
| Front-running/replay | No economic reward; records owner-bound, IDs unique, same owner/release/artifact replay rejected | Other maintainers may review the same public release |
| Late changes/repeated settlement | Immutable locked package, one review, inclusive review deadline, strictly later expiry, terminal FINAL | Network execution time is the transaction timestamp |
| Stuck funds | Constructor and methods nonpayable; no balances or transfers | Forced transfers are outside the supported protocol |

Decision digest uses canonical ASCII JSON, sorted keys and compact separators. Hashing empty `decision_hash` avoids self-reference and chain/contract domain separation prevents reusing a final digest across deployments. History only appends creation, review and final events and contains no mutable evidence replacement.

Review checklist performed: source roles and version binding, count/size checks, address permissions, deadline boundaries, replay guard, no storage writes inside nondeterministic callbacks, strict fingerprints, independent model interpretation, schema/citation/aggregate validation, nonpayable ABI and terminal-state checks. This is a development review, not an independent security audit.

Report issues privately to the repository owner through the contact method in their GitHub profile; do not post credentials or private license material in public issues. LicenseGate only accepts public evidence.
