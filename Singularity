#######################################################################################
## DO NOT EDIT THIS FILE! This file was automatically generated from the dockerfile. ##
## Run babelwhale::convert_dockerfile_to_singularityrecipe() to update this file.    ##
#######################################################################################

Bootstrap: shub

From: dynverse/dynwrap:py2.7

%labels
    version 0.1.4

%files
    . /code

%post
    chmod -R 755 '/code'
    apt-get update && apt-get install -y r-base
    pip install rpy2==2.8
    pip install munkres
    pip install git+https://github.com/dimenwarper/pyroconductor
    pip install git+https://github.com/dimenwarper/scimitar
    R -e "install.packages('corpcor', repos = 'http://cran.us.r-project.org')"

%runscript
    exec python /code/run.py

