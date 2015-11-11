#coding: utf-8
import csv

janken_txt = open('janken.txt', 'r') #読み込み用のファイルを開く
janken_csv = open("janken.csv", 'ab') #書き込み用のファイルを開く。無ければ作成するように'a'を指定
csvWriter = csv.writer(janken_csv)

try:
    header = 'Times,Date,Target'
    janken_csv.write(header + '\n') #ヘッダ行を書き込む

    for line in janken_txt: #janken.txtから1行ずつ読み込んで変数lineに入れる
        listData = [] #リストlistDataを初期化
        listData = line.split() #空白で分割されたリストを作成して変数listDataに入れる
        csvWriter.writerow(listData) #1行分書き込む

finally:
    janken_txt.close() #ファイルjanken_txtをクローズ
    janken_csv.close() #ファイルjanken_csvをクローズ
