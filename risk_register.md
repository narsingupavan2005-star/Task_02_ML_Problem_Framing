# Risk Register

| Risk | Possible Impact | Mitigation |
|---|---|---|
| Very small dataset | Poor generalization | Collect more representative data |
| Dataset imbalance | Some outcomes may be learned poorly | Monitor class-specific metrics |
| Data leakage | Unrealistically high performance | Verify feature availability before prediction |
| False positive | Customer incorrectly flagged | Human review |
| False negative | At-risk customer missed | Monitor recall and errors |
| Privacy exposure | Customer information disclosed | Restrict access and remove unnecessary identifiers |
| Model misuse | Prediction treated as certain | Use as decision support |