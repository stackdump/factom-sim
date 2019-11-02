#!/usr/bin/env bash

# test the sim server using factom-cli
which factom-cli >> /dev/null
if [[ $? -ne 0 ]] ; then
    echo "factom-cli must be installed"
    exit 1
fi

function import() {
	factom-cli importaddress Fs3E9gV6DXsYzf7Fqx1fVBQPQXV695eP3k5XbmHEZVRLkMdD9qCK # FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q
	factom-cli importaddress Es3C7Ybmj8qoG1xZNrTm18EWKjW3BgvXQDFWZ1q1LvxxUBW5S5DL # EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj
}

function buyec() {
	factom-cli buyec FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj 2000
}

function list() {
	factom-cli listaddresses
}

case $1 in
import | buyec | list)
	$1
	;;
*)
	echo "test using factom-cli : ./test.sh [import|buyec|list]"
	exit -1
	;;
esac
