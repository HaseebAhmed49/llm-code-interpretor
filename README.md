# LangChain - Develop LLM powered applications with LangChain
## LangChain QR Code Interpretor and CSV Agent
In this code, there are two agents (CSV and QR Code Intrepretor), output will be on prompt based. Agent will be selected in runtime.

# Application Output Screenshots
## Python Agent
![image](https://github.com/user-attachments/assets/44e920d1-5a74-4325-9b0a-40ff9034ec86)

## CSV Agent Runtime Selection
![image](https://github.com/user-attachments/assets/0efc244d-affc-497e-aa5c-c2baf1f6f12b)

### Steps to run the application

1. Install Python=3.11.
2. Install Pycharm
3. Clone the repository
```bash
git clone "repository-url"
```
4. Generate a separate interpretor by following these steps
     1. Open Interpretor in Preferences
     2. Add Local Interpretor using this image ![image](https://github.com/user-attachments/assets/c65b6f06-66a0-4d12-87a8-5bbc557c7665)
     3. Click on Pipenv Environment
     4. Add Base Interpretor (Python path where its installed by using "which python3" on terminal)
     5. Add Pipenv executable (Python path where its installed by using "which pipenv" on terminal)
        1. Run the command "pip install pipenv" (if pipenv not installed)
     6. See this screenshot for Step 4.4 and 4.5
        ```bash
        which python3
        which pipenv
        pip install pipenv
        ```
5. Generate .env file and store API Keys as in image
 ```bash
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```
6. Install all the dependencies using pipfile
```bash
cd llm-code-interpretor
pipenv install
```
7. Start "pipenv shell" environment in terminal (Make sure you're in working directory)
```bash
pipenv shell
```
 ![image](https://github.com/user-attachments/assets/09759085-e140-4197-9819-af3a32168510)
8. Run the application in pycharm.

** This is a test applications. Errors and Ommissions are accepted ** 
** Developed & Tested this LangChain ChatBot application in macOS **

*** In case of any errors, contact at "haseebahmed02@gmail.com" or Whatsapp "+447949067041". Will debug the application at your end and let it run ***

Thanks for your visit to my profile.

