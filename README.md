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

Citation to the HMDB database, which is awesome!

> Wishart DS, Tzur D, Knox C, et al., HMDB: the Human Metabolome Database. Nucleic Acids Res. 2007 Jan;35(Database issue):D521-6. 17202168

> Wishart DS, Knox C, Guo AC, et al., HMDB: a knowledgebase for the human metabolome. Nucleic Acids Res. 2009 37(Database issue):D603-610. 18953024

> Wishart DS, Jewison T, Guo AC, Wilson M, Knox C, et al., HMDB 3.0 — The Human Metabolome Database in 2013. Nucleic Acids Res. 2013. Jan 1;41(D1):D801-7. 23161693

> Wishart DS, Feunang YD, Marcu A, Guo AC, Liang K, et al., HMDB 4.0 — The Human Metabolome Database for 2018. Nucleic Acids Res. 2018. Jan 4;46(D1):D608-17. 29140435

> Wishart DS, Guo AC, Oler E, et al., HMDB 5.0: the Human Metabolome Database for 2022. Nucleic Acids Res. 2022. Jan 7;50(D1):D622–31. 34986597 
