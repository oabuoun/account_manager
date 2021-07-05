pipeline {
  environment {
    conainer_name = "account-generation1"
    registry = "oabuoun/account-generation"
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

    stage('Build-Test-Image') {
    	steps{
        sh '''
          pwd
          ls -la
  			  docker build -t $registry:$BUILD_NUMBER .
        '''
    	}
    }

    stage('Test access rights') {
    	steps {
        script {
          sh '''
            docker run --rm --tty -v $PWD/test-results:/reports --workdir /Account-Generator --name $conainer_name $registry:$BUILD_NUMBER pytest --cov=. --cov-report=html:reports/html_dir --cov-report=xml:reports/coverage.xml
          '''
        }
      }
    	post {
    			always {
    					junit testResults: '**/test-results/*.xml'
    			}
    	}
    }

    stage('Build-Image') {
    	steps{
    		script {
    			dockerImage = docker.build registry + ":$BUILD_NUMBER"
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
