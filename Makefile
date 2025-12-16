
build:
	sudo docker build -t telegram-notifier-py .

run: build
	sudo docker run -p 80:80 telegram-notifier-py
