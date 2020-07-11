FROM python:3

RUN pip install selenium

RUN python automation.py

CMD [“python automation.py”]

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
