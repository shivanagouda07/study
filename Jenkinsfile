pipeline {
    agent any
    stage{
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

   
