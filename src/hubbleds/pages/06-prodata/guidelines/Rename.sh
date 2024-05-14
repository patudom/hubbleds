#!/bin/bash

# convert all files to PascalCase
# 1) Get the list of files
# 2) For each file, convert the name to PascalCase
# 3) Rename the file using mv command

# define function that converts snake_case to PascalCase
function snake_to_pascal() {
  echo $1 | sed -r 's/(^|_)([a-z])/\U\2/g'
}

# get the list of files
files=$(ls)

# for each file, convert the name to PascalCase
for file in $files
do
  # convert the name to PascalCase
  new_name=$(snake_to_pascal $file)

  # rename the file
  mv $file $new_name
done
