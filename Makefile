hello: ii-3001-1-mouse-kidney_1GV/ii-3001-1-mouse-kidney_1GV.txt
	python image_process.py

ii-3001-1-mouse-kidney_1GV/ii-3001-1-mouse-kidney_1GV.txt: ii-3001-1-mouse-kidney_1GV.zip
	unzip -o ii-3001-1-mouse-kidney_1GV.zip
	touch ii-3001-1-mouse-kidney_1GV/ii-3001-1-mouse-kidney_1GV.txt

ii-3001-1-mouse-kidney_1GV.zip:
	wget -O ii-3001-1-mouse-kidney_1GV.zip http://3scan-opendata.s3-website-us-west-2.amazonaws.com/ii-3001-1-mouse-kidney_1GV.zip
	touch $@
