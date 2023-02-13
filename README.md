# Python Discord HTML Exporter to DiscoHook Exporter Json （沒那麽完美的Discord頻道合并功能）
### “林間專屬專利 —— 沒那麽完美的訊息移動功能”

衆所周知，Discord不開放合并文字頻道這功能給所有人。  
但有時候就會遇到一些問題 —— 如果兩個頻道的話題感覺差不多一樣 / 有一部分的話題更適合在其他的頻道區，  
除了放下面子跪地板求求其他人把文字原封不動搬遷到你想要的地方之外，應該有其他不求人的方法把？  

此系統利用 https://discohook.org/ export出來的json文件作爲樣本，  
從 https://github.com/Tyrrrz/DiscordChatExporter 輸出出來的html檔案轉換成適配 DiscoHook的 json檔案給用戶導入。  

## 前置安裝
```python
pip install bs4
```
本程式碼采用了beautifulsoup函數來整理抓到的網頁源代碼的内容，爲了後續的方便整理和篩選。

## 使用方法：
1. 先用Tyrrrz大大的DiscordChatExporter把你想要合并的頻道輸出成html格式
2. 把檔案放到跟此程式在同一個文件夾后，輸入以下指令：
```bat
python execute.py
```
3. 輸入檔案名稱，之後等待。
4. 把拿到的`output.json`丟去discohook導入，之後做一些細節修改（例如換頭像之類的），綁定`webhook url`就可以send了！

## 效果預覽
（之後再補上）

## 目前缺點
1. Discord的rate limited很讓人頭痛就是了
2. 上傳圖片必須，必須要另外保存以及手動增加 （如果你不打算保存舊頻道的話）
3. 因爲是webhook的關係，所有user的後面會有一個 "bot" 標志
4. 無法同步時間軸，因爲discord就不給你混肴時間事實。

## 延伸想法
1. —

## 參考文獻
你信不信這個程式碼有60%都是靠chatgpt生成出來的嗎？ 那還不用來試試？
https://chat.openai.com/chat/
