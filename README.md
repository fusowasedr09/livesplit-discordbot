# livesplit-discordbot
LivesplitをDiscordで操作するためのbot。自分でbotをビルドする必要があります。

## 必要環境
・Python 3.8~  
・discord.py 1.4.0a~  
・Livesplit Server( https://github.com/LiveSplit/LiveSplit.Server )が導入されているLivesplit  

## 使い方
1.DiscordのBotのアカウントを作成する。  参考URL：https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf   
2.取得したbotのトークンをlivesplit-discordbot.pyのtokenのところに入力  
3.Livesplitを起動し、layoutにlivesplit.serverを追加。追加後、control>Start Serverをクリック  
4.ローカルでlivesplit-discordbot.pyを走らせる  
5.botがオンラインになり、メッセージを送信したのを確認できたらOK。コマンド入力でLivesplitが動く（はず）

## コマンド
!start - タイマースタート  
!split - 次のスプリットへ、最後のスプリットならタイマー停止  
!reset - タイマーをリセットする  
!pause - タイマーの一時停止  
!resume - タイマー再開  
!back - 前のスプリットに戻す  
!skip - 現在のスプリットをスキップする 

作りがかなり適当かつ検証不足なので不具合が出るかもしれません
