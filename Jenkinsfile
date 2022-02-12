//  store 'region': 'latest ami is present or not'
def serviceAmiIdChanged = [: ]

pipeline {
  agent none

  parameters{

    string(name:'AWS_AGENT_LABEL',defaultValue:'any',description:'Label of the Agent which has python3 and aws profile configured')
    string(name:'AGENT_LABEL',defaultValue:'any',description:'Label of the Agent on which to execute the JOBS')
    string(name:'JOBCONFIG_FILE_PATH',defaultValue:'config/jobconfig.json',description:'Path of the job config file')
    string(name:'AWS_SERVICE_CONFIG_FILE',defaultValue:'./config/config.json',description:'Path of the aws service config file')
  }

  stages {
    stage('check the ami version') {
      agent  any
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

                build job: "${eachJob.job_name}", parameters: eachJob.parameters
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
      // jiraSendBuildInfo site: 'raghav-personal.atlassian.net'
    }
    failure {
      echo "====++++only when failed++++===="
    }
  }

}