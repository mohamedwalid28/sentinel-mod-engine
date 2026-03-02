# 🛡️ Sentinel: AI-Driven Community Moderation

**Sentinel** is a specialized microservice designed to protect online communities from toxicity, spam, and—crucially—**medical misinformation**. 

While platforms like Circle.so provide basic moderation, **Sentinel** adds an intelligent layer of "Product Thinking" to automate safety and track the emotional health of the community.

### 🚀 Key Features
- **Medical-Safety Scoring:** Uses NLP to flag dangerous medical advice or unverified cures.
- **Automated "Guardian" Logic:** Auto-bans repeat offenders and flags high-risk content for admin review via Circle API.
- **Sentiment Analytics:** Tracks community "Health Metrics" to alert founders of shifts in patient morale.
- **Circle-Native Integration:** Plug-and-play webhook support for Circle.so.

### 🛠 Tech Stack
- **Language:** Python 3.11
- **ML Framework:** Scikit-learn (NLP / Logistic Regression)
- **API:** FastAPI (Asynchronous)
- **Deployment:** Docker
