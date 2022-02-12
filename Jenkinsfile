pipeline {
  agent any
  def region_ami_id_match = [:]
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
          script {
            def region_ami_id_match = sh(returnStdout: true, script: 'python3 check_ami_version.py')
            echo "${region_ami_id_match}"
          }

        }
      }
    }
  }

}