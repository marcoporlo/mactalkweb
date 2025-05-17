from pybot_random import choice_command, dice_command
from pybot_event import event_command
from pybot_wikipedia import wikipedia_command

command_file = open('/Users/kam/Documents/Python/mactalkweb/mactalkweb/chatbot013.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(command):
    #command = input('pybot> ')
    response = ''
    try:
        for message in bot_dict:
            if message in command:
                response = bot_dict[message]
                break

        
        if '選ぶ' in command:
            response = choice_command(command)
        if 'さいころ' in command:
            response = dice_command()
        #if 'イベント' in command:
            response = event_command(command)
        #if '事典' in command:
            response = wikipedia_command(command)

        if not response:
            response = '何ヲ言ッテルカ、ワカラナイ'
        return response

        # if 'さようなら' in command:
        #     break

    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ')
        print(f'* 種類: {type(e)}')
        print(f'* 内容: {e}')
