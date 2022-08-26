# hmdb-explorer-01
HMDB exploration and transformation to .csv files. Designed to work with data obtained from [https://hmdb.ca/downloads](https://hmdb.ca/downloads). The data are whole directories of individual `.txt` files and `.xml` files, which total 12 GB. Hence, these are ignore in the `.gitignore`.

The original data files that are downloaded from the URL are:

- `hmdb_metabolites.zip` (contains XML with data about metabolites)
- `hmdb_proteins.zip` (contains XML with data about proteins)
- `hmdb_predicted_msms_peak_lists.zip` (MS/MS predicted peaks)
- `hmdb_predicted_cms_peak_lists.zip` (CMS predicted peaks)

These are expected to be unzipped in the following tree structure, symlinked to the `data/` folder in this project.

- `hmdb_metabolites.xml` (an `.xml` file)
- `hmdb_proteins.xml` (an `.xml` file)
- `hmdb_predicted_msms_peak_lists` (a folder of `.txt` files)
- `hmdb_predicted_cms_peak_lists` (a folder of `.txt` files)
