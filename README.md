# surprising-facts
This is the repository for the paper "Identifying Surprising Facts in Wikidata" (TODO - update name if you choose somethign else, and add link once available).

## Notes to Filip / Hayden
I've marked where updates need to be made to add Hayden's automl method in `survey_surprise_task.ipynb` and `quiz_surprise_task.ipynb` with "hayden-todo", so you should be able to cmd-f for where to make changes.

Results for the surprise scores given by each method as well as the correlation scores for each method are saved under `/output/`.

TODO
I've gathered resources into a folder and specified their location below in the instructions. Aside from the random walk embeddings, everything is in a folder that is accessible only to kgtk/similarity people. The folder should be moved to a publicly available location, and the link in the instructions below should be updated.



## Steps for reproducing results
1. Install the required packages:
    * tqdm (`pip install tqdm`)
    * gensim (`pip install gensim`)
    * kgtk (follow documentation here: https://kgtk.readthedocs.io/en/latest/install/)
2. Download the following resources:
    * Random walk embeddings are avalable [here](https://drive.google.com/drive/folders/1XE7w29_kr7yeEMuSDJbBifcR3iGuawd_?usp=sharing)
        * For each random walk embedding model you want to use, both the `.kv` and `.kv.vectors.npy` file need to be downloaded. For simplicity, you can download the whole folder.
    * All other resources are available [here](https://drive.google.com/drive/folders/16f6xgcqciJprB8PUYZsTvfyazSJTpgMN?usp=sharing)
        * text, complex, transe, p-complex, and p-transe embeddings
        * benchmark data
            * These are also saved on github.
        * subset of wikidata edges about humans
            * alternatively, these can be created by following instructions in `create_q5_wd_subset.ipynb`
        * subset of wikidata edges about english labels
        * entity profile labels files
            * These are abstractions of information in WD, created by previous work ["Generating Explainable Abstractions for Wikidata Entities"](https://dl.acm.org/doi/10.1145/3460210.3493580). You can instead use the files directly created by that work, however the files we provide in the above resources folder have been filtered down to a smaller set of rows that are needed for this work. To use the original unfiltered files, use [this file](https://drive.google.com/file/d/19MKQs6Ua0hI_JXfOCPJax3ZLPhVXNfkk/view?usp=sharing) (60MB) instead of `profile_labels_info_joined.RELs_and_AILs.tsv` and [this file](https://drive.google.com/file/d/1zf3gywzOF4apFgNs86SEqdsw8H5QKJ8M/view?usp=sharing) (56GB) with an extra step of shuffling the rows instead of `entity_profile_labels.RELs_and_AILs.shuffled.tsv`.
3. Reproducing results for the survey benchmark:
    * update the parameters in `survey_surprise_task.ipynb` to point to the location of your downloaded resources.
    * Run the cells in this notebook. Results will be displayed and also saved under your specifed `work_dir` (note, our results are available on github under `/output/`.
4. Reproducing results for the quiz benchmark:
    * Follow the same instructions as for the survey benchmark, except use the `quiz_surprise_task.ipynb` notebook.
    
## Contact info
Nicholas Klein | nicklein@umich.edu | https://www.linkedin.com/in/nic-klein/