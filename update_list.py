# Script que actualiza automáticamente los emojis del archivo markdown basándose en el número de citas 
# de cada artículo en  Semantic Scholar, modificando solamente los artículos presentes en el config.yaml
# See https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/post_graph_get_papers
# See https://stackoverflow.com/questions/28566714/how-to-load-html-page-variable-into-python-variable-using-the-web-address

import yaml
import requests
import re
import time
from urllib.parse import urlparse
import tqdm as tqdm

def get_influentialCitationCount(semantic_scholar_url):
    path = urlparse(semantic_scholar_url).path
    paper_id = path.split('/')[-1]
    api_url = f'https://api.semanticscholar.org/v1/paper/{paper_id}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        citationCount = data.get('influentialCitationCount', 0)
        print('influentialCitationCount', citationCount)
        return citationCount
    except:
        return None

def get_emoji(influentialCitationCount):
    if influentialCitationCount is None:
        return None # Mantener emoji existente si hay error
    if influentialCitationCount >= 50:
        return '🌟'
    elif influentialCitationCount > 25:
        return '🔥'
    elif influentialCitationCount >= 10:
        return '🔸'
    elif influentialCitationCount >= 5:
        return '🔹'
    else:
        return '◼️'

def replace_emoji(line, new_emoji):
    if not new_emoji:
        return line
    emoji_pattern = re.compile(r'(◼️|🔹|🔸|🔥|🌟)')
    matches = list(emoji_pattern.finditer(line))
    if not matches:
        return line.rstrip() + ' ' + new_emoji + '\n'
    else:
        last_match = matches[-1]
        return line[:last_match.start()] + new_emoji + line[last_match.end():]

def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    papers = config.get('papers', [])
    
    with open('README_2.md', 'r') as f:
        lines = f.readlines()
    
    for paper in tqdm.tqdm(papers, desc='Updating citations...'):
        name = paper['name']
        url = paper['url']
        
        try:
            influentialCitationCount = get_influentialCitationCount(url)
            emoji = get_emoji(influentialCitationCount)
        except:
            continue
        
        for i, line in enumerate(lines):
            if name in line:
                lines[i] = replace_emoji(line, emoji)
                break
        
        time.sleep(1)  # Evitar rate limiting
    
    with open('README_2.md', 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()