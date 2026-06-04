pipeline {
agent any

```
stages {

    stage('Deploy Backend') {
        steps {
            sshagent(credentials: ['azure-ssh']) {
                sh '''
                ssh -o StrictHostKeyChecking=no azureuser@74.235.72.123 "
                docker pull coolcoder34/simple-backend:latest &&
                docker stop backend-app || true &&
                docker rm backend-app || true &&
                docker run -d --name backend-app -p 80:80 coolcoder34/simple-backend:latest
                "
                '''
            }
        }
    }

    stage('Deploy Frontend') {
        steps {
            sshagent(credentials: ['azure-ssh']) {
                sh '''
                ssh -o StrictHostKeyChecking=no azureuser@74.235.72.123 "
                docker pull coolcoder34/frontend-js:latest &&
                docker stop fronted-app || true &&
                docker rm fronted-app || true &&
                docker run -d --name fronted-app -p 3000:80 coolcoder34/frontend-js:latest
                "
                '''
            }
        }
    }

    stage('Deploy Worker') {
        steps {
            sshagent(credentials: ['azure-ssh']) {
                sh '''
                ssh -o StrictHostKeyChecking=no azureuser@74.235.72.123 "
                docker pull coolcoder34/worker-python:latest &&
                docker stop worker-app || true &&
                docker rm worker-app || true &&
                docker run -d --name worker-app coolcoder34/worker-python:latest
                "
                '''
            }
        }
    }
}
```

}
