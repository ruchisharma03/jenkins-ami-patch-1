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
          script {

            def result = sh(returnStdout: true, script: 'python3 check_ami_version.py')

            for (String jobStatus: result.split(',')) {

              String[] eachjobStatus = jobStatus.split(':');

              if (eachjobStatus.size() > 1) {

                serviceAmiIdChanged[eachjobStatus[0]] = eachjobStatus[1];
              }

            }
          }
          echo "${serviceAmiIdChanged}"

        }
      }
    }
    // create the jobs dynamically
    stage('build the job if the latest ami id is present') {

      agent any

      steps {

        script {

          def jobList = readJSON file: "${env.WORKSPACE}/${params.JOBCONFIG_FILE_PATH}";
          println(jobList);
          jobList["jobs"].each {
            eachJob ->
              if (serviceAmiIdChanged["${eachJob.job_name}"]) {

                build job:"${eachJob.job_name}"
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
      jiraSendDeploymentInfo site: 'raghav-personal.atlassian.net', 
      environmentId: 'us-prod1', environmentName: 'us-prod2', 
      environmentType: 'production', issueKeys: ['DEV-001', 'DEV-002']
    }
    failure {
      echo "====++++only when failed++++===="
    }
  }

}