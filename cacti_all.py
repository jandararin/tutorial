# -*- coding: utf-8 -*-
import bs4
import re
import os
import glob

i = 0

# listフォルダ内のhtmlファイルを読み込む
for i in range(5):
	get_fnames = glob.glob("./list/*.html")

	with open(get_fnames[i], mode='r', encoding='utf-8', errors='ignore') as f:
		soup = bs4.BeautifulSoup(f, 'lxml')

		# <class='linkEditMain'>を抽出する
		for a in soup.find_all(class_="linkEditMain"):
			
			# BeautifulSoupでclass_="linkEditMain"内のtitleを抽出
			title = a.attrs['title']
			
			# BeautifulSoupでclass_="linkEditMain"内のhrefを抽出
			url = a.attrs['href']
			
			# 抽出したhrefからid番号のみを抽出
			url_id = url.replace('graphs.php?action=graph_edit&id=', '')
			
			x = i + 1
			c = "," + str(x)
			server = ('61.45.73.214', '61.45.73.239', '61.45.72.230', '61.45.72.229', '61.45.72.231')
			cacti_url = "http://" + server[i] + "/cacti/graph.php?action=view&local_graph_id="
			end_url = "&rra_id=all"
			
			# エンコード・デコードエラーを起こす文字を置換
			title_enc = title.replace('\u2017', '_').replace('\u014d', 'o').replace('\u016b', 'u').replace('\u0332', ' ')
			
			# 先頭のスペースを削除
			s_title_enc = re.sub('^ +', '', title_enc)
			
			# 出力したいフォーマットにする
			cacti = f'{s_title_enc}\t{url_id}{c}\t{cacti_url}{url_id}{end_url}\n'
			
			# ファイル出力
			file_name = "./cacti_all.txt"
			try:
				file = open(file_name, 'a')
				file.write(cacti)
			except Exception as e:
				print(e)
			finally:
				file.close()
