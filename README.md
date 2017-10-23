geting started

$ virtualenv --python=python3.6  --no-site-packages ENV
$ source ENV/bin/activate
$ pip install -r requirements.txt


each time a new package is added in the virtual ENV, generate a new requirements.txt file via:

(ENV)$ pip freeze > requirements.txt

