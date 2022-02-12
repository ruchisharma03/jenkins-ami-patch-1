pipeline {
  agent any

  stages {

    stage('build a job') {

      steps {
        withCredentials([
          [
            $class: 'AmazonWebServicesCredentialsBinding',
            credentialsId: "aws-creds",
            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
          ]
        ]) {
          // AWS Code
          sh 'python3 --version'

        }
      }
    }
  }

}
