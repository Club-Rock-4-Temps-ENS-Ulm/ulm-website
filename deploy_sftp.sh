#!/usr/bin/env bash

set -o allexport; source .env; set +o allexport

rm -rf output/
make html
cd output
sed -i '' -e 's/=\"\//=\"\/public\/output\//g' *.html
cd pages
sed -i '' -e 's/=\"\//=\"\/public\/output\//g' *.html
cd ..
cd ..

echo $usr@$host
lftp --env-password sftp://$usr@$host -e "cd public; mirror -R output/; bye"
