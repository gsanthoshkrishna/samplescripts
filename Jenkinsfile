pipeline{
 agent any
  stages{
    stage('test stage'){
      steps{
        script{
         currentBuild.displayName = "build-${env.BUILD_NUMBER}"
         currentBuild.description = "descriptionl--${env.CHANGE_ID}"
          echo "CHANGEID ${env.CHANGE_ID}"
         echo "build-id ${env.BUILD_ID}"
        }
      }
    }
  }
}
