# Pingu
Request your homepage via a cron job

To install and use:

```
git clone git@github.com:Jompra/pingu.git Pingu
pipenv shell
pipenv install
python3 pingu.py
```

Pingu creates a cron job to run a script that will request your homepage and then do nothing with it. It's handy for keeping sleepy servers alive.

Initally intended to run on a raspberry pi with raspbian but ultimately can run on any mac/linux machine, just make sure it's always on.

This was a super quick rush together so please send me a PR with any improvements.