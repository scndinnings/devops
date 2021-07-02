pipeline {
    agent any 
  
stages { 

  stage('Server Creation') {
       steps {
         sh label: '', script: 'ansible-playbook /var/lib/jenkins/Ansible/ec2.yml'
			}
   }
 
  stage('Unit Tomcat Setup') {
      steps {
		sh label: '', script: '/var/lib/jenkins/Ansible/Tomcat.yml'
      
      }
 }

}
post {
        success {
            mail to:"raknas000@gmail.com", subject:"FAILURE: ${currentBuild.fullDisplayName}", body: "Build failed"
        }
        failure {
            mail to:"raknas000@gmail.com", subject:"FAILURE: ${currentBuild.fullDisplayName}", body: "Build failed"
        }
    }       
}
