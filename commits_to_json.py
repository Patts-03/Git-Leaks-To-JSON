from git import Repo
import re 
import time
import json

REPO_PATH = './skale-manager'                  # Dirección del repo donde vas a buscar los commits
KEY_WORDS = ['secrets','password','key']         # Palabras que vas a buscar en los commits 


def extract(REPO_PATH):
    repo = Repo(REPO_PATH)                           # Accedes a la información del repo y la guardas para poder procesarla más tarde
    
    return repo

def transform(repo):
    res = []
    json_res = {}
    commits_list = list(repo.iter_commits())         # Sacas del repo los commits para poder procesarlos y filtrar
    
    for word in KEY_WORDS:
        commits_word = {}
        counter = 1

        for commit in commits_list:

            if re.search(word, commit.message, re.I):

                res.append(f'Commit {counter} \nContains the key word : {word}\n{commit.hexsha} - {commit.message}')

                commits_word[counter] = f'{commit.hexsha} - {commit.message}'
                counter += 1


        json_res[word] = commits_word


                
    return res , json_res

def load(res): 

    for commit in res:
        print(commit)

    time.sleep(1)
    
def save_json(data):

    with open("commits.json", "w") as write_file:
        json.dump(data, write_file)

    return 

if __name__=='__main__':
    repo = extract(REPO_PATH)
    res , json_res = transform(repo)
    
    print('\nThere have been found',len(res),'commits:\n')
    load(res)

    
    save_json(json_res)
    