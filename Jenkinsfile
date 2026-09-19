pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'ls -la'
                sh 'docker build -t metrics-server:jenkins-${BUILD_NUMBER} .'
            } 
        }
        stage('Test') {
            steps {
                sh 'test -f index.html'
                sh 'echo "Application test passed"'
            }
        }

        stage('Deploy DEV') {
            steps {
                sh 'echo "Deploying application to DEV..."'
            }
        }

        stage('Approval for PROD') {
            steps {
                input message: 'Approve deployment to PROD?', 
                      ok: 'Deploy to PROD'
            }
        }

        stage('Deploy PROD') {
            steps {
                sh 'echo "Deploying application to PROD..."'
            }
        }
    }
}
