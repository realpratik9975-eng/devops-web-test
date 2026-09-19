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
        sh '''
            cat > access.log <<EOF
127.0.0.1 - - [19/Sep/2026 12:00:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/Sep/2026 12:00:01] "GET /abc HTTP/1.1" 404 -
EOF

            docker rm -f metrics-app-dev || true

            docker run -d \
              --name metrics-app-dev \
              -p 8001:8000 \
              -v "$WORKSPACE/access.log:/app/access.log:ro" \
              metrics-server:jenkins-${BUILD_NUMBER}
        '''
            }
        }

        stage('Health Check DEV') {
            steps {
                sh '''
                    sleep 2
                    curl -f http://localhost:8001/metrics
                '''
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
