# GapScanner
A tool that scans a set of tickers for the largest price gap from the previous days market close to the current time. Can be used to find the largest gap ups during premarket.

# How to Use:
- This tool requires the following Python modules:
  - time, yfinance, pandas, ray, datetime, tkinter, ttk, and threading.
- After installing the above modules, navigate to the directory containing gui.py in a terminal and run `python gui.py`.
- Upon running it will begin to load which should only take about 1 minute (assuming tickers.py has not been updated).

![image](https://user-images.githubusercontent.com/81063978/232839785-4be0ca32-c677-4e22-81df-6ea9ff021ed1.png)

- After loading, 50 of the tickers with the largest gap ups will appear in a table.

![image](https://user-images.githubusercontent.com/81063978/232840161-ea32ad68-d0d1-4f0d-ba63-fdde11839f3e.png)

# Tips:
- Set of tickers can be personalized by editing the tickers in tickers.py.
- Currently, tickers.py only contains small cap tickers with prices below $10.
- Adding a large number of tickers will increase the load time of the program.

# Notes:
- This tool can be useful for finding which stocks will be popular on market open, but does not always indicate winning stocks. 
- Additional research should be done on these stocks before making a decision to trade.
- Sometimes the data recieved from yfinance can be faulty, resulting in false output.
