pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-cicd .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f flask-app || true
                    docker run -d --name flask-app -p 5000:5000 flask-cicd
                '''
            }
        }
    }
}
