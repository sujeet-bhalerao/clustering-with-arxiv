This repository contains two Python scripts to cluster faculty members based on tags for papers available on arXiv:

* hierarchical-clustering.py: Uses hierarchical clustering based on the Jaccard similarity between tag lists.

* clusters-by-frequency.py: Clusters faculty members based on their most frequent tags.

names.txt has the input list of faculty members. It's best if this list has names in the same format as they appear on arXiv.

The output clusters for clusters-by-frequency.py will look like this: 

```
Cluster math.NT:
Kevin Ford, Scott  Ahlgren, Alexandru Zaharescu, Florin P. Boca, Jesse Thorner, Bruce  Reznick

Cluster math.AP:
Jeremy Tyson, M. Burak Erdoğan, Vera Mikyoung Hur, Jared  Bronski, Eduard-Wilhelm Kirr, Nikolaos Tzirakis, Richard S. Laugesen

Cluster math.AG:
Sheldon Katz , Christopher  Dodd, Steven  Bradlow, William  Haboush, Jeremiah  Heller, S. P. Dutta

Cluster math.DG:
Pierre Albin, Rui Loja Fernandes, Eugene M.  Lerman, Anil N. Hirani, Gabriele La Nave

Cluster math.GT:
Nathan M.  Dunfield, Rosemary Guzman

Cluster math.CO:
Alexandr  Kostochka, Alexander  Yong, Jozsef Balogh, Yuliy Baryshnikov

Cluster math.MP:
Rinat Kedem, Kay  Kirkpatrick, Philippe Di Francesco, Zoi Rapti

Cluster math.PR:
Renming Song, Richard B. Sowers, Partha S. Dey, Runhuan Feng

Cluster cs.IT:
Iwan Duursma, Felix Leditzky

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

```