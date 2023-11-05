.PHONY: clean build

SCRIPT_NAME = gpu_info.py

OUTPUT_DIR = dist

clean:
	rm -rf $(OUTPUT_DIR)

build:
	pyinstaller --onefile $(SCRIPT_NAME)

