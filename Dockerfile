FROM ubuntu
ADD data /work/data
RUN apt-get update
RUN apt-get install -y autoconf automake bzip2 faad g++ gawk git lame libatlas3-base libtool make mawk python2.7 python3 python3-pip screen subversion tree vim wget xclip zlib1g-dev
RUN ln -s /usr/bin/python2.7 /usr/bin/python2
RUN cd /work; git clone https://github.com/kaldi-asr/kaldi.git kaldi --origin upstream
RUN pip3 install virtualenv
