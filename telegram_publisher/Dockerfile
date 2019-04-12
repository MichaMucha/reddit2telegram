FROM continuumio/miniconda3
WORKDIR /app
COPY conda_env.yml environment.yml
RUN conda update -n base -c defaults conda
RUN conda env create -f environment.yml
ENTRYPOINT [ "/bin/bash", "-c" ]
RUN conda init bash
RUN echo "conda activate app" > ~/.bashrc
ENV PATH /opt/conda/envs/app/bin:$PATH
RUN conda list --explicit > env-spec-file.txt
COPY . /app
CMD ["python publisher.py publish comments"]