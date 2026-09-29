# ML Problem Framing & Responsible Data Card

## 1. ML Problem Framing

### Decision
The business wants to identify customers who may churn so that appropriate customer-retention actions can be considered.

### Prediction Target
Predict whether a customer will churn.

Target variable:
churned

0 = Customer did not churn
1 = Customer churned

### Unit of Observation
One row represents one customer.

### Action Window
The model output can be used to identify customers who may need attention during the defined retention period.

### Non-ML Baseline
Before using ML, compare against a simple rule-based approach, such as flagging customers with high recent inactivity and/or multiple support tickets.

### Is ML Justified?
ML can be explored as a decision-support tool because several customer attributes may be related to churn. However, the available dataset is very small, so model results should not be treated as reliable evidence for real-world deployment without additional representative data and validation.

## Baseline Result

A simple rule-based baseline was implemented using:
- last_login_days > 10, OR
- support_tickets >= 3

The baseline was evaluated on the supplied 12-row dataset.

Baseline Accuracy: 1.00 (100%)

Important limitation: this is an in-sample baseline result on a very small dataset and should not be interpreted as evidence of real-world model performance. A separate validation/test dataset and additional representative data would be required before deployment.