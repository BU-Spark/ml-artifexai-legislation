import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://malegislature.gov/Committees"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

committee_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith("/Committees/"):
        committee_links.append("https://malegislature.gov" + href)

committee_data = []

for committee_url in committee_links:
    print(f"Scraping: {committee_url}")
    committee_response = requests.get(committee_url)
    committee_soup = BeautifulSoup(committee_response.content, 'html.parser')

    committee_name = committee_soup.find('h1').text.strip()
    print(committee_name)

    members = []
    committee_member_lists = committee_soup.find_all('ul', {'class': 'committeeMemberList'}) 

    for member_list in committee_member_lists:
        for member_item in member_list.find_all('li'): 
            member_data = {}

            member_a_tag = member_item.find('a', href=True)
            if member_a_tag:
                member_data['profile_url'] = "https://malegislature.gov" + member_a_tag['href']
                member_data['name'] = member_a_tag.text.strip()

            role_tag = member_item.find('span')
            if role_tag:
                member_data['role'] = role_tag.text.strip()
            else:
                additional_role = member_item.text.strip().split("\n")[-1]  
                if additional_role:
                    member_data['role'] = additional_role.strip()

            if 'name' in member_data and 'profile_url' in member_data:
                members.append(member_data)


    for member in members:
        member['committee_name'] = committee_name
    committee_data.extend(members)

df = pd.DataFrame(committee_data)


df.to_csv('committees_members.csv', index=False)

print(df.head())
