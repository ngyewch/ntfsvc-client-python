VERSION --explicit-global 0.6
FROM python:3.8

RUN apt-get -y update && apt-get install -y curl git

RUN git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.9.0
RUN echo ". $HOME/.asdf/asdf.sh" >> /root/.bashrc
ENV PATH="${PATH}:/root/.asdf/shims:/root/.asdf/bin"

RUN asdf plugin add python
RUN asdf plugin add poetry
RUN asdf plugin add task

RUN pip install sphinx sphinx-autoapi

WORKDIR /workspace

setup:
    COPY .tool-versions .
    RUN asdf local python system
    RUN asdf install

    COPY --dir src .
    COPY pyproject.toml poetry.lock .
    RUN poetry install

build:
    FROM +setup

    COPY . .
    RUN asdf local python system
    RUN task check
    RUN rm -rf .mypy_cache
    RUN cd docs && make html
    SAVE ARTIFACT docs/build/html docs
