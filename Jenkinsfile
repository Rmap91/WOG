node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {

        def customImage = docker.build("rmap91/'worldofgames")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
