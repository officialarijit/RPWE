# Reward Penalty Based Weighted Ensemble approach for multimodal data stream classification

# Research Goal:

The majority voting is the simplest ensemble approach where it considers that each classifier in ensemble set has equal priority, whereas in weighted majority a heterogeneous weights are assigned to each classifier. The weighted majority voting is more complex ensemble where in the beginning each classifier is given equal weights but based on the classifiers performance the weights are adjusted, means the weights are decreased every time the classifier predicts wrong class.  

 - Can the classification performance improve if the weight penalty happens for the classifier that predicts the wrong class and the classifier's weight increment (reward) in case of correct class prediction?

 - Can the constant factor (_beta_) be adjusted automatically based on the classifier's performance?

The aim of this research study is to develop a **Reward-Penalty Based Weighted Ensemble (RPWE)** for emotion state classification using multi-modal physiological data streams. In RPWE, the weights are increased and decreased based on the classifiers performance; if the classifier is performing good (classifying correct classes) then it will be be rewarded (increasing weights means increasing priority) by the reward-penalty factor (called _beta_). On the other side, if the classifier performs bad (classifying wrong classes) it will be penalized  by the reward-penalty factor. The _beta_ is adjusted automatically based on the classifiers' performance.

# NOTE*: Please feel free to use the code by giving proper citation and star to this repository.

## 📝 License
Copyright © [Arijit](https://github.com/officialarijit).
This project is MIT licensed.
