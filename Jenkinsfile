

pipeline {
    agent any

    environment {
        ECR_REGISTRY = "test"
        commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
    }

    stages {
        stage('Identify Changed Microservices') {
            steps {
                script {
                    def changedFiles = sh(script: 'git diff --name-only HEAD^ HEAD', returnStdout: true).trim().split('\n')
                    def servicesToBuild = []

                    changedFiles.each { file ->
                        if (file.startsWith('omarService/')) {
                            echo "service omarService modified"
                            servicesToBuild << 'omarService'
                        } else if (file.startsWith('saterService/')) {
                            servicesToBuild << 'saterService'
                            echo "service saterService modified"
                        }
                    }

                    servicesToBuild = servicesToBuild.unique()
                    echo "Services to build: ${servicesToBuild.join(', ')}"
                    env.SERVICES_TO_BUILD = servicesToBuild.join(',')
                }
            }
        }

        stage('Build Docker Images') {
            when {
                expression { return env.SERVICES_TO_BUILD }
            }
            steps {
                script {
                    def services = env.SERVICES_TO_BUILD.split(',')
                    services.each { service ->
                        sh """
                            cd ${service}
                            docker build -t ${env.ECR_REGISTRY}/${service}:${commitHash} .
                            cd ..
                        """
                    }
                }
            }
        }
    }
}