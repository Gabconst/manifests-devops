# Projeto de CI/CD com GitOps (Argo CD) e Observabilidade

Este projeto demonstra uma abordagem **GitOps** para o gerenciamento de configurações do Kubernetes, utilizando o **Argo CD** para sincronização automatizada. A observabilidade é implementada com **Prometheus** e **Grafana** para monitorar o estado da aplicação e as métricas do container.


## Tecnologias Utilizadas

* **GitOps:** Metodologia de entrega de software.
* **Kubernetes (K8s):** Orquestrador de containers.
* **Argo CD:** Ferramenta de entrega contínua (CD) baseada em GitOps.
* **Docker:** Para construção e gerenciamento da imagem do container da aplicação.
* **Prometheus:** Sistema de monitoramento e alerta de código aberto.
* **Grafana:** Plataforma de análise e visualização de dados.

---

## Arquitetura do Projeto

1.  **Repositório Git (Source of Truth):** Os arquivos de configuração (**manifests** Kubernetes) são versionados neste repositório.
2.  **Desenvolvimento:** As edições nos *manifests* K8s são feitas localmente e **commitadas** para a *branch* remota.
3.  **Argo CD (Reconciliation Loop):** O Argo CD monitora ativamente esta *branch* remota. Ao detectar um novo *commit*, ele **sincroniza** automaticamente as mudanças para o *cluster* Kubernetes, garantindo que o estado do *cluster* corresponda ao estado definido no Git.
4.  **Aplicação:** O *Deployment* do Kubernetes gerencia a aplicação em container Docker.
5.  **Observabilidade:** O Prometheus coleta métricas da aplicação e do container Docker, que são visualizadas por meio de um *Dashboard* configurado no Grafana.

---

## Fluxo de Trabalho (GitOps em Ação)

O ciclo de entrega é simplificado da seguinte forma:

1.  **Editar Manifests:** Altere ou adicione arquivos de configuração do Kubernetes (ex: `deployment.yaml`, `service.yaml`) no diretório apropriado do repositório.
2.  **Commit e Push:**
    ```bash
    git add .
    git commit -m "feat: Aplica nova versao ou configuracao"
    git push origin <sua-branch-remota>
    ```
3.  **Sincronização Automática:** O Argo CD detecta o novo *commit* e inicia a sincronização:
    * **Argo CD:** Observa o repositório.
    * **Argo CD:** Aplica as mudanças no *cluster* K8s.
4.  **Verificação do Cluster:** Confirme o estado dos seus *Deployments* e *Pods* no *cluster*:
    ```bash
    kubectl get deployments
    kubectl get pods
    kubectl describe deployment <nome-do-deployment>
    ```

---

## Construção da Imagem Docker

A aplicação é empacotada em uma imagem Docker. Use o `Dockerfile` incluso para construir a imagem:

### **1. Construir a Imagem**

```bash
docker build -t <seu-registry>/<nome-da-imagem>:<tag> .