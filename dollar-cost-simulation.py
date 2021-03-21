# coding: UTF-8
import csv
 
# 基準価格
price = 0.0

# 所持口数
stock = 0
# 毎月の購入金額
wallet = 1000.0
 
# 出力するCSV
output = ["年月,所持口数,総資産額"]
 
# csvのデータを読み込み
with open('./data.csv') as f:
    list = csv.reader(f)
    num = 0;
    for line in list:
        num = num + 1
        #一行目はヘッダのためスキップ
        if num == 1:
            # continueとは繰り返しのスキップで以降の処理をさせずに次の処理を行います。
            continue
 
        price = float(line[1])

        #所持口数の追加
        stock = stock + wallet / price

        #CSV１行分の作成
        output.append(line[0] + "," + str(stock) + "," + str(stock * price))
 
# 作成したリストを一行ずつcsvとして出力
for line in output:
  print(line)