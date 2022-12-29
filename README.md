# datasecurity
Data security performance analysis developed in Python (Flask) - SQL (SQLite).

# Installation
```diff
# Go to the requirements folder
cd pip

# Run the command
pip install -r requirements.txt
```

# Database Migration
```diff
# Run the following commands in order
python db.py sqlite init
python db.py sqlite migrate
python db.py sqlite upgrade
```

# RabbitMQ - Publisher
```diff
# Go to data folder
cd data

# Running the publisher agent
python main.py
```

# RabbitMQ - Subscriber
```diff
# Running the subscriber agent
python subscriber.py
```

# Flask
```diff
python core.py
```

# Database Migration - Image
![image](https://user-images.githubusercontent.com/88355373/210005478-feccc6be-6ba6-4705-84d3-44e4e5d10a8d.png)

# RabbitMQ - Image
# HTTP POST
![image](https://user-images.githubusercontent.com/88355373/210005438-ffa7fd52-a87b-42fb-909f-63dc1609f1dd.png)
![image](https://user-images.githubusercontent.com/88355373/210005520-e8fe48ef-9690-4e40-9510-3635c5a56e68.png)

# HTTP UPDATE
![image](https://user-images.githubusercontent.com/88355373/210005580-c1b56bc5-7373-4500-a7e8-bc63c1f12526.png)
![image](https://user-images.githubusercontent.com/88355373/210005595-5c062431-05ab-41d5-9b56-3aa908357833.png)

# HTTP DELETE
![image](https://user-images.githubusercontent.com/88355373/210005604-a9020ef1-61d0-473b-9288-0ec3be61f47f.png)
![image](https://user-images.githubusercontent.com/88355373/210005610-fe9d74dc-d261-47f0-a59d-3f4dd378c8f4.png)

