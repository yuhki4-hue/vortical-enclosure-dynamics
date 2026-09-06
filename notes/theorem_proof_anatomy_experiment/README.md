# Theorem / Proof Anatomy Experiment Archive

> This directory contains the closed experimental record of a theorem/proof anatomy study.  
> It is not presented as a new proof theory or framework.

この directory は、theorem / proof anatomy 実験系列を、完結した研究記録として保存する archive です。完成理論を提示するものではなく、仮説、stress tests、counterexamples、失敗した枝、退役した語彙、証拠規律、最終的な停止判断を追跡できるように再配置しています。

## Status

- **closed research record**
- **not a theorem**
- **not a new proof theory**
- **not a new framework**
- **no claim of mathematical novelty**
- **negative results retained**

## What this archive records

- tool truth / identifiability をめぐる起源と、科学的 claim の監査
- 21定理を用いた theorem / proof anatomy v1.1
- claim correction history の proof-formation reconstruction
- finite propositional model による semantic stress
- record-frame branch と、その explicit `KILL`
- 当時の名称を保存した reachability stress と、同語彙の退役
- theoremhood、proof quotient、specification translation、cross-calculus pilots
- source architecture、source map、系列内 audit、final closure record

## Start here

1. [最終実験記録](./07_audit_and_closure/theorem_proof_anatomy_experiment_final_record_v1.0_ja.md)
2. [Source map](./07_audit_and_closure/theorem_proof_anatomy_experiment_source_map_v0.1_ja.md)
3. [Source architecture](./07_audit_and_closure/theorem_proof_anatomy_experiment_source_architecture_v0.1_ja.md)
4. [Internal audit](./07_audit_and_closure/theorem_proof_anatomy_full_series_independent_audit_v0.1.md)
5. [Original theorem / proof anatomy v1.1](./01_theorem_anatomy/theorem_proof_anatomy_v1.1_ja.md)

## Main outcome

> The strongest surviving methodological result is to match the form of evidence to the logical form of the claim.

たとえば、ある displayed proof の失敗、同じ theory での別 proof の存在、reduced theory からの non-derivability、setting の変更、proof translation の存在、quotient map の well-definedness、injectivity、surjectivity は、それぞれ別の主張であり、必要な証拠も異なります。

## Important limits

- mathematically new concept は得られていません。
- proof-formation の **L2 comparative utility は未実施**です。
- natural deduction と LJ の Pair B に関する global proof-class bijection は **NOT ESTABLISHED** です。
- “independent audit” は系列内の自己監査であり、external peer review ではありません。
- filenames に残る historical working terms は traceability のため保持しています。現在の technical vocabulary として復活させるものではありません。
- archive の83件という集計は series artifacts のみで、この README は含みません。

## Directory guide

| Directory | Contents |
|---|---|
| [`00_origin/`](./00_origin/) | tool truth、identifiability、scientific assurance、field controls、trajectory summary |
| [`01_theorem_anatomy/`](./01_theorem_anatomy/) | theorem / proof anatomy v1.1 と10 stress tests |
| [`02_proof_formation/`](./02_proof_formation/) | meta-experiment、frozen corpus、coder instructions、readers、adjudication |
| [`03_finite_propositional/`](./03_finite_propositional/) | finite propositional prototype、stress test、checkers、postmortem |
| [`04_record_frame/`](./04_record_frame/) | record-frame tests と各 checker |
| [`05_reachability_stress/`](./05_reachability_stress/) | 4 theorem stress tests、cross-test audit、retirement record |
| [`06_theorem_proof_pilots/`](./06_theorem_proof_pilots/) | theoremhood、minimality、quotient、specification change、cross-calculus pilots |
| [`07_audit_and_closure/`](./07_audit_and_closure/) | source architecture、source map、internal audit、final experimental record |

## Archive policy

既存の KILL / RETIRE / DOWNGRADE / OPEN / NOT ESTABLISHED を肯定結果へ書き換えません。checkers は encoded finite claims の確認に限られ、一般定理の代用ではありません。この archive を根拠に新しい pilot、v1.1 revision、または proof-theory expansion を開始することも意図していません。
