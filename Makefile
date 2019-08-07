all:

requirements:
	pip install -r requirements.txt

test:
ifdef MOLECULE_DEBUG
	molecule --debug test
else ifdef MOLECULE_KEEP
	molecule test --destroy=never
else
	molecule test
endif
