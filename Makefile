.PHONY: docs
docs:
	@## output=OUTPUT_PATH
	@#
	@# Build documentation

	cd docs; make dirhtml
	if [ $(output) ]; then mkdir -p $(output); mv docs/build/dirhtml/* $(output); fi
