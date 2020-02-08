# Generating Paintings using Generative Adversarial Networks
This is the repository for my Generation of Paintings using Generative Adversarial Networks Project at Imperial College London 

![samplegif_4fps](https://github.com/RajanPatel97/FYP/blob/master/Assets/samplegif_4fps.gif)

The repository has been designed such that experiments for each architecture are
self contained and are easily adaptable for any data-set. Each folder contains its
own set of instructions in their respective README.md files to run experiments.
It is important to note that many experiments run on different environments, some
require Python 2.7, others require Python 3.6, as well as different versions of CUDA
and cuDNN for compatibility reasons with older packages such as Torch. Thus, it is
important to modify your environments accordingly to ensure certain experiments
can be run. The repository contains nine folders:

* The ’Assets’ folder contains a small sample of generated images and gifs.
* The ’Clean Dataset’ folder contains code to clean the Xart data-set, which is
necessary to run so that certain images that are corrupted and cannot be read
by OpenCV Python package are removed.
* The ’DCGAN’, ’CDCGAN’, ’CAN’ and ’StackGAN’ folders contain the code
for experiments run on these respective architectures.
* The ’Embeddings’ folder contains two folders ’CHAR-CNN-RNN’ and ’SkipThought’ that each contain the code for experiments conducted on these methods. Trained models from these methods can then be used in the StackGAN
implementation.
* The ’Inception Score’ and ’FID Score’ folders contain the code to run these
quantitative measures.
* It is important to note that some files may take a long time to train and test,
sometimes over 3 weeks, thus saving weights and models every few epochs is
crucial.

## Datasets
The ArtImages data-set can be downloaded from this [link](https://imperialcollegelondon.box.com/s/fslnl56lrmv4o4ten7yeaspx4goxnqaj)

The WikiArt data-set can be downloaded from this [link](https://drive.google.com/file/d/182-pFiKvXPB25DbTfAYjJ6gDE-ZCRXz0/view)

*INSTRUCTIONS STILL NEED TO BE ADDED TO VARIOUS FOLDERS (OR YOU CAN FIGURE IT OUT) AND CERTAIN MODIFICATIONS NEED TO BE UPLOADED
