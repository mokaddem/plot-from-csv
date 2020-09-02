sudo apt-get install python3-virtualenv virtualenv -y

if [ -z "$VIRTUAL_ENV" ]; then
    virtualenv -p python3 venv ; venv=$?

    if [[ "$venv" != "0" ]]; then
      echo "Something went wrong with the virtualenv."
      echo "Please investigate manually."
      exit $venv
    fi

    . ./venv/bin/activate
fi

pip3 install -U -r requirements.txt
