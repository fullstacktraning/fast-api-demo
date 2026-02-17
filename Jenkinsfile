pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/fullstacktraning/fast-api-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-auth .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop fastapi-container || true'
                sh 'docker rm fastapi-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name fastapi-container fastapi-auth'
            }
        }
    }
}
