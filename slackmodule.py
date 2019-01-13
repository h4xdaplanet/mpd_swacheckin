from slackclient import SlackClient
from key import token
from key import bot_token
import time

# sc = SlackClient(bot_token)

# response = sc.api_call(
#     'chat.postMessage',
#     channel='U7KCNM2UT',
#     text='testing southwest2'
# )
# print(response)

# users = list
# user_list = sc.api_call('users.list')
# # print(user_list)
# # for u, id in user_list.items():
# #     print(u, id)
# print(user_list.keys())
# for u in user_list['members']:
#     if not u['deleted']:
#         print(u['id'] + ',' + u['real_name'])

# api_call = sc.api_call("users.list")
# if api_call.get('ok'):
#     users = api_call.get('members')
#     for user in users:
#         print(user.get('name'))

# if sc.rtm_connect(with_team_state=False):
#     print("Successfully connected, listening for events")
#     while True:
#         print(sc.rtm_read())
#
#         time.sleep(1)
# else:
#     print("Connection Failed")

import bot
bot.Bot()
