
This code presented the work of the bachelor thesis 'Exploring peptide-centric HLA-type prediction with data mining and machine learning'.
The three explorative typing approaches (NetMHCpan approach, allele-associated-lookup approach and Random Forest approach) can be evaluated on the TueDB.
The best-performing allele-associated lookup approach can be executed in the allele_associated_lookup_allele_specific_peptides.ipynb for own peptide input.

# 0 - Baseline
The baseline for 2-digit and 4-digit prediction can be run in the baseline.ipynb.
### Evaluation possible on:
- 2-digit
- 4-digit

# 1 - Ghosh Typing
The internal standard 2-digit prediction can be run with ghosh_typing.py.

# 2 - NetMHCpan-approach
The NetMHCpan approach can be run and evaluated in the netmhcpan_run_evaluation.ipynb in three variations.
- Option 1
- Option 2
- Option 3
### Evaluation possible on:
- 2-digit
- 4-digit

# 3 - Allele-associated-lookup approach
The allele-associated lookup approach has a run and an evaluation file. The run can be performed in five variations.
- Option 1: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 2: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 3: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 4: run allele_associated_lookup_allele_specific_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 5: run allele_associated_lookup_allele_specific_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb (the gibbs clustered dataset can be generated in the gibbs-clustering folder)
### Evaluation possible on:
- 2-digit
- 4-digit

# 4 - Random-forest-approach
The random forest approach can run with the RandomForest.ipynb
### Evaluation possible on:
- 2-digit
- 4-digit

# Allele-associated dataset
The allele-associated dataset was generated from data from these mhcquant commands.

# TueDB
The TueDB was preprocessed and adapted to the use case.

# DATA
The DATA folder comprises 4.62 GB and entails the TueDB, allele-associated-dataset and additional external data. The DATA folder can be requested on demand.
The results of all approaches are in a result txt in the corresponding folder.
