pipeline{
 agent any
  stages{
    stage('test stage'){
      steps{
        script{
         currentBuild.displayName = "build-${env.BUILD_NUMBER}"
          currentBuild.description = "${env.CHANGE_ID}"
          echo 'test PR3'
        }
      }
    }
  }
}
