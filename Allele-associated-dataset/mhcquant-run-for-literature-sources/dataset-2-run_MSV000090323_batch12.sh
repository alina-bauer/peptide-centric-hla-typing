#! /bin/bash
# https://www.nature.com/articles/s41587-023-01945-y#data-availability
#neoepitopes were first allocated to peptide pools in unique combinations before
#healthy human donor CD8+ T cells were expanded using autologous monocyte-derived 
#dendritic cells, restimulated with the neoepitope peptide pools, sorted for 
#activation marker upregulation and subjected to TCRβ sequencing.

# Methods
#non-tryptic, the enzyme specificity was set as none; CID was selected as an activation method;
#and Orbitrap (Orbi-Orbi) was chosen as an instrument parameter. In-depth de novo assisted database
# search and quantification were performed with precursor mass error tolerance of 15 ppm, fragment 
# mass error tolerance of 0.02 Da and missed cleavage allowance of 3. Carbamidomethylation (Cys+57.02) 
#was set as a fixed modification, whereas deamidation (Asn+0.98 and Gln+0.98) and oxidation (Met+15.99) 

nextflow run nf-core/mhcquant -r 2.5.0 \
	-profile cfc \
	--input '/sfs/9/ws/qeasc01-allotypic_peptides/samplesheets/samplesheet_MSV000090323_batch12.tsv' \
	--outdir '/sfs/9/ws/qeasc01-allotypic_peptides/results/MSV000090323/batch12' \
	--fasta '/sfs/9/ws/qeasc01-allotypic_peptides/UP000005640_9606.fasta' \
	--digest_mass_range 800:2500 \
	--activation_method CID \
	--prec_charge 2:3 \
	--fdr_threshold 0.01 \
	--fdr_level peptide_level_fdrs \
	--number_mods 3 \
	--precursor_mass_tolerance 15 \
	--fragment_mass_tolerance 0.01 \
	--num_hits 1 \
	--peptide_min_length 8 \
	--peptide_max_length 15 \
	--spectrum_batch_size 0 \
    --use_deeplc \
    --use_ms2pip \
    --ms2pip_model_name 'CIDch2' \
    --skip_quantification \
    --fixed_mods 'Carbamidomethyl (C)' \
    --variable_mods 'Oxidation (M)' \ #ignoring the rest for now
    -resume