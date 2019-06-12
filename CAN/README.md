# Creative Adversarial Networks
An implementation of [CAN: Creative Adversarial Networks, Generating "Art" 
by Learning About Styles and Deviating from Style Norms](https://arxiv.org/abs/1706.07068) with a variation that improves sample variance and quality significantly.

Repo based on [DCGAN-tensorflow](https://github.com/carpedm20/DCGAN-tensorflow).

<!-- with modifications to reduce checkerboard artifacts according to [this --> 
<!-- distill article](https://distill.pub/2016/deconv-checkerboard/) -->

## Training a CAN model from scratch (architecture used in the paper)
```
bash experiments/train_can_paper.sh # must run from the root directory of the project
```
## Evaluating an existing CAN model
```
# make sure that load_dir acts correctly
bash experiments/eval_can_paper.sh
```
## Training ECAN
```
# make sure that `style_net_checkpoint` is set correctly, or you will error out
bash experiment/train_can_external_style.sh
```

## Training the (ImageNet pre-trained) Inception Resnet
```
cd slim/
vim finetune_inception_resnet_v2_on_wikiart.sh # edit INPUT_DATASET_DIR to match the location of where you downloaded wikiart
bash finetune_inception_resnet_v2_on_wikiart.sh
```
## Evaluating ECAN
```
# make sure that `style_net_checkpoint` and `load_dir` point to the downloaded models. 
bash eval_can_external_style.sh
```

## Experiments


## Authors of Original Repo 
[Phillip Kravtsov](https://github.com/phillip-kravtsov)

[Phillip Kuznetsov](https://github.com/philkuz)

## Citation

If you use this implementation in your own work please cite the following
```
@misc{2017cans,
  author = {Phillip Kravtsov and Phillip Kuznetsov},
  title = {Creative Adversarial Networks},
  year = {2017},
  howpublished = {\url{https://github.com/mlberkeley/Creative-Adversarial-Networks}},
  note = {commit xxxxxxx}
}
```
