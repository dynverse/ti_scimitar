FROM dynverse/dynwrap_latest:v0.1.0

ARG GITHUB_PAT

RUN pip install munkres
RUN pip install git+https://github.com/dimenwarper/pyroconductor
RUN pip install git+https://github.com/dynverse/SCIMITAR.git

# install R dependencies
RUN R -e "install.packages('corpcor', repos = 'http://cran.us.r-project.org')"

COPY definition.yml run.py example.sh /code/

ENTRYPOINT ["/code/run.py"]
