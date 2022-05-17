# surprising-facts
This is the repository for the paper "Identifying Surprising Facts in Wikidata" (TODO - update name if you choose somethign else, and add link once available).

## Notes to Filip / Hayden
I've marked where updates need to be made to add Hayden's automl method in `survey_surprise_task.ipynb` and `quiz_surprise_task.ipynb` with "hayden-todo", so you should be able to cmd-f for where to make changes.

Results for the surprise scores given by each method as well as the correlation scores for each method are saved under `/output/`.

TODO
I've gathered resources into a folder and specified their location below in the instructions. Aside from the random walk embeddings, everything is in a folder that is accessible only to kgtk/similarity people. The folder should be moved to a publicly available location, and the link in the instructions below should be updated.


Todo:
* put all necessary resources on gdrive (update comments in notebook parameters sections accordingly)
    * text, transe, complex profile transe and profile complex need new folder for this project
    * random walk embeddings could be copied to folder for this project, or we can link to the folder for the profiling project
    * wikidata-20210215-dwd.claims.wikibase-item.q5.tsv.gz should be moved to gdrive and off of github
    * labels.en file should be either copied to folder for this project, or link to the folder in the profiling project
    * profile_labels_info_joined.RELs_and_AILs.tsv and entity_profile_labels.RELs_and_AILs.shuffled.tsv should be added (with some instructions for how they could be created from the profiling project's ooutput
    * benchmark data should be added to gdrive, though fine to keep them on github
   
* add line for saving final results for both notebooks (both results and predictions)


## Steps for reproducing results
1. Install the required packages:
    * tqdm (`pip install tqdm`)
    * gensim (`pip install gensim`)
    * kgtk (follow documentation here: https://kgtk.readthedocs.io/en/latest/install/)
2. Download the following resources:
    * Most resources are available [here] (https://drive.google.com/drive/folders/16f6xgcqciJprB8PUYZsTvfyazSJTpgMN?usp=sharing)
        * benchmark data
            * These are also saved on github.
        * subset of wikidata edges about humans
            * alternatively, these can be created by following instructions in `create_q5_wd_subset.ipynb`
        * subset of wikidata edges about english labels
        * entity profile labels files
            * These are abstractions of information in WD, created by previous work ["Generating Explainable Abstractions for Wikidata Entities"](https://dl.acm.org/doi/10.1145/3460210.3493580). You can instead use the files directly created by that work (use `profile_labels.support.tsv` and (https://drive.google.com/file/d/19MKQs6Ua0hI_JXfOCPJax3ZLPhVXNfkk/view?usp=sharing) instead of `profile_labels_info_joined.RELs_and_AILs.tsv` and instead of  use 
        * text, transe, p-complex, and p-transe embeddings
    * Random walk embeddings are avalable [here](https://drive.google.com/drive/folders/1XE7w29_kr7yeEMuSDJbBifcR3iGuawd_?usp=sharing)
        * For each random walk embedding model you want to use, both the `.kv` and `.kv.vectors.npy` file need to be downloaded. For simplicity, you can download the whole folder.
3. Reproducing results for the survey benchmark:
    * update the parameters in `survey_surprise_task.ipynb` to point to the location of your downloaded resources.
    * Run the cells in this notebook. Results will be displayed and also saved under your specifed `work_dir` (note, our results are available on github under `/output/`.
4. Reproducing results for the quiz benchmark:
    * Follow the same instructions as for the survey benchmark, except use the `quiz_surprise_task.ipynb` notebook.