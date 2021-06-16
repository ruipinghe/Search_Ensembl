# Search_Ensembl
Using Python and the framework Django to develop a REST endpoint service that provides a single endpoint get_species_databases.

git clone https://github.com/ruipinghe/Search_Ensembl.git

cd Search_Ensembl

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate --fake-initial

python manage.py runserver


'''
git clone git@cseegit.essex.ac.uk:yw19282/methylation_database.git
cd methylation_database
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver
'''
