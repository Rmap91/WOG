pipeline {
  agent {
    node {
      label 'ubuntu'
    }
  }
  stages {
    stage("checkout") {
      steps {
        checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [
          [name: '*/main']
        ], extensions: [
          [$class: 'WipeWorkspace']
        ], userRemoteConfigs: [
          [credentialsId: '***', url: 'https://github.com/Rmap91/WOG']
        ]]
      }
    }
    stage("build") {
      steps {
        script {
            sh "docker build -t world_of_games:${BUILD_NUMBER} ."
            sh "docker run -d --name wog${BUILD_NUMBER} world_of_games:${BUILD_NUMBER}"
        }
      }
    }
        stage("test") {
            steps {
                script{
                    // sh "docker start wog${BUILD_NUMBER}"
                    sh "ls -l"
                    sh "docker exec wog${BUILD_NUMBER} python3 /app/e2e.py"
            }
        }
        }
    
  }
}
