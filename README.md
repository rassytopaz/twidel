## 0.はじめに
### モチベーション
ほんの数年前は無料のツイ消しサービスが流行ってたのに、今は有料プランばっかり。  
無料だったサービスまで有料化し始めた。  
過去のツイートがちょっと取りにくくなったからって、全消しに600円、700円も金取ることないじゃん。  
許せねぇ、絶対に金払いたくない。

### 非対応事項
期間指定はタイムスタンプ活用すればできるけど、全消ししたかったので非対応  
RTは残る
### 参考
ここ↓  
https://qiita.com/aeas44/items/a5b82da69b64b32aada4  
tweet.jsのままやりたいならこっち↓（※）  
https://qiita.com/A_Akira0803/items/fe277f4b112a8ff501ee

## 1.必要なもの
> - ⓵アーカイブ
> - ⓶Python3
> - ⓷APIトークン

⓵ツイートからアーカイブをダウンロードしてくる    
設定　→　アカウント　→　データのアーカイブから  
⓶ggってDLしてくる  
⓷Twitter Developpers登録して、新規App or 既にあるApp のAPIトークン確認する  
必要なのは、api keyとaccess tokenと、それぞれのsecret。これをメモる（詳しくはネットで検索）  
(Twitter Developpers未登録で、今回初だと手間取るかも）

## 2.tweet.jsをCSVに変換
アーカイブを展開して、tweet.jsを取り出す  
上記（※）の記事を参考に、tweet.jsのまま使ってもいいんだけど、  
Windowsだとtweet.jsの編集時に勝手に文字コードが書き換わったので触りたくない   
なので、下記サービスをお借りして、CSVに変えてくる↓  
https://17number.github.io/tweet-js-loader/

## 3.実行前の準備
上記でDLしたtwitters.csvと同じディレクトリに、twidel.pyを配置  
twidel.pyをエディターで開いて、apiの空白にAPIトークンを記述  
これで準備完了。  

## 4.実行
実行すると、各ツイートのタイムスタンプがコンソールに流れていく   
アーカイブ取得後に削除したものは「deleted data」になる  

## 5.補足

### システムの説明
CSVファイルが
> - row[0]:ツイートid
> - row[1]:タイムスタンプ
> - row[2]:ツイート文
> - row[3]:いいね数
> - row[4]:リツイート数  

になってるので、row[0]を使って削除しにいく  
ツイートidあれば、ツイートは削除できる  
ちなみに、コンソール上には元々、タイムスタンプとツイート文を表記してたんだけど、  
絵文字が含まれてた時、コンソールがOSError吐き出すので、ツイート文の表示はやめた  

### 拡張性について
1)タイムスタンプを分解して、if作って、期間指定作ってもいいと思う。（参考の２つ目はやってる）  
2)RTは「RT (ツイート内容)」みたいな形でtweet.jsに保存されてるので、判定して取り消しの処理をいれてみてもいいと思う  
3)サービス借りずに、自分でjsonをcsvに変換する機構を作ってもいいと思う  
4)絵文字除去するか、コンソールで絵文字使えるようにするかで、削除するツイート文を表記してもいいと思う 




