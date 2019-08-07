FROM registry.ubicast.net/docker/debian-dev:buster

# avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
# local pyvenv to avoid conflicts with system
ENV PYVENV /usr/local/pyvenv
# add pyvenv to path
ENV PATH ${PYVENV}/bin:${PATH}

RUN \
    # install required tools
    apt-get update && \
    apt-get install -y \
        libffi-dev \
        libssl-dev \
        && \
    # clean up
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* &&  \
    # create pyvenv
    python3 -m venv ${PYVENV} && \
    # update pip tools into pyvenv
    pip install -U \
        pip \
        wheel \
    && \
    # import hashicorp gpg key
    gpg --recv-key 51852D87348FFC4C && \
    :

ENV PACKER_VERSION 1.4.2
RUN \
    # packer
    curl -LOSs https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    curl -LOSs https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS && \
    curl -LOSs https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS.sig && \
    gpg --verify packer_${PACKER_VERSION}_SHA256SUMS.sig packer_${PACKER_VERSION}_SHA256SUMS && \
    shasum -a 256 -c packer_${PACKER_VERSION}_SHA256SUMS --ignore-missing && \
    unzip -d /usr/local/bin packer_${PACKER_VERSION}_linux_amd64.zip && \
    rm -f packer_${PACKER_VERSION}* && \
    :

COPY requirements.txt .
RUN \
    # ansible & co
    pip install -r requirements.txt && \
    rm requirements.txt && \
    :

# switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog
