
index: bulk.txt
	curl 'http://localhost:9200/testing' -XDELETE
	curl 'http://localhost:9200/testing' -XPUT -d '@mappings/testing.json'
	curl 'http://localhost:9200/_bulk' -XPOST --data-binary '@bulk.txt' > /dev/null

bulk.txt: clean0.py clean1.py clean2.py dev0.txt dev1.txt dev2.txt dev3.txt dev4.txt dev5.txt
	./clean0.py dev0.txt.backup dev1.txt.backup dev2.txt.backup > bulk.txt
	./clean1.py dev0.txt dev1.txt dev2.txt >> bulk.txt
	./clean2.py dev3.txt dev4.txt dev5.txt >> bulk.txt

fetch:
	curl -O 'http://advaitha.pw/PM_Sense/dev0.txt'
	curl -O 'http://advaitha.pw/PM_Sense/dev1.txt'
	curl -O 'http://advaitha.pw/PM_Sense/dev2.txt'
	curl -O 'http://advaitha.pw/PM_Sense/dev3.txt'
	curl -O 'http://advaitha.pw/PM_Sense/dev4.txt'
	curl -O 'http://advaitha.pw/PM_Sense/dev5.txt'

json:
	./jsonify0.py dev0.txt.backup > dev0-old.json
	./jsonify0.py dev1.txt.backup > dev1-old.json
	./jsonify0.py dev2.txt.backup > dev2-old.json
	./jsonify1.py dev0.txt > dev0.json
	./jsonify1.py dev1.txt > dev1.json
	./jsonify1.py dev2.txt > dev2.json
	./jsonify2.py dev3.txt > dev3.json
	./jsonify2.py dev4.txt > dev4.json
	./jsonify2.py dev5.txt > dev5.json
