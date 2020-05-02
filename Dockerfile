FROM python

COPY . .

RUN apt-get update /
    apt-get install zsh /
    sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" /
    pip install -r requirements.txt

