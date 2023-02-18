import sys
import pandas as pd

contact_info_file = sys.argv[1]
other_info_file = sys.argv[2]
output_file = sys.argv[3]

contact_data = pd.read_csv(contact_info_file)
other_data = pd.read_csv(other_info_file)

result = pd.merge(contact_data, other_data, left_on='respondent_id', right_on='id')
result = result.drop(columns='id')
result = result.dropna(how='any')

output = result[~result['job'].str.contains('insurance') == True]
output = output[~output['job'].str.contains('Insurance') == True]
output.to_csv(output_file, index=False)

print(output.info())