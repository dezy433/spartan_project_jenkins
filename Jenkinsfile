pipeline{

  agent any

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
              DOCKER_IMAGE = docker.build 'dezy433/spartan_project_vagrant-main'
            }
          }
        }
        stage('Push to Docker Hub')
          steps{
            script{
              docker.withRegistry('', 'docker_hub_cred'){
                DOCKER_IMAGE.push()
              }
            }
          }
      }
    }
