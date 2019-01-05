import requests
token = 'd9897b473aa80e4de80759c616a0f5c3b060e3bbbc5ba65c11abac6555b1928d32417c712a9e168bd2747'

# r = requests.get(f'https://api.vk.com/method/users.get?user_ids=14503420&fields=bdate&access_token={token}&v=5.92')

users = [1, 14503420, 324]  # list user id
for user in users:
    r = requests.get('https://api.vk.com/method/users.get', params={
        'user_ids': user,
        'fields': 'followers_count,bdate',
        'access_token': 'd9897b473aa80e4de80759c616a0f5c3b060e3bbbc5ba65c11abac6555b1928d32417c712a9e168bd2747',
        'v': 5.92
    })
    print(r.json())