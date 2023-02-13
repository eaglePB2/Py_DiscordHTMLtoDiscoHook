from bs4 import BeautifulSoup
import json

name = input("輸入你的檔案名稱（後面不用加.html，系統自動幫你加）")
finalise = name + '.html'


with open(finalise, "r", encoding="UTF-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

json_data = {
  "version": 7,
  "backups": [
    {
      "name": "w",
      "messages": [],
      "targets": [
          {
              "url": ""
          }
          ]
    }
  ]
}

for message_group in soup.find_all(class_='chatlog__message-group'):
    messages = []
    for message_container in message_group.find_all(class_='chatlog__message'):
        message = {}
        try:
            author = message_container.find(class_='chatlog__author').text
        except AttributeError:
            print('Author not found, use previous author instead.')
        try:
            avatar_element = message_container.find(class_='chatlog__avatar')
            if avatar_element:
                avatar_url = avatar_element['src']
        except AttributeError:
            print('Avatar Image not found, use previous Image instead.')
        try:
            text = message_container.find(class_='chatlog__markdown-preserve').text
        except AttributeError:
            print('text is not found, skipping!')
            break
        print(author)
        print(text)
        message['data'] = {
            "content": text,
            "embeds": None,
            "username": author,
            "avatar_url": avatar_url,
            "attachments": []
        }
        messages.append(message)
    json_data['backups'][0]['messages'].extend(messages)

with open('output.json', 'w') as file:
    json.dump(json_data, file, indent=4)

print("DONE! 請查看output.json，之後導入試試！")