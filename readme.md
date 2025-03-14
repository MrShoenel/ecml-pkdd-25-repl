# Replication Package: `From Lab to Factory: Pitfalls and Guidelines for Self- and Unsupervised Defect Detection on Low-Quality Industrial Images`

## Initialize Submodules and Install Environment

After cloning this repository, you need to initialize the submodules. Run:

```shell
git submodule update --init --recursive
```

Then, go ahead and restore the `conda` environment. The included file was tested under Ubuntu 24.04 LTS and Cuda 12.5.
The following command will create and activate the environment `ecml25repl`:

```shell
conda env create -f environment.yml
conda activate ecml25repl
```

# Notebooks and Scripts

This repository is a collection of Jupyter notebooks and scripts that allow to replicate our reported results.
Furthermore, the intention is to provide practitioners with usable scripts that help them to prepare their data, and to train and evaluate appropriate models.

Currently, we provide the following notebooks:

* [**`CS-Flow/Naive G-Link`**](./notebooks/cs-flow_naive-g-link.ipynb): This notebook replicates the results of naively applying CS-Flow to our coupling links dataset (the "G-Links").
* [**`CS-Flow/Masked G-Link`**](./notebooks/cs-flow_masked-g-link.ipynb): This notebook is similar to the previous one, but we test against a masked version of the G-Link dataset.
* [**`CS-Flow/Center-embedded G-Link`**](./notebooks/cs-flow_ce-g-link.ipynb): Similar to the previous notebook, but uses the "center-embedded" G-Link dataset.
* [**`CS-Flow/MVTec Cable`**](./notebooks/cs-flow_mvtec-cable.ipynb): In this notebook, we train a vanilla model against MVTec AD's cable category and check whether the model can handle rotated, but otherwise nominal, images.
* [**`CS-Flow/MVTec Cable Rotated`**](./notebooks/cs-flow_mvtec-cable.ipynb): Similar to the previous notebook, but we train on rotated images of cables, too.



Currently, we provide the following Scripts:

* [**`preprocess_sam.py`**](./src/repos/grounded_sam/preprocess_sam.py): A command-line application that uses GroundedSAM. Using a single text prompt, it can segment entire datasets.
* [**`preprocess_sam_with_masks.py`**](./src/repos/grounded_sam/preprocess_sam_with_masks.py): Like `process_sam.py`, but also saves foreground masks of the objects of interest.
* [**`main_ce-g-link_E.py`**](./src/repos/glass/main_ce-g-link_E.py): A configurable command-line script for training GLASS using own datasets, currently adapted for the champion-approach using the G-Link dataset.
