FROM python:3.10-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive
ARG USER=appuser
ENV APPUSER=$USER LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 WORKDIR=/app
WORKDIR $WORKDIR
RUN useradd --skel /dev/null --create-home $APPUSER
RUN chown $APPUSER:$APPUSER $WORKDIR
ENV PATH="/home/${APPUSER}/.local/bin:${PATH}"
ARG PACKAGES_PATH=/home/${APPUSER}/.local/lib/python${PYTHON_VERSION}/site-packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc6-dev \
        libpq-dev
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gettext \
        git \
        graphviz \
        libpq-dev \
        make \
        openssh-client
USER $APPUSER
COPY --chown=$APPUSER ./requirements.txt requirements.txt
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
COPY --chown=$APPUSER . .
USER $APPUSER
WORKDIR /app/archive
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["python3", "-m", "gunicorn", "archive.asgi"]