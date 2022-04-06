pipeline{

  agent any
  environment{
    IMAGE_NAME = "dezy433/spartan_project_vagrant-main:" + "$BUILD_NUMBER"
  }
  stages{
    stage('Cloning the project from Github'){
      steps{
        git branch: 'master',
        url: 'https://github.com/dezy433/spartan_project_vagrant-main.git'
        }
      }

      stage('Build Docker Image'){
        steps{
            script {
              DOCKER_IMAGE = docker.build IMAGE_NAME
          }
        }
        stage('Push to Docker Hub'){
          steps{
            script{
              docker.withRegistry('', 'docker_hub_cred'){
                DOCKER_IMAGE.push()
              }
            }
          }
      }
    }
  }
}
