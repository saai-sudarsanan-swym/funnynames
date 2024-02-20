# K8s Demo

## Install Minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
sudo install minikube-darwin-amd64 /usr/local/bin/minikube
```

## Install kubectl
```
brew install kubectl
Docs: https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/
```

## Setup Minikube Cluster with Docker Driver
```
minikube start
```

## Make Docker client use Minikube Docker Endpoint 
```
eval $(minikube docker-env)
```

## Clone this repo
```
git clone git@github.com:saai-sudarsanan-swym/funnynames.git
```

## Build the docker image
```
cd funnynames
docker build -t funnynames:1.0.0 .
```

## Deploy your replicaset using deployment.yaml
```
kubectl apply -f deployment.yaml
```