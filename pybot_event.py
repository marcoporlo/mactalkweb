import requests

def event_command(command):
    cmd, keyword = command.split()
    base_url = 'https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja'
    url = f'{base_url}?keyword={keyword}'
    r = requests.get(url)
    event_data = r.json()
    
    title = event_data['events'][0]['title']
    place = event_data['events'][0]['news']
    event_url = event_data['events'][0]['event_url']

    response = f'「{title}」ノ会場ハ{place}デス({event_url})'
    return response
