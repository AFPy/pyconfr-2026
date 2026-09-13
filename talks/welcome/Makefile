SRC := intro.md
HTML := $(SRC:.md=.html)

.PHONY: all
all: $(HTML)

%.html: %.md
	mdtoreveal $< -o $@
