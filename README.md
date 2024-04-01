
This code for the bachelor thesis 'Exploring peptide-centric HLA-type prediction with data mining and machine learning'.

The DATA folder comprises 4.62 GB and entails the TueDB, allele-associated-dataset and additional external data. The DATA folder can be requested on demand.
The results of all approaches are in a result txt in the corresponding folder.

# 0 - Baseline
The baseline for 2-digit and 4-digit prediction
### Evaluation possible on:
- 2-digit
- 4-digit

# 1 - Ghosh Typing
### internal standard employs the ghosh_typing.tsv
- 2-digit
- 4-digit

# 2 - NetMHCpan-approach
### NetMHCpan run on all peptides in TueDB
NetMHCpan approach run 
- Option 1
- Option 2
- Option 3
### Evaluation possible on:
- 2-digit
- 4-digit

# 3 - Allele-associated-lookup approach
### Has a run ipynb and an evaluation ipynb.
- Option 1: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 2: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 3: run allele_associated_lookup_all_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 4: run allele_associated_lookup_allele_specific_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb
- Option 5: run allele_associated_lookup_allele_specific_peptides.ipynb to get a result_dict, run allele_associated_lookup_evaluation.ipynb (the gibbs clustered dataset can be generated in the gibbs-clustering folder)
### Evaluation possible on:
- 2-digit
- 4-digit

# 4 - Random-forest-approach
### Evaluation possible on:
- 2-digit
- 4-digit

# Allele-associated dataset
- was generated from data from with these mhcwuant commands
- peptide allele pairs are stored in the data_readout_final folder


# TueDB
- preprocessing
- plotting
