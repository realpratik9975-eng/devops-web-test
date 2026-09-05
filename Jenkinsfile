pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'ls -la'
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
    }
}
