FROM apache/spark:3.5.1-python3

# switch user to root so we can do things
USER root

# Python Installs
RUN pip install pandas
RUN pip install Cerberus
RUN pip install pyarrow
RUN pip install pytest
RUN pip install coverage

# make spark user UID match WSL user for permssions ease.
RUN usermod -u 1000 spark

# IMPORTANT... switch back to spark users for container operations.
USER spark

