FROM python:3.9.10-alpine3.15
ADD app /app
RUN pip install pipenv
WORKDIR /app
RUN pipenv install

# add tini init
RUN apk add tini

# expose uvicorn port
EXPOSE 8000

# start tini init
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["pipenv", "run", "uvicorn", "--host", "0.0.0.0", "main:app"]
