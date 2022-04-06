pipeline{
  agent any


  environment{
    IMAGE_NAME = "dez433/spartan_project_jenkins:3." + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_cred'
   }


  stages {
      stage('Cloning the project from GitHub'){
        steps {
          checkout([
              $class: 'GitSCM', branches: [[name: '*/master']],
              userRemoteConfigs: [[
                url: 'git@github.com:dezy433/spartan_project_jenkins.git',
                credentialsId: 'ssh_git_cred'
              ]]
            ])
        }
      }

    stage('Build Docker Image'){
      steps{
          script {
            DOCKER_IMAGE = docker.build IMAGE_NAME
          }
        }
      }
    stage('Testing the code'){
      steps{
        script{
          sh'''
            docker run --rm -v $PWD/test-results:/reports --workdir /app $IMAGE_NAME pytest -v --junitxml=/reports/results.xml
            ls $PWD/test-results
            '''
          }
        }

      post{
        always{
          junit testResults: '**/test-results/*.xml'
        }
      }
    }
    stage('Push to Docker Hub'){
      steps {
        script {
          docker.withRegistry('', DOCKER_CREDENTIALS){
            DOCKER_IMAGE.push()
        }
      }
    }
  }

    stage('Removing the Docker Image'){
      steps {
        sh "docker rmi $IMAGE_NAME"
      }
    }
  }
}
