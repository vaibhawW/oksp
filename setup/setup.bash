python3 setup/setup.py
sudo apt-get update
sudo apt-get install python3-pip python3.5-dev libpq-dev postgresql postgresql-contrib memcached libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev libxml2-dev libxslt1-dev libffi-dev nodejs nodejs-legacy npm pandoc
pip3 install -r requirements/production.txt
echo "All Done Sir!!"