import requests
from bs4 import BeautifulSoup
import difflib
from itertools import combinations
import os

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
    except requests.exceptions.RequestException:
        return None
    return response.text

def strip_text(soup):
    for elm in soup.find_all():
        if not elm.find(recursive=False):  # if not children
            elm.string = ' '
    return soup

def compare_html(html1, html2):
    seq_matcher = difflib.SequenceMatcher(None, html1, html2)
    return seq_matcher.ratio() * 100

def compare_all(names):
    names.sort()
    base_url = 'https://{}.github.io/wdd131/place.html'
    results = []

    for name1, name2 in combinations(names, 2):
        url1 = base_url.format(name1)
        url2 = base_url.format(name2)

        html1 = get_html(url1)
        if html1 is None:
            continue
        html2 = get_html(url2)
        if html2 is None:
            continue

        _, ext = os.path.splitext(base_url)

        if ext in ['.htm', '.html']:
            soup1 = BeautifulSoup(html1, 'html.parser')
            soup2 = BeautifulSoup(html2, 'html.parser')

            stripped_html1 = strip_text(soup1).prettify()
            stripped_html2 = strip_text(soup2).prettify()

            similarity = compare_html(stripped_html1, stripped_html2)
        else:
            similarity = compare_html(html1, html2)

        if similarity > 90:
            results.append(((name1, name2), similarity))

    results.sort(key=lambda x: x[1], reverse=True)

    '''''
    with open('output.txt', 'w') as f:  # Open the file in write mode
        for ((name1, name2), similarity) in results:
            f.write(f'{name1} and {name2} are {similarity:.2f}% similar.\n')  # Write to the file
    '''''

    for ((name1, name2), similarity) in results:
        print(f'{name1} and {name2} are {similarity:.2f}% similar.')

names = [
    'student_github_id_1', 'student_github_id_2'
]

compare_all(names)
