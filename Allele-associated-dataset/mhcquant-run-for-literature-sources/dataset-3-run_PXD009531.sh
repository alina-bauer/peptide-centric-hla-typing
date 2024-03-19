#! /bin/bash

nextflow run nf-core/mhcquant -r 2.5.0 \
	-profile cfc \
	--input '/sfs/9/ws/qeasc01-allotypic_peptides/samplesheets/samplesheet_PXD009531.tsv' \
	--outdir '/sfs/9/ws/qeasc01-allotypic_peptides/results/PXD009531' \
	--fasta '/sfs/9/ws/qeasc01-allotypic_peptides/UP000005640_9606.fasta' \
	--digest_mass_range 800:2500 \
	--activation_method CID \
	--prec_charge 2:3 \
	--fdr_threshold 0.01 \
	--fdr_level peptide_level_fdrs \
	--number_mods 3 \
	--precursor_mass_tolerance 5 \
	--fragment_mass_tolerance 0.01 \
	--num_hits 1 \
	--peptide_min_length 8 \
	--peptide_max_length 15 \
	--spectrum_batch_size 0 \
    --use_deeplc \
    --use_ms2pip \
    --ms2pip_model_name 'CIDch2' \
    --skip_quantification \
    -resume