import requests
import plotly.express as px

# Make an API call and check the response.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
r= requests.get(url, headers = headers)

print(f"Status Code: {r.status_code}")

# Process overall results.
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information
repo_dicts = response_dict['items']
stars, hover_texts, repo_links = [], [], []

# One repository
# print("\n Selected information from first repository")

# Multiple repository
print("\n Selected information from each repository")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

    # Turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a herf='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

# Make visualization
title = "Most-Starred Python Project on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_links, y = stars, title = title, labels = labels, hover_name = hover_texts)
fig.update_traces(
    marker_color = 'SteelBlue',
    marker_opacity = 0.6
)
fig.update_layout(
    title_font_size = 28,
    xaxis_title_font_size = 20,
    yaxis_title_font_size = 20
)
fig.show()
