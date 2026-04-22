import requests

url = "https://github.com/search?q=mental+health&type=repositories"
response = requests.get(url)

html = response.text
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
repos = soup.find_all("li", class_="repo-list-item")
data = []

for page in range(1, 6):  # 5 pages
    url = f"https://github.com/search?q=mental+health&type=repositories&p={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    repos = soup.find_all("li")
    
    for repo in repos:
        title_tag = repo.find("a")
        if not title_tag:
            continue
        
        title = title_tag.text.strip()
        
        description_tag = repo.find("p")
        description = description_tag.text.strip() if description_tag else "No description"
        
        data.append({
            "title": title,
            "description": description
        })
        import pandas as pd

df = pd.DataFrame(data)
df.to_csv("github_repos.csv", index=False)

print("CSV créé avec succès ")