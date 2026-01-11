pipeline {
    agent any
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

   
