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
      script{
        def testIssue = [fields: [ project: [key: 'RFC'],
                                  summary: 'New JIRA Created from Jenkins.',
                                  description: 'New JIRA Created from Jenkins.',
                                  issuetype: [id: '10002']]]

        response = jiraNewIssue issue: testIssue, site: 'raghav-personal'

        echo response.successful.toString()
        echo response.data.toString()
      }
    }
    failure {
      echo "====++++only when failed++++===="
    }
  }

}