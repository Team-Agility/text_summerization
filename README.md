## ACL2018_AbsSumm

### Tested on

- Ubuntu 20.04
- Python 3.7

### Install Requirements

```
$ pip install -r requirements.txt 
$ wget -c https://objectstorage.ap-mumbai-1.oraclecloud.com/p/8cK15SZ-mySY2t5kymeO8WVGyDxncLEthJqip4nJGKJXNJMgdDdWn6ohkxMlrxjH/n/bm7noglpf2jq/b/FYP-Data/o/en-70k-0.2.lm.gz -O resources/en-70k-0.2.lm.gz
$ zcat resources/en-70k-0.2.lm.gz > resources/en-70k-0.2.lm
$ wget -c https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz -O resources/GoogleNews-vectors-negative300.bin.gz
```
### Utterance Community Detection

```
$ python utterance_community_detection.py
```

### test and evaluation on test set:
(with the best combination of parameters)
```
$ python multi_sentence_compression_single.py
$ python copy_ami_icsi_reference.py
$ python budgeted_submodular_maximization_single.py
```

### parameter tuning on development set:
```
$ python multi_sentence_compression_multiprocessing.py
$ python copy_ami_icsi_reference.py
$ python budgeted_submodular_maximization_multiprocessing.py
```

### Citation
```
Shang, G., Ding, W., Zhang, Z., Tixier, A. J. P., Meladianos, P., Vazirgiannis, M., & Lorre, J. P. (2018). Unsupervised Abstractive Meeting Summarization with Multi-Sentence Compression and Budgeted Submodular Maximization. arXiv preprint arXiv:1805.05271.

Boudin, F., & Morin, E. (2013, June). Keyphrase extraction for n-best reranking in multi-sentence compression. In North American Chapter of the Association for Computational Linguistics (NAACL).
```