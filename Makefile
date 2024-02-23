build:
	docker build \
		--build-arg INSTALL_GROUPS="main" \
		-t exercise-data-pipeline \
		.

build-dev:
	docker build \
		--build-arg INSTALL_GROUPS="main,dev" \
		-t exercise-data-pipeline-dev \
		.

pyright: build-dev
	docker run \
		--rm -it \
		--entrypoint=pyright \
		exercise-data-pipeline-dev \
		--project /app/pyproject.toml \
		/app

pytest: build-dev
	docker run \
		--rm -it \
		--entrypoint=pytest \
		exercise-data-pipeline-dev \
		-vv

coverage: build-dev
	docker run \
		--rm -it \
		--entrypoint=pytest \
		exercise-data-pipeline-dev \
		-vv \
		--cov=src/ \
		--cov-report term \
		--cov-report json:coverage.json \
		--cov-report html:cov_html
