FROM miniconda3
WORKDIR /app
COPY conda_env.yml environment.yml
RUN conda env create -f environment.yml
RUN echo "conda activate app" > ~/.bashrc
RUN conda list --explicit > env-spec-file.txt
COPY . /app
RUN pip install .
CMD ["message_processor"]