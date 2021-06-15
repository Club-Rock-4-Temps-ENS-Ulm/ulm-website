#!/usr/bin/env bash

set -o allexport; source .env; set +o allexport

# Publish for /public/
rm -rf public/
make html
cd public
sed -i '' -e 's/=\"\//=\"\/public\//g' *.html
cd pages
sed -i '' -e 's/=\"\//=\"\/public\//g' *.html
cd ..
cd ..

echo $usr@$host

#mv output public

lftp --env-password sftp://$usr@$host -e "mirror -R public/; bye"

# Publish for /public/output


#cp -R public output
#lftp --env-password sftp://$usr@$host -e "cd public; mirror -R output/; bye"
#rm output