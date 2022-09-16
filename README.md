# Reward Penalty Based Weighted Ensemble Approach for Multimodal Data Stream Classification

# This work is published in : `International Journal of Neural Systems`
# `Full paper link:` https://www.worldscientific.com/doi/10.1142/S0129065722500496

# Research Goal:

The majority voting is the simplest ensemble approach where it considers that each classifier in the ensemble set has equal priority. In contrast, heterogeneous weights are assigned to each classifier in the weighted majority. The weighted majority voting is in itself more complex than simple majority voting due to the use of weights for the corresponding classifier. It improves the accuracy of classification without increasing the complexity of the ensemble classifier as a whole. Based on the classifier's performance, the weights are adjusted, which means the weights are decreased every time the classifier predicts the wrong class. 

- `RQ1:` How does classification performance improve if a weight penalty is applied to the classifier that predicts the incorrect class and a weight increment (reward) is applied to the classifier that predicts the correct class?

- `RQ2:` How can the constant factor (_beta_) be adjusted automatically based on the classifier's performance?

- `RQ3:` Does the predictive performance of the RPWE outperform selected state-of-the-art methods?

The aim of this research study is to develop a **Reward-Penalty Based Weighted Ensemble (RPWE)** for emotion state classification using multi-modal physiological data streams. In RPWE, the weights are increased and decreased based on the classifiers performance; if the classifier is performing well (classifying correct classes) then it will be be rewarded (increasing weights means increasing priority) by the reward-penalty factor (called _beta_). On the other hand, if the classifier performs poorly (classifying the wrong classes) it will be penalized  by the reward-penalty factor. The _beta_ is adjusted automatically based on the classifiers' performance.

**DATASET** : `DEAP` and `AMIGOS` dataset is required. To download `DEAP dataset` click on : https://www.eecs.qmul.ac.uk/mmv/datasets/deap/download.html




**DATA Rearrangement required**
```diff
- CAUTION

+ The DEAP data needs a simple rearrangement to work with the code. 

@@  Check the `data_rearrangements` folder for the  DEAP  data rearrangement from the .dat or .mat file from the DEAP dataset. @@
@@ Then follow the follwoing steps. @@

```

- Programming language
  - `Python 3.6`

- Operating system
  - `Ubuntu 18.04 (64 bit)` 


## NOTE*: Please feel free to use the code by giving proper citation and star to this repository.

# Cite this work: 
    @article{doi:10.1142/S0129065722500496,
		author = {Nandi, Arijit and Xhafa, Fatos and Subirats, Laia and Fort, Santi},
		title = {Reward-Penalty Weighted Ensemble for Emotion State Classification from Multi-modal Data Streams},
		journal = {International Journal of Neural Systems},
		volume = {0},
		number = {ja},
		pages = {null},
		year = {0},
		doi = {10.1142/S0129065722500496},
		URL = {https://doi.org/10.1142/S0129065722500496},
		eprint = {https://doi.org/10.1142/S0129065722500496}
	}



## 📝 License
Copyright © [Arijit](https://github.com/officialarijit).
This project is MIT licensed.
