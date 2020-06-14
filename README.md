# Pingu
Request your homepage via a cron job

To install and use:

```
git clone git@github.com:Jompra/pingu.git Pingu
pipenv shell
pipenv install
sudo python3 pingu.py
```
sudo is required to edit the cron jobs. You may need to enter yourr password or press okay on a dialogue box.

Pingu creates a cron job to run a script that will request your homepage and then do nothing with it. It's handy for keeping sleepy servers alive.

Initally intended to run on a raspberry pi with raspbian but ultimately can run on any mac/linux machine, just make sure it's always on.

This was a super quick rush together so please send me a PR with any improvements.

##Uninstall
You can stop the process working by simply removing the pingu directory:
```
rm -rf pingu
```

however to remove the cron job do the following:
```
sudo env EDITOR=nano crontab -e
```
Delete any lines with 'Keeping YOUR-SITE-NAME alive'
Control o, enter, then control x.
Press okay on any dialogue box