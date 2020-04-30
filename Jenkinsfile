pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh "docker build -t fibonacci:${env.GIT_COMMIT} -f build/Dockerfile ."
      }
    }

    stage('Test') {
      parallel {

        stage('Unit Tests') {
          steps {
            sh "docker run -i fibonacci:${env.GIT_COMMIT} pytest tests/unit"
          }
	}

        stage('Integration Tests') {
          steps {
            sh "docker run -i fibonacci:${env.GIT_COMMIT} pytest tests/integration"
          }
	}
      }
    }

    stage('Cleanup') {
      steps {
        sh "docker images rm --all"
      }
    }
  }
}