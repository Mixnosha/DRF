FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/drf_site

COPY ./requirements /usr/src/requirements

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements

COPY . /usr/src/drf_site


#ENTRYPOINT ["python", "manage.py"]

#
#EXPOSE 8000
#
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]