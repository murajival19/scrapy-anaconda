# ベースイメージ名:タグ名
FROM continuumio/anaconda3

# コンテナ側のルート直下にworkdir/（任意）という名前の作業ディレクトリを作り移動する
WORKDIR /workdir

# 仮想環境名
ARG env_name=scrapy_env

# 仮想環境の作成
COPY requirements.txt .
RUN	conda create -n ${env_name} python=3.8 && \
	echo "conda activate ${env_name}" >> ~/.bashrc

# パスの設定
ENV PATH /opt/conda/envs/${env_name}/bin:$PATH

# pipをアップグレードし必要なパッケージをインストール
RUN pip install --upgrade pip && \
	pip install -r requirements.txt
