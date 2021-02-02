
conda create -n py37_flask python=3.7
conda activate py37_flask
pip install flask
pip install uwsgi


conda create -n py36_flask python=3.6
conda activate py36_flask

conda env remove -n py36_flask


