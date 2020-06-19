# Pingu
Request your homepage via a cron job

This is intended to run on some 'always on' device running linux/macos. Personally I'm using it on a raspberry pi to keep power consumption to a minimum however any linux device will work.

To install and use:
I assume you have python 3 and pipenv installed on your machine.

```
git clone git@github.com:Jompra/pingu.git Pingu
cd Pingu
pipenv shell
pipenv install
sudo python3 pingu.py
```
sudo is required to edit the cron jobs. You may need to enter yourr password or press okay on a dialogue box.

Pingu creates a cron job to run a script that will request your homepage and then do nothing with it. It's handy for keeping sleepy servers alive.

Initally intended to run on a raspberry pi with raspbian but ultimately can run on any mac/linux machine, just make sure it's always on.

This was a super quick rush together so please send me a PR with any improvements.

## Uninstall
You can stop the process working by simply removing the pingu directory:
CD to the directory where Pingu is saved and carefully type:
```
rm -rf Pingu
```

however to remove the cron job do the following:
```
sudo env EDITOR=nano crontab -e
```
Delete any lines ending with Pingu/ping.py
Control o, enter, then control x.
Press okay on any dialogue box

## Improvements

Please feel free to fork the repo and add any clever functionality that you have.