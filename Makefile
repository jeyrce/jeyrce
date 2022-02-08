
hub=docker.io
imageName=jeyrce/jeyrce:latest
tag=${hub}/${imageName}

.phony: all
all: image index

.phony: image
image:
	docker build -t ${tag} .
	docker push ${tag}

.phony: index
index:
	docker run -it --rm --name jeyrce -d ${tag}
	docker cp jeyrce:/jeyrce/index.html .
	docker stop jeyrce
