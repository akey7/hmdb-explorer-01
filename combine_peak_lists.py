from lib2to3.pgen2 import token
import os
import pandas as pd

directory = os.fsencode('data/hmdb_predicted_msms_peak_lists')

accessions = set()

rows = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.txt'):
        tokens = filename.split('_')
        accession = tokens[0]
        if accession in accessions:
            print(f'{accession} is a duplicate. Skipping.')
        else:
            method = tokens[1]
            with open(f'data/hmdb_predicted_msms_peak_lists/{filename}', 'r') as f:
                for line in f:
                    line_stripped = line.strip()
                    mz, peak = line_stripped.split(" ")
                    row = {
                        'accession': accession,
                        'method': method,
                        'mz': mz,
                        'peak': peak
                    }
                    print(row)
                    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv('data/hmdb_predicted_msms_peak.csv', index=False)
