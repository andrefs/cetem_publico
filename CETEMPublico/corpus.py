"""
    Download, convert format and load CETEMPublico corpus to NLTK
"""
import os
import re
import gzip
import requests
from nltk.corpus.reader.conll import ConllCorpusReader
from clint.textui import progress

home_path = os.environ['HOME']
folder = home_path + "/.CETEMPublico"
small_file = "cetem_publico_small.txt.gz"
small_url  = "http://bit.do/cetem2019"
big_file   = "cetem_publico_full.txt.gz"
big_url    = "https://www.linguateca.pt/CETEMPublico/download/CETEMPublicoAnotado2019.txt"

def download(full=False):
    """Downloads the corpus file(s) and saves them in a folder.

    :full=False: set to True if you want the full 12GB file, otherwise it will download a small (500KB) sample

    TODO: add flag for partial vs full download, allow to define folder to save file
    """

    filename = small_file
    url = small_url
    if full:
        url = big_url
        filename = big_file

    os.makedirs(folder+"/cetem", exist_ok=True)

    r = requests.get(url, stream=True)
    path = folder +"/cetem/"+filename

    with gzip.open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

def cetem_to_conll(corpus_file, corpus_folder):
    """Converts corpus from original format to ConLL format

    :param corpus_file: the location of the original corpus file
    :param corpus_folder: the path where to save the conll files
    """
    file = gzip.open(corpus_file, 'rt')
    os.makedirs(corpus_folder, exist_ok=True)

    cur_file = ""
    frase = False

    for line in file.readlines():
        line = re.sub(r'\n', '', line)

        match = re.match(r'<ext n=(.*?) sec=(.*?) sem=(.*?)>$', line)
        if match:
            folder_to_write = corpus_folder + match[2] +'/' + match[3] + '/'
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
    """Recursively reads .conll files from a directory tree

    :param folder: the root folder for the corpus
    :returns: a NLTK Corpus object
    """
    fields = ('words', 'ignore', 'ignore', 'ignore', 'pos')
    corpus = ConllCorpusReader(folder, r".*\.conll", fields)
    return corpus


def load(full=False):
    """Load the CETEMPublico corpus

    If necessary, first download the corpus and/or convert it to the right format.

    :full=False: set to True if you want the full 12GB file, otherwise it will load the small (500KB) sample
    :returns: a NLTK Corpus object
    """


    filename = small_file
    conll_folder = folder + "/conll-small/"

    if full:
        filename = big_file
        conll_folder = folder + "/conll-full/"

    path = folder +"/cetem/"+filename

    if not os.path.exists(path):
        download(full=full)

    if not os.path.exists(conll_folder):
        cetem_to_conll(path, conll_folder)

    corpus = load_to_nltk(conll_folder)
    return corpus
