import pandas as pd
from collections import Counter

#read in ghosh typing
with open('../../DATA/gosh_typing.json','r') as f:
    dict = eval(f.read())
    ghosh_alleles = list(dict.values())

#prepare tuedb
tdb = pd.read_csv('../../DATA/db_dump_311023_cleaned.tsv', sep='\t')
tdb_df = tdb.copy()
alleles = tdb_df['all_hla_alleles_donor'].explode().unique()
donors = tdb_df['donor_code'].unique()
tdb_df = tdb_df.sort_values(by=['donor_code'])
group1_df = tdb_df.groupby('donor_code')['peptide_sequence'].apply(list).reset_index()
group1_df['alleles'] = tdb_df.groupby('donor_code')['all_hla_alleles_donor'].apply(list).reset_index()['all_hla_alleles_donor']
group1_df['alleles'] = group1_df['alleles'].apply(lambda x: x[0])


#calculate accuracies
accuracies = []

for _, row in group1_df.iterrows():

    donor = row['donor_code']
    peptides = row['peptide_sequence']
    alleles = eval(row['alleles'])
    ghosh_typing =  []

    alleles = [a[:3] for a in alleles]
    alleles = list(set(alleles))

    if len(alleles) > 3 and len(alleles) < 7:

        alleles_a = set([a for a in alleles if a.startswith('A')])
        alleles_b = set([a for a in alleles if a.startswith('B')])
        alleles_c = set([a for a in alleles if a.startswith('C')])

        for peptide in peptides:
            if peptide in dict:
                typing = dict[peptide]
                typing = typing[:3]
                ghosh_typing.append(typing)
        
        ghosh_counter = Counter(ghosh_typing)
        unique_ghosh_typing = list(set(ghosh_typing))

        ghosh_a = {k: v for k, v in ghosh_counter.items() if k.startswith('A')}
        ghosh_b = {k: v for k, v in ghosh_counter.items() if k.startswith('B')}
        ghosh_c = {k: v for k, v in ghosh_counter.items() if k.startswith('C')}

        penalty = 0
        matching = 0
        
        if len(ghosh_a) < len(alleles_a):
            penalty += len(alleles_a) - len(ghosh_a)
        if len(ghosh_a) == len(alleles_a):
            matching += len(set(list(ghosh_a.keys())).intersection(alleles_a))
        if len(ghosh_a) > len(alleles_a):
            sorted_ghosh_a = [item[0] for item in sorted(ghosh_a.items(), key=lambda x: x[1], reverse=True)[:2]]
            matching += len(set(sorted_ghosh_a).intersection(alleles_a))

        if len(ghosh_b) < len(alleles_b):
            penalty += len(alleles_b) - len(ghosh_b)
        if len(ghosh_b) == len(alleles_b):
            matching += len(set(list(ghosh_b.keys())).intersection(alleles_b))
        if len(ghosh_b) > len(alleles_b):
            sorted_ghosh_b = [item[0] for item in sorted(ghosh_b.items(), key=lambda x: x[1], reverse=True)[:2]]
            matching += len(set(sorted_ghosh_b).intersection(alleles_b))

        if len(ghosh_c) < len(alleles_c):
            penalty += len(alleles_c) - len(ghosh_c)
        if len(ghosh_c) == len(alleles_c):
            matching += len(set(list(ghosh_c.keys())).intersection(alleles_c))
        if len(ghosh_c) > len(alleles_c):
            sorted_ghosh_c = [item[0] for item in sorted(ghosh_c.items(), key=lambda x: x[1], reverse=True)[:2]]
            matching += len(set(sorted_ghosh_c).intersection(alleles_c))
        
        accuracy = (matching - penalty) / len(alleles)
        if accuracy < 0:
            accuracy = 0
        accuracies.append(accuracy)

print('Average accuracy: ', round(sum(accuracies)/len(accuracies),2))