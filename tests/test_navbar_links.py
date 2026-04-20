import os
from bs4 import BeautifulSoup

# Path to index.html relative to repo root
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


def test_navbar_links_exist():
    index_path = os.path.join(PROJECT_ROOT, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    navbar = soup.find('div', class_='navbar')
    assert navbar is not None, "Navbar not found"

    links = [a['href'] for a in navbar.find_all('a', href=True)]

    for link in links:
        assert os.path.isfile(os.path.join(PROJECT_ROOT, link)), f"Missing file for link: {link}"

