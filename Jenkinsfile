pipeline{
 agent any
  stages{
    stage('test stage'){
      steps{
        script{
         currentBuild.displayName = "build-${env.BUILD_NUMBER}"
         currentBuild.description = "description--${env.BUILD_NUMBER}"
          echo 'test PR3'
        }
      }
    }
  }
}
