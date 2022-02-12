//  store 'region': 'latest ami is present or not'
def serviceAmiIdChanged = [: ]

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

            for (String jobStatus: result.split(',')) {

              String[] eachjobStatus = jobStatus.split(':');

              if (eachjobStatus.size() > 1) {

                serviceAmiIdChanged[eachjobStatus[0]] = eachjobStatus[1];
              }

            }
          }
          echo "${regionAmiIdMatch}"

        }
      }
    }
    // create the jobs dynamically
    stage('build the job if the latest ami id is present') {

      agent any

      steps {

        script {

          def serviceList = readJSON file: "${env.WORKSPACE}/config/jobconfig.json";
          println(serviceList);
          serviceList["jobs"].each {
            eachService ->
              if (serviceAmiIdChanged[$serviceList.job_name]) {

                println(eachService.job_name)
              }

          }
        }
      }

    }

  }

  post {
    always {
      echo "====++++always++++===="
    }
    success {
      echo "====++++only when successful++++===="
    }
    failure {
      echo "====++++only when failed++++===="
    }
  }

}