# Kafka and Kubernetes: Hands-On Tutorial for Automating Kafka Deployments with ArgoCD.
## Introduction to the Components of the Deployment
For this practice, we will start by explaining the purpose and functionality of each component we will integrate into the deployment. 

### Kafka
Kafka is a distributed event streaming platform designed for high-performance data pipelines, streaming analytics, and real-time processing. It allows producers and consumers to communicate seamlessly through a publish-subscribe model.

**Applications of Kafka Beyond This Tutorial**
- Real-time Data Processing: Used by companies like LinkedIn, Netflix, and Uber to process and analyze massive streams of real-time data.
- Event-Driven Architectures: Kafka is widely used as the backbone for microservices communication.
- Data Integration: Acts as a central hub for collecting and distributing data across systems.
- Monitoring and Logging: Ideal for aggregating logs or metrics from distributed systems for centralized analysis.

### Zookeeper
Zookeeper is a critical component for Kafka’s functionality. It is responsible for:

- Managing metadata about the Kafka cluster, such as tracking which brokers are active.
- Facilitating leader elections for Kafka partitions to ensure availability and fault tolerance.
- Notifying Kafka of configuration changes, such as new topics or brokers.

### Kubernetes 

If you know what a container is like you’ve probably heard of Docker, the tool for creating and managing these containers.
While Docker runs containers on a single machine, Kubernetes takes it to the next level: it manages and orchestrates containers across multiple machines.

- Docker creates containers.
- Kubernetes organizes and scales them, ensuring they work together efficiently.
If you’ve mastered Docker, Kubernetes is the natural next step for learning how to deploy and manage containers at scale in production.

### ArgoCD

ArgoCD is a tool designed to automate the process of deploying and managing applications in Kubernetes. It works by syncing the desired state of your applications, defined in a Git repository, with your actual Kubernetes cluster.

**Why is ArgoCD Useful?**
Automated and Consistent: It eliminates the need for manual deployments and reduces the chances of errors.
Version Control: All configurations are stored in Git, making it easy to track changes and roll back if needed.
Continuous Monitoring: ArgoCD keeps monitoring your cluster, ensuring it stays in sync with the desired state.



## Environment Setup

For this practice, the first thing you’ll need if you plan to use Minikube on your local machine is to have Docker installed or any virtual machine manager like VirtualBox. Here’s the link to the official Minikube website, where the installation process is explained in more detail:
https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download

Secondly, once Kubernetes is running we’ll need to install and configure ArgoCD. For this, here you can find the link to the official ArgoCD documentation, which outlines the basic setup steps:
https://argo-cd.readthedocs.io/en/stable/getting_started/

Once you got ready your environment you can start coding.

## Code

In this tutorial, we will create two Docker images:

1. A Kafka Producer that sends 10 sequential messages to a specified Kafka topic.
2. A Kafka Consumer that receives and processes those messages.


The objective is to implement a seamless GitOps workflow where:

- Updates to the producer and consumer code are pushed to a GitHub repository.
- The changes are automatically deployed to Kubernetes using ArgoCD.
The desired state of the application will be defined in ArgoCD Application manifests, which will reside in the same Git repository.

![image](https://github.com/user-attachments/assets/75e01e89-2b88-4652-a0b8-ea070d47421d)

This setup ensures:

1. Consistency: Any code changes are automatically reflected in the deployment, keeping the system consistent with the desired state.
2. Efficiency: Simplifies updates and reduces manual intervention.


### **Steps to Deploy Kafka Producer and Consumer**

#### **1. Create an ArgoCD application**
Run the following command:
```bash
argocd app create kafka-app \
  --repo https://github.com/youruser/yourrepo.git \
  --path applications \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace kafka
```

**Explanation of the parameters:**
- **`--repo`**: Specifies your GitHub repository containing the Kubernetes manifests.
- **`--path`**: The directory within the repository where the manifests are located.
- **`--dest-server`**: The Kubernetes cluster URL (default for in-cluster is `https://kubernetes.default.svc`).
- **`--dest-namespace`**: The Kubernetes namespace for deploying the application.

---

#### **2. Sync Application to Kubernetes**
Run the following command:
```bash
argocd app sync kafka-app
```

This command:
- Applies the Kubernetes manifests in the specified repository and path.
- Ensures the state in Kubernetes matches the desired state defined in Git.


# Issues Faced
===> Configuring ... KAFKA_PORT is deprecated. Please use KAFKA_ADVERTISED_LISTENERS instead...

This error occurs due to how Kubernetes automatically generates environment variables for services when a pod starts. The kubelet dynamically creates these variables based on the names, hosts, and ports of services in the cluster. For example, if you name your service kafka, Kubernetes will generate variables like:
KAFKA_PORT, KAFKA_PORT_9092_TCP, KAFKA_SERVICE_HOST, etc.
This interfere with Kafka's configuration. The simplest way to resolve this issue is to rename your Kubernetes service to something distinct from the default kafka. This ensures that Kubernetes-generated variables do not interfere with Kafka's configuration.
