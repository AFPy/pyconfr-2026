SRC := pres.md
HTML := $(SRC:.md=.html)

.PHONY: all
all: $(HTML)

%.html: %.md
	../../.venv/bin/mdtoreveal $< -o $@
