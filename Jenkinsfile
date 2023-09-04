pipeline {
    agent {
        docker {
            image 'python:3.8'
            args '--network=host'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}@tmp"
        BIN_PATH = "${HOME}/.local/bin/"
    }
    stages {
        stage('Git Clone') {
            steps {
                git changelog: false, url: 'http://gitlab.devops.ru/nadin001/tornado_fibonacci.git'
            }
        }
        stage('Prepare') {
            steps {
/* аналогично подготовительному этапу во 3 л.р.*/
                sh 'python --version'
                sh 'pip install virtualenv'
                sh "${BIN_PATH}virtualenv venv"
                sh 'bash -c "source venv/bin/activate"'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps{
/* меняем запуск теста, который был в 3 л.р.*/
                sh 'python -m unittest discover -s "./tests" -p "*_test.py"'
                sh "${BIN_PATH}flake8 ."
                sh "${BIN_PATH}mypy ."
            }
        }
    }
}