This repository contains two Python scripts to cluster faculty members based on tags for papers available on arXiv:

* hierarchical-clustering.py: Uses hierarchical clustering based on the Jaccard similarity between tag lists.

* clusters-by-frequency.py: Clusters faculty members based on their most frequent tags.

names.txt has the input list of faculty members. It's best if this list has names in the same format as they appear on arXiv. Even then, there may be multiple people with the same name on arXiv, or some faculty members have no preprints available on arxiv, in which case this script does not work well.

To install the required libraries, run:

```bash
pip install requests arxiv fuzzywuzzy scipy numpy matplotlib scikit-learn
```

The output clusters for clusters-by-frequency.py will look like this: 

```
Cluster math.NT:
Kevin Ford, Scott  Ahlgren, Alexandru Zaharescu, Florin P. Boca, Jesse Thorner, Bruce  Reznick

Cluster math.AP:
Jeremy Tyson, M. Burak Erdoğan, Vera Mikyoung Hur, Jared  Bronski, Eduard-Wilhelm Kirr, Nikolaos Tzirakis, Richard S. Laugesen, Daniel B. Cooney

Cluster math.AG:
Sheldon Katz , Christopher  Dodd, Steven  Bradlow, William  Haboush, Jeremiah  Heller, Felix Janda, S. P. Dutta

Cluster math.DG:
Pierre Albin, Rui Loja Fernandes, Eugene M.  Lerman, Pei-Kun Hung, Anil N. Hirani, Gabriele La Nave

Cluster math.GT:
Nathan M.  Dunfield, Rosemary Guzman, Jacob Rasmussen, Sarah Dean Rasmussen

Cluster math.CO:
Alexandr  Kostochka, Alexander  Yong, Jozsef Balogh, Yuliy Baryshnikov

Cluster math.MP:
Rinat Kedem, Kay  Kirkpatrick, Philippe Di Francesco, Amanda Young

Cluster math.PR:
Renming Song, Richard B. Sowers, Partha S. Dey, Xuan Wu, Runhuan Feng, Tolulope Fadina

Cluster cs.IT:
Iwan Duursma, Felix Leditzky, Yuan Liu

Cluster math.AT:
Randy McCarthy, Charles  Rezk, Vesna Stojanoska, Matthew Ando, Daniel Berwick-Evans

Cluster math.SG:
Susan Tolman, James Pascaleff, Ely Kerman

Cluster math.FA:
Denka  Kutzarova, Timur Oikhberg, Marius Junge

Cluster math.DS:
Lee DeVille, Vadim Zharnitsky

Cluster math.MG:
Igor G. Nikolaev, Igor Mineyev, Aimo  Hinkkanen

Cluster cond-mat.mtrl:
Xiaochen Jing

Cluster stat.AP:
Zhiyu Quan

Cluster q-bio.PE:
Zoi Rapti

```

The output of hierarchical-clustering.py is a dendrogram saved in the output folder.
