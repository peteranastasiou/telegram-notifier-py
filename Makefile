
PUSHOVER_APIKEY=`cat .apikey`
PUSHOVER_USERKEY=`cat .userkey`

build:
	sudo docker build \
		--build-arg PUSHOVER_APIKEY=${PUSHOVER_APIKEY} \
		--build-arg PUSHOVER_USERKEY=${PUSHOVER_USERKEY} \
		-t push-notifier-service .

run: build
	sudo docker run -p 80:80 push-notifier-service
