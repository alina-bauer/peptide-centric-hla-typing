#! /bin/bash
# https://www.nature.com/articles/s41587-019-0322-9#Sec14

# Methods
# MS/MS search parameters included: no-enzyme specificity; fixed modification: cysteinylation of cysteine;
# variable modifications: carbamidomethylation of cysteine, oxidation of methionine and pyroglutamic acid 
# at peptide N-terminal glutamine; precursor mass tolerance of ±10 ppm; product mass tolerance of ±10 ppm; 
# and a minimum matched peak intensity of 30%. Variable modification of carbamidomethylation of cysteine was
# only used for HLA alleles that included an alkylation step (performed in 2017 or later)

nextflow run nf-core/mhcquant -r 2.5.0 \
	-profile cfc \
	--input '/sfs/9/ws/qeasc01-allotypic_peptides/samplesheets/samplesheet_MSV000084172.tsv' \
	--outdir '/sfs/9/ws/qeasc01-allotypic_peptides/results/MSV000084172/post2016' \
	--fasta '/sfs/9/ws/qeasc01-allotypic_peptides/UP000005640_9606.fasta' \
	--digest_mass_range 800:2500 \
	--activation_method HCD \
	--prec_charge 2:3 \
	--fdr_threshold 0.01 \
	--fdr_level peptide_level_fdrs \
	--number_mods 3 \
	--precursor_mass_tolerance 10 \
	--fragment_mass_tolerance 0.01 \
	--num_hits 1 \
	--peptide_min_length 8 \
	--peptide_max_length 15 \
	--spectrum_batch_size 0 \
    --use_deeplc \
    --use_ms2pip \
    --ms2pip_model_name 'Immuno-HCD' \
    --skip_quantification \
    --fixed_mods 'Cysteinyl (C)' \
    --variable_mods 'Carbamidomethyl (C)' 'Oxidation (M)' 'pyro-Glu (N-term Q)' \
    -resume