.PHONY: test

test:
	circleci local execute -e CIRCLE_PROJECT_REPONAME=$(shell basename $(shell pwd)) -e RHN_USER=${RHN_USER} -e RHN_PASS=${RHN_PASS} --job test
