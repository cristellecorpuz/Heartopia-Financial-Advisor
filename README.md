# 💰 Heartopia-Financial-Advisor
As an avid Heartopia player, I often found myself trying to find methods to earn enough coins to buy cute clothes, furniture, land, build houses, or even test my luck with Naughty's Treasures. Like most cozy games, Heartopia offers several hobbies such as Cooking, Fishing, Bird Watching, and Insect Catching where players can collect items and sell them to Albert Jr. for coins. Since every item has a different selling price, I had to manually calculate how many items I needed to sell to reach my weekly goal of 1 million coins.

That's what inspired this project. Heartopia Financial Assistant is an AI-powered chatbot designed to help players make smarter financial decisions in the game. Its knowledge base contains hobby items and their corresponding selling prices, allowing players to ask questions such as "How much can I sell my Blueberry Jam for?" or "What's the quickest way to earn 1 million coins?" Instead of manually doing the math, players can simply ask the chatbot and receive instant, context-aware answers.

# App Preview
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/6b11a14c-5b07-475e-ae83-a4a029de1d01" />
<p align="center"> Figure 1. Chat interface </p>
The application is deployed using Streamlit. Figure 1 shows the chat interface that users interact with after launching the application. The application, named Heartopia Financial Advisor, allows users to enter questions in the text input box at the bottom of the interface. In the example shown, the user asks, "How much profit does Blueberry make?", and the large language model (LLM) generates an appropriate response based on its knowledge base. Below the response is a feedback feature that enables users to evaluate the quality of the answer by clicking either the thumbs up or thumbs down button. This feedback can be used to assess the chatbot's performance and improve future responses. Users can also navigate to other pages through the side bar navigation panel on the left side where a short description of the project and a disclaimer is seen.

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/063f675e-3621-4914-9578-82bf428cbe26" />
<p align="center"> Figure 2. Review Page </p>
The review page is where users can freely submit suggestions on ways the application can improve. The submitted form is appended to my csv.

<<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/b0d72efb-7131-4a8f-a141-fe1ab95011c9" />
<p align="center"> Figure 3. Dashboard </p>
The dashboard page shows live update of feedbacks and recent queries of the user. This ensures that the developer can easily track and monitor anomalies while deployed.

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/32d7e938-06e1-48d9-b119-664cbb34c848" />
<p align="center"> Figure 4. Credentials </p>
The credentials is a simple page showing the developer's details and where the data came from.

# How It Works
