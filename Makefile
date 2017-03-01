
index:
	curl -s 'http://localhost:9200/testing' -XDELETE
	curl -s 'http://localhost:9200/testing' -XPUT -d '@mappings/testing.json'
	curl -s 'http://localhost:9200/_bulk' -XPOST --data-binary '@bulk.txt' >> /dev/null

fetch:
	echo > bulk.txt

	cat dev0.0.txt | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev0_0 >> bulk.txt
	cat dev1.0.txt | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev1_0 >> bulk.txt
	cat dev2.0.txt | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev2_0 >> bulk.txt

	cat dev3.0.txt | sed -n -e '/Bins:/p' | ./clean2.py dev3_0 >> bulk.txt
	cat dev4.0.txt | sed -n -e '/Bins:/p' | ./clean2.py dev4_0 >> bulk.txt
	cat dev5.0.txt | sed -n -e '/Bins:/p' | ./clean2.py dev5_0 >> bulk.txt

	curl 'http://advaitha.pw/PM_Sense/dev1.txt' | sed -n -e '/Bins:/p' | ./clean2.py dev1 >> bulk.txt
	curl 'http://advaitha.pw/PM_Sense/dev2.txt' | sed -n -e '/Bins:/p' | ./clean2.py dev2 >> bulk.txt
	curl 'http://advaitha.pw/PM_Sense/dev3.txt' | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev3 >> bulk.txt
	curl 'http://advaitha.pw/PM_Sense/dev4.txt' | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev4 >> bulk.txt
	curl 'http://advaitha.pw/PM_Sense/dev5.txt' | sed -n -e '/Bins:/p' | ./clean2.py dev5 >> bulk.txt
	curl 'http://advaitha.pw/PM_Sense/dev6.txt' | sed -e '1,3d' -e '/--*/d' -e 's/(/[/g' -e 's/)/]/g' | ./clean1.py dev6 >> bulk.txt
