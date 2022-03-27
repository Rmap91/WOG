node {
    checkout scm

    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {

        def customImage = docker.build("rmap91/world_of_Games")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}
