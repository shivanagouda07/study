pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/shivanagouda07/study.git'
            }
        }

        stage('Run even.py') {
            steps {
                sh '''
                  echo "Running even.py"
                  ls -l
                  python3 even.py
                '''
            }
        }
    }
}
   
