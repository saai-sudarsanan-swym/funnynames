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
kubectl create ns funny
kubectl apply -f deployment.yaml
```

## Expose your service
```
kubectl get po -n funny
kubectl port-forward svc/funnynames-service 5000:80 -n funny
```

## Connect to your service
```
curl 127.0.0.1:5000/getname
```

--- 

# Helm Demo


## Delete old deployment
```
kubectl delete -f deployment.yaml 
```

## Install Helm
```
brew install helm
```

## Install the Application using the helm chart
```
helm install funnynames funnynames-chart -n funny -f funnynames-chart/values.yml
```