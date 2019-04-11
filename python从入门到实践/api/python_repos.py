import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print 'status code:', r.status_code

response_dict = r.json()
print "Total respositories:", response_dict['total_count']

repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    # print 'Owner:', repo_dict['owner']['login']
    # print 'Stars:', repo_dict['stargazers_count']
    # print 'Repository:', repo_dict['html_url']
    # print 'Created:', repo_dict['created_at']
    # print 'Updated:', repo_dict['updated_at']
    # print 'Description:', repo_dict['description']

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_style.x_label_rotation = 45
my_style.show_legend = False
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_style.truncate_label = 15
my_style.show_y_guides = False
my_style.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
