conda create -n python-practice -c conda-forge python=3.15.0 requests=2.34.2 -y
conda run -n python-practice python main.py
conda env export -n python-practice --from-history > environment.yml
