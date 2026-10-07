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

Live transaction links and final state are added here only after verification.
