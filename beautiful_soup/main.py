from bs4 import BeautifulSoup
import requests

search = input("Enter search team: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
  item_text = item.find("a").text
  item_ref = item.find("a").attrs["href"]

  if item_text and item_ref:
    print(item_text)
    print(item_ref)
    # print("Summary: ", item.find("a").parent.parent.find("p").text)

    children = item.find("h2")
    print("Next sibling of the h2:", children.next_sibling)


