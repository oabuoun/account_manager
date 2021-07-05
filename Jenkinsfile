pipeline {
  environment {
    registry = "oabuoun/account-generation"
    IMAGE_NAME=${REG}:${BUILD_NUMBER}
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
            docker run --tty --name $registry:$BUILD_NUMBER pytest
          '''
        }
      }
    	post {
    			always {
    					junit testResults: '**/test-results/*.xml'
    			}
    	}
    }
    stage('Test account deletion') {
    	agent {
    			docker {

    					image 'qnib/pytest'
    			}
    	}
    	steps {
          sh '. venv/bin/activate && pip install -r requirements.txt'
    			sh 'virtualenv venv --distribute && pip install --upgrade pip && . venv/bin/activate && pip install -r requirements.txt && ./test_account_deletion.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_acc_deletion.xml'
    			}
    	}
    }
    stage('Test account management') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
    			sh './test_account_management.sh'
    	}
    	post {
    			always {

    					junit 'test-reports/results_acc_management.xml'
    			}
    	}
    }
    stage('Test password control') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
    			sh './test_password_control.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_password_control.xml'
    			}
    	}
    }
    stage('Test password response') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
          sh 'python3 -m venv venv'
          sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
    			sh './test_password_response.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_password_response.xml'
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
