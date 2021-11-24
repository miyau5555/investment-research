# coding: UTF-8
import csv
 
# 基準価格
price = 0.0

# 口数
stock = 0.0

# ステータス
none = 0
buy = 1
sell = 2
status = none 

# 購入・売却額
basePrice = 0;

# 上昇・下降回数
time = 0

# 上限
limitTime = -1


# 前回価格
lastprice = 0

# 初期元本
wallet = 10000.00

# 取引手数料
commission = 0.01
 
# 税
tax = 0.2


# 出力するCSV
output = ["年月,総資産額"]
 
# csvのデータを読み込み
with open('./spy-vwo-daily.csv') as f:
    list = csv.reader(f)
    num = 0;
    for line in list:
        num = num + 1
        #一行目はヘッダのためスキップ
        if num == 1:
            # continueとは繰り返しのスキップで以降の処理をさせずに次の処理を行います。
            continue
 
        price = float(line[1])

        # 買いであった場合
        if status == buy :
            # 前日価格より上がっていた場f合
            if lastprice < price :
                # 3連続上昇の時は売って利確
                if time > limitTime : 
                    status = none
                    time = 0
                    # 利益がてたら税金を引く
                    if  price * (1 - commission) > basePrice :
                        wallet = wallet + stock * price * (1 - commission) - (price * (1 - commission) - basePrice) * stock * tax
                    # 損が出ていれば税金は引かない
                    else :
                        wallet = wallet + stock * price * (1 - commission)
                # それ以外はホールド     
                else : 
                    time = time + 1
            # 前日価格よりさがっていた場合は損切り
            else :
                status = none
                time = 0
                # 利益がてたら税金を引く
                if price * (1 - commission) > basePrice :
                    wallet = wallet + stock * price * (1 - commission) - (price * (1 - commission) - basePrice) * stock * tax
                # 損が出ていれば税金は引かない
                else :
                    wallet = wallet + stock * price * (1 - commission)
        # 売りだった場合
        elif status == sell :            
            # 前日価格より下がっていた場合
            if lastprice > price :
                # 3連続下降の時は買い戻して利確
                if time > limitTime : 
                    status = none
                    time = 0
                    # 利益がてたら税金を引く
                    if price * (1 + commission) < basePrice :
                        wallet = wallet + (stock * basePrice - (stock * price * (1 + commission))) - (basePrice - price * (1 + commission)) * stock * tax
                    # 損が出ていれば税金は引かない
                    else :
                        wallet = wallet + stock * basePrice - (stock * price * (1 + commission))

                # それ以外はホールド     
                else : 
                    time = time + 1
            # 前日価格よりあがっていた場合は損切り
            else :
                status = none
                time = 0
                # 利益がてたら税金を引く
                if price * (1 + commission) < basePrice :
                    wallet = wallet + (stock * basePrice - (stock * price * (1 + commission))) - (basePrice - price * (1 + commission)) * stock * tax
                # 損が出ていれば税金は引かない
                else :
                    wallet = wallet + stock * basePrice - (stock * price * (1 + commission))
        # 買いも売りもしていない場合は買いか売りの実施
        else :
            if lastprice < price :
                stock = round((wallet * 0.3) / price, 3)
                wallet = wallet - wallet * 0.3
                status = buy
                basePrice = price
            else :
                stock = round((wallet * 0.3) / price, 3)
                status = sell
                basePrice = price

        lastprice = price 

        if status == buy:
            output.append(line[0] + "," + str(price) + "," + str(status) + "," + str(wallet + (stock * price * (1 - commission))))
        elif status == sell:
            output.append(line[0] + "," + str(price) + "," + str(status) + "," + str(wallet + stock * basePrice - (stock * price * (1 + commission))))
        else :
            output.append(line[0] + "," + str(price) + "," + str(status) + "," + str(wallet))

#作成したリストを一行ずつcsvとして出力
for line in output :
    print(line)