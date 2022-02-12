pipeline {
  agent any

  stages {

    stage('check the ami version') {

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
          sh 'python3 check_ami_version.py'

        }
      }
    }
  }

}
