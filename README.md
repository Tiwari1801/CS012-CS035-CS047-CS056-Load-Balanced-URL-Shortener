cd url-shortener
touch app.py requirements.txt Dockerfile

<img width="688" alt="image" src="https://github.com/user-attachments/assets/dc5612b3-1cc3-4681-b3f3-06622a0ad15b" />

docker build -t url-shortener:latest .

<img width="959" alt="image" src="https://github.com/user-attachments/assets/f6d22414-2c6e-4dd6-ae10-2490585c76d1" />

docker run -d --name redis -p 6379:6379 redis

<img width="959" alt="image" src="https://github.com/user-attachments/assets/f5d02500-8ac3-46fc-8c4e-23d72485746a" />

docker run -d --name url-shortener -p 5000:5000 --link redis:redis url-shortener:latest

<img width="959" alt="image" src="https://github.com/user-attachments/assets/6cb4530d-68c9-43a5-96c2-6e0a2aeb8cb2" />

curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://localhost:5000/shorten

<img width="947" alt="image" src="https://github.com/user-attachments/assets/d55a2755-7221-4c08-b15a-83bea9ac7145" />

Example.com website hosted as localhost

<img width="960" alt="image" src="https://github.com/user-attachments/assets/b052794a-702a-4c7c-9d92-fb93d98efda7" />

