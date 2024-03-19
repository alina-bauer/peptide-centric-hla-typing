import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

with open('../../DATA/gosh_typing.json','r') as f:
    dict = eval(f.read())

    ghosh_alleles = list(dict.values())
    #divide list into beginning with A, B or C
    A = list(set([x for x in ghosh_alleles if x.startswith('A')]))
    A.sort()
    B = list(set([x for x in ghosh_alleles if x.startswith('B')]))
    B.sort()
    C = list(set([x for x in ghosh_alleles if x.startswith('C')]))
    C.sort()
    print('A', len(A), 'B', len(B), 'C', len(C))

#show how many 2 digit and 4 digit typing
keys = list(dict.values())
keys_equal3 = [key for key in keys if len(key) == 3]
keys_longer3 = [key for key in keys if len(key) > 3]
keys_shorter3 = [key for key in keys if len(key) < 3]
percentage_equal3 = len(keys_equal3) / len(keys) * 100
percentage_longer3 = len(keys_longer3) / len(keys) * 100
print(f"Percentage of strings equal 3 characters: {percentage_equal3:.2f}% e.g. {list(set(keys_equal3))[:5]} with {Counter(keys_equal3)}")
print(f"Percentage of strings longer 3 characters: {percentage_longer3:.2f}% e.g. {list(set(keys_longer3))} with {Counter(keys_longer3)}")


tdb = pd.read_csv('../../DATA/db_dump_311023_cleaned.tsv', sep='\t')
tdb_df = tdb.copy()

alleles = tdb_df['all_hla_alleles_donor'].explode().unique()
donors = tdb_df['donor_code'].unique()
tdb_df = tdb_df.sort_values(by=['donor_code'])
group1_df = tdb_df.groupby('donor_code')['peptide_sequence'].apply(list).reset_index()
group1_df['alleles'] = tdb_df.groupby('donor_code')['all_hla_alleles_donor'].apply(list).reset_index()['all_hla_alleles_donor']
group1_df['alleles'] = group1_df['alleles'].apply(lambda x: x[0])

loci_per_donor = [] #collection of dictionaries that represent locus
no_typing = [] #number of ghosh typings

no_donors = 0
correct_prediction = 0
accuracies = []
tdb_alleles = []


for _, row in group1_df.iterrows():

    no_donors += 1
    donor = row['donor_code']
    peptides = row['peptide_sequence']
    alleles = eval(row['alleles'])
    ghosh_typing =  []

    alleles = [a[:3] for a in alleles]
    alleles = list(set(alleles))
    tdb_alleles += alleles

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

    loci = {'A': 0, 'B': 0, 'C': 0}
    for u in unique_ghosh_typing:
        if u.startswith('A'):
            loci['A'] += 1
        elif u.startswith('B'):
            loci['B'] += 1
        elif u.startswith('C'):
            loci['C'] += 1
            
    no_typing.append(len(unique_ghosh_typing))
    loci_per_donor.append(str(loci))
    
print('Average number of typings per donor: ', sum(no_typing)/len(no_typing))
print('Average accuracy: ', sum(accuracies)/len(accuracies))

data = Counter(no_typing)
labels, values = zip(*data.items())
plt.bar(labels, values)
#plt.title('Distribution of Number of Ghosh typing per donor')
plt.xlabel('Ghosh typing per donor')
plt.ylabel('Donors')
plt.bar(labels, values, color='green')
plt.show()
plt.savefig('distribution_typing.png')

#make counter for all dicts
counter = Counter()
for d in loci_per_donor:
    counter[d] += 1

A = list(set([allele[:3] for allele in A]))
B = list(set([allele[:3] for allele in B]))
C = list(set([allele[:3] for allele in C]))

print('Number of 2-digit typed alleles on A locus: ', len(A))
print('Number of 2-digit typed alleles on B locus: ', len(B))
print('Number of 2-digit typed alleles on C locus: ', len(C))

tdb_alleles = list(set(tdb_alleles))
A_tdb = [x for x in tdb_alleles if x.startswith('A')]
A_tdb.sort()
print('Number of 2-digit typed alleles on A locus in TueDB: ', len(A_tdb))
B_tdb = [x for x in tdb_alleles if x.startswith('B')]
B_tdb.sort()
print('Number of 2-digit typed alleles on B locus in TueDB: ', len(B_tdb))
C_tdb = [x for x in tdb_alleles if x.startswith('C')]
C_tdb.sort()
print('Number of 2-digit typed alleles on C locus in TueDB: ', len(C_tdb))

print('Ghosh typing alleles', A, B, C)
print('TueDB alleles', A_tdb, B_tdb, C_tdb)

fig, ax = plt.subplots()
index = np.arange(3)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, [len(A), len(B), len(C)], bar_width, alpha=opacity, color='orange', label='Ghosh')
rects2 = plt.bar(index + bar_width, [len(A_tdb), len(B_tdb), len(C_tdb)], bar_width, alpha=opacity, color='green', label='TueDB')

plt.xlabel('Locus')
plt.ylabel('Alleles')
#plt.title('Number of 2-digit typed alleles per locus')
plt.xticks(index + bar_width / 2, ('A', 'B', 'C'))
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('alleles_per_locus_tuedb_ghosh.png')