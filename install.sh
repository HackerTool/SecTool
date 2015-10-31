#!/bin/sh

brew install openssl libdnet libnet libnids glib cmake automake autoconf readline reaver

wget https://pypi.python.org/packages/source/p/pip/pip-7.1.2.tar.gz#md5=3823d2343d9f3aaab21cf9c917710196
tar -zxvf pip-7.1.2.tar.gz 
cd pip-7.1.2/
python setup.py build 
python setup.py install 
cd ..
rm -f -r pip-7.1.2*
pip install -r requirements.txt

gem sources --add https://ruby.taobao.org/ --remove https://rubygems.org/
gem sources -l
gem install bundler 

git clone https://github.com/sqlmapproject/sqlmap.git
git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework
bundle install 
cd ..
git clone https://github.com/beefproject/beef.git
cd beef
bundle install 
cd ..

echo "enjoy"


