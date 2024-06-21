FROM continuumio/anaconda3

RUN apt-get -y update && apt-get -y install libpq-dev python3-dev

WORKDIR /app

# Install JupyterLab Extension
WORKDIR /jup

RUN apt-get install -y gcc g++ make nodejs npm
RUN apt install -y jupyter-notebook && pip install 'jupyterlab==4.2.2'

# COPY Local Files
COPY requirements.txt /app/requirements.txt
COPY commands /commands

RUN pip install -v -r /app/requirements.txt

# Start the JupyterLab
EXPOSE 8888
EXPOSE 8050
ENTRYPOINT ["/bin/bash", "-c","/commands/setup.sh"]
