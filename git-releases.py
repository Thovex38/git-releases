from bs4 import BeautifulSoup
import urllib.request
import json
import re


def create_soup(url):
    """Return beautiful object from an url"""
    req = urllib.request.urlopen(url)
    soup = BeautifulSoup(req, 'html.parser')
    return soup


def get_releases_current_page(soup,releases):
    """For the current pages get the different releases shown

    Look inside h4 tag  with specified class at the href link
    Save the releases in a list
    """
    name_box = soup.find_all('h4', attrs={'class': 'flex-auto min-width-0 pr-2 pb-1 commit-title'})
    for div in name_box:
        for a in div.find_all('a'):
            href = a['href']
            tag = href.split("tag/")[1]
            releases.append(tag)


def find_next(soup):
    """Get the next release page from the current one

    Look inside div tag  with specified class at the href link
    Return the url
    """
    after_box = soup.find_all('div', attrs={'class': 'pagination'})
    after_link = after_box[0].find_all('a')
    for a in after_link:
        if a.get_text() == 'Next':
            return a['href']
    return 0


def find_release_gitrepo(url):
    """Get the releases list of a git repositery

    Return the release list
    """
    url = url+'/tags'
    soup_first_page = create_soup(url)
    releases = []
    get_releases_current_page(soup_first_page, releases)
    next_url = find_next(soup_first_page)
    while next_url != 0:
        url = next_url
        soup_next_page = create_soup(url)
        get_releases_current_page(soup_next_page, releases)
        next_url = find_next(soup_next_page)
    return releases


def standardize_release(release_list):
    """Standardize the release convention according to decided rules"""
    standardized = [re.sub('((?!show)(?!tflite)^\D+)', '', i) for i in release_list]
    standardized = [re.sub('-', '', i) for i in standardized]
    standardized = [re.sub('alpha', 'a', i) for i in standardized]
    standardized = [re.sub('incubating', 'i', i) for i in standardized]
    standardized = [re.sub('candidate', 'c', i) for i in standardized]
    standardized = [re.sub('beta', 'b', i) for i in standardized]
    standardized = list(dict.fromkeys(standardized))  # remove possible duplicates
    return standardized


if __name__ == "__main__":
    git_links = {'kafka': 'https://github.com/apache/kafka','tensorflow': 'https://github.com/tensorflow/tensorflow',
                 'django': 'https://github.com/django/django'}

    git_releases = {}  # stock the releases for each repo in a dict with key the name of the repo
    for key, value in git_links.items():
        release = find_release_gitrepo(value)
        git_releases[key] = release

    with open('git_releases.txt', 'w') as outfile:
        json.dump(git_releases, outfile)  # write to json format

    git_releases_standardized = {}  # stock the standardized releases for each repo in a dict
    for key, value in git_releases.items():
        releases_standardized = standardize_release(list(value))
        git_releases_standardized[key] = releases_standardized

    with open('git_releases_standardized.txt', 'w') as outfile1:
        json.dump(git_releases_standardized, outfile1)   # write to json format















