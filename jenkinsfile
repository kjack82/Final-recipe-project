pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/kjack82/project2.git'
            }
        }
        stage('Setup Python environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run FastAPI application') {
            steps {
                sh '''
                . venv/bin/activate
                uvicorn app:app --host 0.0.0.0 --port 8000 &
                '''
            }
        }
    }
}
