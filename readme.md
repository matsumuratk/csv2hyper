# ローカルDockerイメージ作成 
docker image build -t csv2hyper . 

# Dockerコンテナ開始
docker run -dit -p 8080:8080 --name csv2hyper_container -d csv2hyper

# GCP CloudRun環境用に作成
# レポジトリ作成
gcloud artifacts repositories create csv2hyper-repo --location=asia-northeast1 --repository-format=docker --project=exture-taku2-lab

#　認証
gcloud auth configure-docker asia-northeast1-docker.pkg.dev

# Docker イメージ作成
docker build -t asia-northeast1-docker.pkg.dev/exture-taku2-lab/csv2hyper-repo/csv2hyper:1.0 .

# Push
docker push asia-northeast1-docker.pkg.dev/exture-taku2-lab/csv2hyper-repo/csv2hyper:1.0

# CloudRun Deploy
gcloud run deploy --image asia-northeast1-docker.pkg.dev/exture-taku2-lab/csv2hyper-repo/csv2hyper:1.0 --platform=managed --project=exture-taku2-lab --region=asia-northeast1

# カスタムドメインの追加
gcloud domains list-user-verified

# カスタムドメインの連携
gcloud beta run 