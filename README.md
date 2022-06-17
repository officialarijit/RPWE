# Reward Penalty Based Weighted Ensemble approach for multimodal data stream classification

# Research Goal:

The majority voting is the simplest ensemble approach where it considers that each classifier in the ensemble set has equal priority. In contrast, heterogeneous weights are assigned to each classifier in the weighted majority. The weighted majority voting is in itself more complex than simple majority voting due to the use of weights for the corresponding classifier. It improves the accuracy of classification without increasing the complexity of the ensemble classifier as a whole. Based on the classifier's performance, the weights are adjusted, which means the weights are decreased every time the classifier predicts the wrong class. 

- `RQ1:` How does classification performance improve if a weight penalty is applied to the classifier that predicts the incorrect class and a weight increment (reward) is applied to the classifier that predicts the correct class?

- `RQ2:` How can the constant factor (_beta_) be adjusted automatically based on the classifier's performance?

- `RQ3:` Does the predictive performance of the RPWE outperform selected state-of-the-art methods?

The aim of this research study is to develop a **Reward-Penalty Based Weighted Ensemble (RPWE)** for emotion state classification using multi-modal physiological data streams. In RPWE, the weights are increased and decreased based on the classifiers performance; if the classifier is performing well (classifying correct classes) then it will be be rewarded (increasing weights means increasing priority) by the reward-penalty factor (called _beta_). On the other hand, if the classifier performs poorly (classifying the wrong classes) it will be penalized  by the reward-penalty factor. The _beta_ is adjusted automatically based on the classifiers' performance.

# NOTE*: Please feel free to use the code by giving proper citation and star to this repository.

## 📝 License
Copyright © [Arijit](https://github.com/officialarijit).
This project is MIT licensed.
