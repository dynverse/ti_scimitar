FROM dynverse/dynwrappy:v0.1.0

RUN pip install rpy2==2.8
RUN pip install munkres
RUN pip install git+https://github.com/dimenwarper/pyroconductor
RUN pip install git+https://github.com/dimenwarper/scimitar

# install R dependencies
RUN R -e "install.packages('corpcor', repos = 'http://cran.us.r-project.org')"

COPY definition.yml run.py example.h5 /code/

ENTRYPOINT ["/code/run.py"]
