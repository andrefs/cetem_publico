"""
    Download, convert format and load CETEMPublico corpus to NLTK
"""
import os
import re
import requests
from nltk.corpus.reader.conll import ConllCorpusReader

home_path = os.environ['HOME']
folder = home_path + "/.cetem_publico"

def download():
    """Downloads the corpus file(s) and saves them in a folder

    TODO: add flag for partial vs full download, allow to define folder to save file
    """
    url = "http://bit.do/cetem2019"
    data = requests.get(url)
    os.makedirs(folder+"/cetem", exist_ok=True)
    filename = folder +"/cetem/cetem_publico_10k.txt"
    open(filename, "wb").write(data.content)


def cetem_to_conll(corpus_file):
    """Converts corpus from original format to ConLL format

    :param corpus_file: the location of the original corpus file
    """
    file = open(corpus_file)
    os.makedirs(folder  + '/conll/', exist_ok=True)

    cur_file = ""
    frase = False

    for line in file.readlines():
        line = re.sub(r'\n', '', line)

        match = re.match(r'<ext n=(.*?) sec=(.*?) sem=(.*?)>$', line)
        if match:
            folder_to_write = folder + '/conll/' + match[2] +'/' + match[3] + '/'
            os.makedirs(folder_to_write, exist_ok=True)
            file_name = match[1]+ '-' + match[2]+ '-'+match[3]+'.conll'
            cur_file = open(folder_to_write + file_name, 'w')
        elif re.match(r'<s>', line):
            frase = True
        elif re.match(r'</s>', line):
            frase = False
            cur_file.write('\n')
        elif re.match(r'</ext>', line):
            cur_file.close()
        elif re.match(r'</?mwe', line):
            continue
        elif frase:
            line = re.sub(r' ', '_', line)
            fields = line.split('\t')
            if len(fields) != 14:
                cur_file.write('\t'.join(fields)+ '\tFIXME\n')
            else:
                cur_file.write('\t'.join(fields)+ '\n')
            continue

def load_to_nltk(folder):
    """Recursively reads .conll files from a directory tree and return an nltk Corpus object

    :param folder: the root folder for the corpus
    """
    fields = ('words', 'ignore', 'ignore', 'ignore', 'pos')
    corpus = ConllCorpusReader(folder, r".*\.conll", fields)
    return corpus


def load():
    """Load the CETEMPublico corpus and return an NLTK Corpus object.

    If necessary, first download the corpus and/or convert it to the right format.
    """
    if not os.path.exists(folder + "/cetem/"):
        download()

    filename = folder +"/cetem/cetem_publico_10k.txt"
    if not os.path.exists(folder + "/conll/"):
        cetem_to_conll(filename)

    corpus = load_to_nltk(folder  + '/conll/')
    return corpus
