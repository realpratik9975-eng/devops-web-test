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
    stage('Push Image') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
            )
        ]) {
                sh '''
                    echo "$DOCKER_PASSWORD" | docker login \
                        --username "$DOCKER_USERNAME" \
                        --password-stdin

                    docker tag \
                        metrics-server:jenkins-${BUILD_NUMBER} \
                        $DOCKER_USERNAME/metrics-server:jenkins-${BUILD_NUMBER}

                    docker push \
                        $DOCKER_USERNAME/metrics-server:jenkins-${BUILD_NUMBER}
                '''
        }
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
        script {
            env.PREVIOUS_IMAGE = sh(
                script: "docker inspect metrics-app-dev --format '{{.Config.Image}}' 2>/dev/null || true",
                returnStdout: true
            ).trim()

            echo "Previous deployed image: ${env.PREVIOUS_IMAGE}"
        }

        sh '''
            cat > access.log <<EOF
127.0.0.1 - - [20/Sep/2026 12:00:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Sep/2026 12:00:01] "GET /abc HTTP/1.1" 404 -
EOF

            docker rm -f metrics-app-dev || true

            docker pull pratik8595/metrics-server:jenkins-${BUILD_NUMBER}

            docker run -d \
              --name metrics-app-dev \
              -p 8001:8000 \
              -v "$WORKSPACE/access.log:/app/access.log:ro" \
              pratik8595/metrics-server:jenkins-${BUILD_NUMBER}
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

    post {
        failure {
            script {
                if (env.PREVIOUS_IMAGE?.trim()) {

                    echo "Health check failed."
                    echo "Rolling back to: ${env.PREVIOUS_IMAGE}"

                    sh """
                        docker rm -f metrics-app-dev || true

                        docker pull ${env.PREVIOUS_IMAGE}

                        docker run -d \
                          --name metrics-app-dev \
                          -p 8001:8000 \
                          -v "\$WORKSPACE/access.log:/app/access.log:ro" \
                          ${env.PREVIOUS_IMAGE}

                        sleep 2

                        curl -f http://localhost:8001/metrics
                    """

                    echo "Rollback completed successfully."
                } else {
                    echo "No previous image found. Rollback is not possible."
                }
            }
        }
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
