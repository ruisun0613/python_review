"""
17-2. Active Discussions: Using the data from hn_submissions.py, make a
bar chart showing the most active discussions currently happening on
Hacker News. The height of each bar should correspond to the number of
comments each submission has. The label for each bar should include the
submission’s title and act as a link to the discussion page for that
submission. If you get a KeyError when creating a chart, use a try-except
block to skip over the promotional posts.
"""

import json
import requests
import plotly.express as px
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print(f"Status Code: {r.status_code}")

submission_ids = r.json()

titles, comments= [], []
for submission_id in submission_ids[:30]:
    try:
        # Make a new API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # Build a dictionary for each article
        submission_dict = {
            'title' : response_dict['title'],
            'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
            'comments' : response_dict['descendants'],
        }

        link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"

        titles.append(link)
        comments.append(submission_dict['comments'])
    except KeyError:
        continue

title = "Hacker News Comments Data"
labels = {'x': 'Title', 'y': 'Comments'}
fig = px.bar(
    x = titles,
    y = comments,
    title = title,
    labels = labels,
)

fig.show()