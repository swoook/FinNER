import os
import requests
import tarfile
import pandas as pd
import dart_fss as dart


def load_korean_companies(dart_api_key):
    dart.set_api_key(api_key=dart_api_key)
    result = dart.get_corp_list()
    result = [(company.corp_code, company.corp_name, company.stock_code, company.modify_date) for company in result]
    result = pd.DataFrame(
        result, 
        columns = [
            'corp_code', 
            'corp_name', 
            'stock_code', 
            'modify_date', 
        ]
    )
    return result

def download(url, filepath):
    file_directory = os.path.dirname(filepath)
    if not os.path.exists(file_directory): os.makedirs(file_directory)
    with open(filepath, 'wb') as file:
        response = requests.get(url)             
        file.write(response.content)
        
def load_mecab_ko_dic_vocabulary(vocabulary_directory):
    result = list()
    columns = [
        '표층형', 'left-ID', 'right-ID', '비용', 
        '품사', '의미 부류', '종성 유무', '읽기', 
        '타입', '첫번째 품사', '마지막 품사', '표현'
    ]

    entries = os.listdir(vocabulary_directory)
    for idx, entry in enumerate(entries):
        # 'Wikipedia.csv' includes some of company names
        if entry in ['Wikipedia.csv']: continue
        entry_path = os.path.join(vocabulary_directory, entry)
        if os.path.isdir(entry_path): continue
        filename, extension = os.path.splitext(entry)
        if not extension == '.csv': continue
        
        dataframe = pd.read_csv(
            entry_path, 
            header=None, 
            names=columns,
        )
        dataframe.insert(dataframe.shape[1], '소스', entry)
        result.append(dataframe)
    
    result = pd.concat(result, axis=0, ignore_index=True)
    return result