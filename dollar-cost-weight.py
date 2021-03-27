# coding: UTF-8
import csv
 
# 基準価格
price = 0.0

# 所持口数
stock = 0
# 毎月の購入金額
wallet = 1000.0
#支払い額
payment = 0
 
# 出力するCSV
output = ["年月,支払額,所持口数,総資産額"]

# 前月の価格
before = 0

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
 
        price = float(line[2])

        if before < price :
            #価格が上がった場合は８割の金額を購入
            stock = stock + wallet * 0.5 / price 
            payment = payment + wallet * 0.5
        else :
            #価格が下がった場合は12割の金額を購入
            stock = stock + wallet * 1.5 / price 
            payment = payment + wallet * 1.5
        before = price
        
        #CSV１行分の作成
        output.append(line[0] + "," + str(payment)+ "," + str(stock) + "," + str(stock * price))
 
# 作成したリストを一行ずつcsvとして出力
for line in output:
  print(line)