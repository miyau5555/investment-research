# coding: UTF-8
import csv
 
# 基準価格
price = 0.0
# これまでにかかった信託報酬
feeTotal = 0.0
# 年率信託報酬
feeRate = 0.03 / 100
# 所持口数
stock = 0
# 毎月の購入金額
wallet = 10000.0
 
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
 
        #コストの計算
        #本来信託報酬は毎日引かれているものだが1年に１度精算という形にする
        # float()とは文字列を小数点の数値型floatに変換する関数です。
        # CSVから取り出したデータがString型のため小数点数値のfloatに変換しています。
        if num % 12 == 0:
          feeTotal = feeTotal + (float(line[1]) - feeTotal) * feeRate
 
        #本来の基準価格からこれまでかかったコストを引いていく
        price = float(line[1]) - feeTotal
 
        #所持口数の追加
        stock = stock + wallet / price
        
        #CSV１行分の作成
        output.append(line[0] + "," + str(stock) + "," + str(stock * price))
 
# 作成したリストを一行ずつcsvとして出力
for line in output:
  print(line)