# dashframe-template-v2
realtime data generation streamed to localhost dash framework server

<img width="587" alt="Screenshot 2023-07-31 at 1 39 20 PM" src="https://github.com/ishaan-awasthi/dashframe-template-v2/assets/136520517/b531fa07-385f-4eb3-9ee4-03ca7685fe99">

This package visualizes four CSV files. The 'sleep' and 'steps' files are hardcoded with data, while the 'heart' and 'spo2' CSVs are continuously updated in real time with new data generated from a finetuned RNG.

<img width="854" alt="Screenshot 2023-07-31 at 1 42 31 PM" src="https://github.com/ishaan-awasthi/dashframe-template-v2/assets/136520517/8212a4e5-be70-4c84-bf4e-7ec054f7f74a">

The backend framework runs on interacting three scripts: two python and one bash shell. While app.py initializes the localhost server, rng.py generates new data in real time to the csv files. The touch.sh script then pings app.py, forcing a refresh of the data.

<img width="1053" alt="Screenshot 2023-07-31 at 1 49 38 PM" src="https://github.com/ishaan-awasthi/dashframe-template-v2/assets/136520517/e9babc5a-7c7a-415f-b471-7a0de0b3481a">

Steps to operate package:
0. Make sure python and MacOS are installed
1. Open terminal in preferred profile and navigate to dashframe-template-v2/scripts via [$cd ~/path]
2. Open two more tabs in the terminal window via [⌘T] or [Shell-->New Tab]
3. In the first tab, run '$python app.py' and open the localhost URL in preferred browser and wait for visualizations to render
4. In the second tab run '$python rng.py' and immediately switch to the third tab
5. In the third tab run '$sh touch.sh'
6. Your dashboard will update every 10 seconds in the localhost URL. This can be modified in the rng and touch scripts 
7. To close the dashboard, close the terminal window and terminate all shell proccesses
