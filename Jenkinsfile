//  store 'region': 'if ami matched or not'
def regionAmiIdMatch = [: ]

pipeline {
  agent none
  stages {
    stage('check the ami version') {
      agent any
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

            def result = sh(returnStdout: true, script: 'python3 check_ami_version.py')

            for (String eachjobStatus: result.split(',')) {

              String[] status = eachjobStatus.split(':');
              if(status.size > 0){

                  regionAmiIdMatch[status[0]] = status[1];
              }

            }
            echo "${regionAmiIdMatch}"
          }

        }
      }
    }

  }

}