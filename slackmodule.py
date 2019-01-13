from slackclient import SlackClient
from key import token

#move to OS later

sc = SlackClient(token)

response = sc.api_call(
    'chat.postMessage',
    channel='U7KCNM2UT',
    text='testing southwest2'
)
print(response)
# users = list
# user_list = sc.api_call('users.list')
# # print(user_list)
# # for u, id in user_list.items():
# #     print(u, id)
# print(user_list.keys())
# for u in user_list['members']:
#     if not u['deleted']:
#         print(u['id'] + ',' + u['real_name'])
