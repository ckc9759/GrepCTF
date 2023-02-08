FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install python3
RUN mkdir challenge
COPY * /challenge/
ENTRYPOINT cd challenge && ./sleeper
