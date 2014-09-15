sudo yum install libxslt-devel libxml2-devel
pip install PIL --allow-unverified PIL
pip freeze | grep -v "^-e" | xargs pip uninstall -y
