#!/bin/sh
file="/app/workspace/autoexec.sh"
alpg="/app/workspace/${DEMKIT_FOLDER}/alpg.sh"
if [ -f $file ]
then
	cd /app/workspace
	sh /app/workspace/autoexec.sh	
elif [ -f $alpg ]
then
	cd /app/workspace/${DEMKIT_FOLDER}
	sh /app/workspace/${DEMKIT_FOLDER}/alpg.sh	
	mv alpg.sh alpg_file.sh	
	cd /app
	python3 -u -m demkit.demkit -f ${DEMKIT_FOLDER} -m ${DEMKIT_MODEL}
else
	cd /app
	python3 -u -m demkit.demkit -f ${DEMKIT_FOLDER} -m ${DEMKIT_MODEL}
fi
