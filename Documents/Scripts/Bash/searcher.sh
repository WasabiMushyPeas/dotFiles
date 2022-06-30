#!/bin/bash
hilighted=$(xsel)
search="https://google.com/search?q="
hilighted=${hilighted// /+}
kitty -e firefox $search$hilighted
