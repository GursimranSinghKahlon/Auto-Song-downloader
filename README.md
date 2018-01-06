# Auto-Song-dowloader
Download top-daily songs automatically by a single click

Pros: It do not download songs already present in folder of local disk

Requirement: python 2.7

If any library not found:
  Recommended(Reinstall python 2.7.x)
  Follow these steps:
  Note: Skip 1 an 2 if pip already install
  1.Add python to environment variables (system)
  2.Install pip (add to env variables if required)

OR  
  Use following command in cmd to install required packages
  "py -2.7 -m pip install SomePackage"
  Replace SomePackage with required package.
  
# Auto-Song-dowloader with progress bar

Note:Download file from progressbar branch

Install following packages(using cmd):
  py -2.7 -m pip install tqdm
  py -2.7 -m pip install requests

Running:
  1.Open cmd
  2.Browse to directory of downloaded python file(Using cd)
  3.Run:
    py -2.7 wapkg_top_today_songs(2.7).py
