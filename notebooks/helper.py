""" A helper script to accompany this pandas tutorial. """

import pandas as pd

def clean_df(df):
    df_list = df.to_dict('records')
    temp_list = []
    record_dict = {}
    for record in df_list:
        date = record['date'][0:10]
        if date not in record_dict.values():
            temp_list.append(record_dict)
            record_dict = {}
            record_dict['DATE'] = date
        record_dict['STATION'] = record['station'][6::]
        d_type = record['datatype']
        if d_type == 'TMAX' or d_type == 'TMIN' or d_type == 'TOBS':
            record_dict[d_type] = round((record['value']/10)*1.8 + 32, 2)
        else:
            record_dict[d_type] = record['value']
        record_dict['{}_ATTRIBUTES'.format(d_type)] = record['attributes']
        
    temp_list = temp_list[1::]
    cleaned_df = pd.DataFrame.from_records(temp_list, index='DATE')
    return cleaned_df