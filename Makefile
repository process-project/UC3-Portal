.PHONY: all

build:
	docker build -t microinfrastructure/process-uc3-portal:3938873 .

run: build
	docker run -it microinfrastructure/process-uc3-portal:3938873 /bin/sh

push: build
	docker push microinfrastructure/process-uc3-portal:3938873

