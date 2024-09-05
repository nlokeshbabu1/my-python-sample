In this repositry file we are going to create CI/CD are python flask application using following service 

1. Git action
2. ArgoCD
3. Helm/Charts
4. EKS or AKS

Installation of ArgoCD

Install Argo CD

Install Argo CD using manifests
# kubectl create namespace argocd
# kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Access the Argo CD UI (Loadbalancer service)
# kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
