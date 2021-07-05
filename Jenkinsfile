pipeline {
  environment {
    PROJECT_DIR = "/Account-Generator"
    CONTAINER_NAME = "account-generation"
    DOCKER_ACCOUNT = "jamesdidit72"
    REGISTRY = $DOCKER_ACCOUNT + $CONTAINER_NAME
    registryCredential = "docker_auth"
    dockerImage = ''
  }

  agent any

  options {
    skipStagesAfterUnstable()
  }

  stages {
    stage('Clone from Git') {
    		steps {
            git branch: 'main',
            url: 'https://github.com/oabuoun/account_manager.git'
    		}
    }

    stage('Build-Image') {
    	steps{
        sh '''
  			  docker build -t $registry:$BUILD_NUMBER .
        '''
    	}
    }

    stage('Test') {
    	steps {
        script {
          sh '''
            docker run --rm --tty -v $PWD/test-results:/reports --workdir $PROJECT_DIR --name $CONTAINER_NAME $REGISTRY:$BUILD_NUMBER pytest --cov=. --cov-report=html:/reports/html_dir --cov-report=xml:/reports/coverage.xml
          '''
        }
      }
    	post {
    			always {
    					junit testResults: '**/test-results/*.xml'
    			}
    	}
    }

    stage('Deploy Image') {
    	steps{
    			script {
    					docker.withRegistry( '', registryCredential ) {
    							dockerImage.push()
    					}
    			}
    	}
    }

    stage('Remove Unused docker image') {
    	steps{
    			sh "docker rmi $registry:$BUILD_NUMBER"
    	}
    }
  }
}
