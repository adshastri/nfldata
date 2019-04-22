from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.pro-football-reference.com/boxscores/201609110clt.htm")
html = r.text
html = html.replace("<!--", "").replace("-->", "")
soup = BeautifulSoup(html, features="html.parser")
rows = soup.find("table", id="team_stats").find_all("tr")[1:]
for r in rows:
    print(r.find("th").string)
    print(r.find_all("td")[0].string)
    print(r.find_all("td")[1].string)