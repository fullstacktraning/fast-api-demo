pipeline {
    agent any

    environment {
        IMAGE_NAME = "fastapi-auth"
        CONTAINER_NAME = "fastapi-container"
        ENV_FILE = "/home/ubuntu/.env"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'master',
                url: 'https://github.com/fullstacktraning/fast-api-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d -p 8000:8000 \
                --env-file $ENV_FILE \
                --name $CONTAINER_NAME \
                $IMAGE_NAME
                '''
            }
        }

        stage('Verify Container') {
            steps {
                sh '''
                docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful 🚀'
        }
        failure {
            echo 'Deployment Failed ❌'
        }
    }
}





// pipeline {
//     agent any

//     stages {

//         stage('Clone') {
//             steps {
//                 git 'https://github.com/fullstacktraning/fast-api-demo.git'
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t fastapi-auth .'
//             }
//         }

//         stage('Stop Old Container') {
//             steps {
//                 sh 'docker stop fastapi-container || true'
//                 sh 'docker rm fastapi-container || true'
//             }
//         }

//         stage('Run New Container') {
//             steps {
//                 sh 'docker run -d -p 8000:8000 --name fastapi-container fastapi-auth'
//             }
//         }
//     }
// }
